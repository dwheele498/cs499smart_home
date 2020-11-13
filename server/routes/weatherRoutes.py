from flask_restful import Resource
from marshmallow import Schema, fields, INCLUDE
from flask import request
import psycopg2
from datetime import datetime
import json
from dbGen.weatherDbGen import CreateConnection, WeatherData, Prediction




class GetWeatherSchema(Schema):
    selectedDate=fields.String()
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
        dates = weatherRequestSchema.load(request.args,unknown=INCLUDE)

        if dates is None:
            return {'message': 'empty data'}, 400
        start = datetime.today().fromisoformat(dates.get('start')[:-1])
        end = datetime.today().fromisoformat(dates.get('end')[:-1])
        WeatherData(start,end),
        connection = CreateConnection()
        data = []
        response = []
        with connection.cursor() as cursor:
            cursor.execute(
                'SELECT tavg,selectedDate,tlow,thigh FROM Weather where selectedDate >=%s and selectedDate <= %s',
                (dates.get('start'), dates.get('end')))
            data = cursor.fetchall()
        for d in data:
            response.append(weather_schema.load({'tavg':d[0],'selectedDate':str(d[1]),'tmin':d[2],'tmax':d[3]}))
        connection.close()
        return({'data': response}), 200


class GetWeatherPrediction(Resource):
    @classmethod
    def get(cls):
        data = Prediction()
        data = data.rename(columns={'ds':'Dates','yhat':'Avg Temp'})
        data = data.astype({'Dates':'str'})
        # data = data.to_json(orient='records')
        return(data.values.tolist()),200

