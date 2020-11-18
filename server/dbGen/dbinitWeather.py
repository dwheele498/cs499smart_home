import math
from datetime import date
import pandas as pd
import psycopg2
import requests
from fbprophet import Prophet
from marshmallow import Schema, fields, ValidationError, INCLUDE


def CreateConnection():
    connection = psycopg2.connect(
        database="Team3DB",
        user="Team3",
        password="3Team3",
        host="127.0.0.1",
        port="5432",
    )
    return connection


def ReCreateWeatherTable():
    connection = CreateConnection()
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE Weather")
        connection.commit()
        cursor.execute(
            "create table weather(id serial PRIMARY KEY, tavg int, tlow int, thigh int, day int, month int)"
        )
        connection.commit()


def DateTable():
    connection = CreateConnection()
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE Weather")
        connection.commit()
        cursor.execute("create table weather(id serial PRIMARY KEY, tavg int, tlow int, thigh int, selectedDate date)")
        connection.commit()



def WeatherData(start:date,end:date):
    if end == date.today():
        end = end.replace(day=date.today().day-1)

    startSplit = start.strftime('%Y-%m-%d')
    endSplit = end.strftime('%Y-%m-%d')

    connection = CreateConnection()

    cursor = connection.cursor()
    cursor.execute(
        "Select selectedDate,tavg,tlow,thigh from weather ",
    )
    weatherTable = cursor.fetchall()
    weatherSet = set(weatherTable)

    size = pd.date_range(start=start,end=end).to_pydatetime().tolist()

    params = {
        "lat": float(33.543682),
        "lon": float(-86.779633),
        "start": startSplit,
        "end": endSplit,
    }

    class CallSchema(Schema):
        lat = fields.Float()
        lon = fields.Float()
        start = fields.String()
        end = fields.String()

    call = CallSchema()
    result = call.dump(params)

    class WeatherSchema(Schema):
        selectedDate: fields.Date()
        tavg: fields.Float()
        tmin: fields.Float()
        tmax: fields.Float()

    if len(weatherTable) == len(size):
        connection.commit()
        connection.close()
        return
    else:

        weather = WeatherSchema()
        res = requests.get(
            "https://api.meteostat.net/v2/point/daily",
            params=result,
            headers={"x-api-key": "1mXl3ltqbTwYp4w7T9F3VylcJGwfzJRh"},
        )
        print(res)
        dataHolder = dict(res.json())
        hold = []
        for r in dataHolder["data"]:
            try:
                z = weather.load(
                    {
                        "selectedDate": date.fromisoformat(r["date"]),
                        "tavg": r["tavg"],
                        "tmin": r["tmin"],
                        "tmax": r["tmax"],
                    },
                    unknown=INCLUDE,
                )
                hold.append(z)
            except ValidationError as err:
                print(err.messages)
        for t in hold:
            if t["tavg"] is not None:
                try:
                    t["tavg"] = math.floor(t["tavg"] * 1.8 + 32)
                    t["tmin"] = math.floor(t["tmin"] * 1.8 + 32)
                    t["tmax"] = math.floor(t["tmax"] * 1.8 + 32)
                except TypeError as err:
                    print(err)
            else:
                try:
                    t["tavg"] = 0
                    t["tmin"] = 0
                    t["tmax"] = 0
                except TypeError as err:
                    print(err)

        for el in hold:
            print(el["selectedDate"])
            tester = (el["selectedDate"], int(el['tavg']), int(el['tmin']), int(el['tmax']))
            if len(weatherSet) > 0:
                if tester in weatherSet:
                    print('duplicate rows')
                else:
                    cursor.execute(
                        "INSERT INTO Weather (tavg,selectedDate,tlow,thigh) VALUES (%s,%s,%s,%s)",
                        (
                            el["tavg"],
                            el["selectedDate"],
                            el["tmin"],
                            el["tmax"],
                        ),
                    )
            else:
                cursor.execute(
                    "INSERT INTO Weather (tavg,selectedDate,tlow,thigh) VALUES (%s,%s,%s,%s)",
                    (
                        el["tavg"],
                        el["selectedDate"],
                        el["tmin"],
                        el["tmax"],
                    ),
                )
        connection.commit()
        cursor.close()

def Prediction():
    connection = CreateConnection()
    with connection.cursor() as cursor:
        cursor.execute("Select selectedDate,tavg from weather where selectedDate >= %s and selectedDate <= %s",('2020-01-01',date.today()))
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=["ds","y"])
        m = Prophet()
        m.fit(df)
        future = m.make_future_dataframe(periods=30,include_history=False)
        prediction = m.predict(future)
        return (prediction[['ds','yhat']])






# ReCreateWeatherTable()
# DateTable()
# WeatherData()
# z = date.today().replace(day=26)
# l = date.today()
# WeatherData(z,l)
# Prediction('2020-01-01','2020-10-31',30)