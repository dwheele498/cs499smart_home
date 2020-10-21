import psycopg2
from datetime import datetime
import requests
import math
from marshmallow import Schema, fields, EXCLUDE, ValidationError, INCLUDE

connection = psycopg2.connect(
    database="Team3DB",
    user="Team3",
    password="3Team3",
    host='127.0.0.1',
    port='5432'
)
cursor = connection.cursor()

def GenerateWeatherDbData():

    cursor.execute("Select temp,day from weather")
    weatherTable = cursor.fetchall()

    connection.commit()


    params = {
        "lat": float(33.543682),
        "lon": float(-86.779633),
        "start": str(datetime.fromisoformat("2020-10-01T00:00").date()),
        "end": str(datetime.now().date()),
    }


    class CallSchema(Schema):
        lat = fields.Float()
        lon = fields.Float()
        start = fields.Str()
        end = fields.Str()


    call = CallSchema()
    result = call.dump(params)


    class WeatherSchema(Schema):
        date: fields.String()
        tavg: fields.String()


    weather = WeatherSchema()
    res = requests.get(
        "https://api.meteostat.net/v2/point/daily",
        params=result,
        headers={"x-api-key": "1mXl3ltqbTwYp4w7T9F3VylcJGwfzJRh"},
    )
    dataHoleder = dict(res.json())
    hold = []
    for r in dataHoleder["data"]:
        try:
            z = weather.load({"date": r["date"], "tavg": r["tavg"]}, unknown=INCLUDE)
            hold.append(z)
        except ValidationError as err:
            print(err.messages)

    for t in hold:
        if t['tavg'] is not None:
            try:
                t['tavg'] = math.floor(t['tavg'] * 1.8 + 32)
            except TypeError as err:
                print(err)
    for el in hold:
        
        if (el['tavg'],datetime.strptime(el['date'],'%Y-%m-%d').date()) in weatherTable:
            print('Duplicate rows')
        else:
            cursor.execute('INSERT INTO Weather (temp,day) VALUES (%s,%s)',(el['tavg'],datetime.strptime(el['date'],'%Y-%m-%d').date()))
    connection.commit()
    cursor.close()
    connection.close()
