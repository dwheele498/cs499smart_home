from flask_restful import Resource
from marshmallow import Schema, fields, EXCLUDE
from flask import request
import psycopg2
from datetime import datetime
from dbGen.weatherDbGen import GenerateWeatherDbData, CreateConnection




class GetWeatherSchema(Schema):
    day = fields.Str()
    month = fields.Str()
    tavg = fields.Int(allow_none=True)
    tmin = fields.Int(required=False)
    tmax = fields.Int(required=False)


class WeatherRequestSchema(Schema):
    start = fields.String()
    end = fields.String()

weather_schema = GetWeatherSchema()
weatherRequestSchema = WeatherRequestSchema()


class WeatherDataMonthly(Resource):
    @classmethod
    def get(cls):
        print(request.args)
        dates = weatherRequestSchema.load(request.args)
        if dates is None:
            return {'message':'empty data'},400
        startSplit = dates.get('start').split('-')
        endSplit = dates.get('end').split('-')
        GenerateWeatherDbData(dates.get('start'),dates.get('end'))
        connection = CreateConnection()
        data = []
        response = []
        with connection.cursor() as cursor:
            cursor.execute('SELECT tavg,day,month,tlow,thigh FROM Weather where month=%s and day between %s and %s',(int(startSplit[1]),int(startSplit[2]),int(endSplit[2])))
            data = cursor.fetchall()
        for d in data:
            print(d)
            response.append(weather_schema.load({'tavg':d[0],'day':str(d[1]),'month':str(d[2]),'tmin':d[3],'tmax':d[4]}))
        connection.close()
        return({'data': response}),200
