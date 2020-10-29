import math

import psycopg2
import requests
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


def GenerateWeatherDbData(start, end):
    startSplit = start.split("-")
    endSplit = end.split("-")

    connection = CreateConnection()

    cursor = connection.cursor()
    cursor.execute(
        "Select day,month,tavg,tlow,thigh from weather ",
        # (int(startSplit[1]), int(startSplit[2]), int(endSplit[2])),
    )
    weatherTable = cursor.fetchall()
    weatherSet = set(weatherTable)

    size = [x for x in range(int(startSplit[2]), int(endSplit[2]) + 1)]

    params = {
        "lat": float(33.543682),
        "lon": float(-86.779633),
        "start": start,
        "end": end,
    }

    class CallSchema(Schema):
        lat = fields.Float()
        lon = fields.Float()
        start = fields.Str()
        end = fields.Str()

    call = CallSchema()
    result = call.dump(params)

    class WeatherSchema(Schema):
        day: fields.String()
        month: fields.String()
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
        dataHoleder = dict(res.json())
        hold = []
        for r in dataHoleder["data"]:
            dateSplit = r["date"].split("-")
            try:
                z = weather.load(
                    {
                        "day": dateSplit[2],
                        "month": dateSplit[1],
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
        for el in hold:
            tester = {(el['day'], el['month'], el['tavg'], el['tlow'], el['thigh'])}
            if len(weatherSet) > 0:
                if tester in weatherSet:
                    print("Duplicate rows")
                else:
                    cursor.execute(
                        "INSERT INTO Weather (tavg,day,month,tlow,thigh) VALUES (%s,%s,%s,%s,%s)",
                        (
                            int(el["tavg"]),
                            int(el["day"]),
                            int(el["month"]),
                            int(el["tmin"]),
                            int(el["tmax"]),
                        ),
                    )
            else:
                cursor.execute(
                    "INSERT INTO Weather (tavg,day,month,tlow,thigh) VALUES (%s,%s,%s,%s,%s)",
                    (
                        int(el["tavg"]),
                        int(el["day"]),
                        int(el["month"]),
                        int(el["tmin"]),
                        int(el["tmax"]),
                    ),
                )
        connection.commit()
        cursor.close()

# ReCreateWeatherTable()
# GenerateWeatherDbData("2020-10-01", "2020-10-09")
