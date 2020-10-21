from flask_restful import Resource
from marshmallow import Schema,fields, EXCLUDE
from flask import request
import psycopg2
from datetime import datetime
from dbinit import GenerateWeatherDbData


connection = psycopg2.connect(
    database="Team3DB",
    user="Team3",
    password="3Team3",
    host='127.0.0.1',
    port='5432'
)


class PostSchema(Schema):
    oToTwenty = fields.Int()
    aMessage = fields.Str()

class GetWeatherSchema(Schema):
    date = fields.Str()
    tavg = fields.Int(allow_none=True)

post_schema = PostSchema()
weather_schema = GetWeatherSchema()

class TestRequest(Resource):
    @classmethod
    def get(cls):
        return{"message":"Test response"},200


class PostTest(Resource):
    @classmethod
    def post(cls):
        data = post_schema.load(request.get_json())
        return {"message":data},200

class WeatherData(Resource):
    @classmethod
    def get(cls):
        GenerateWeatherDbData()
        data = []
        response = []
        with connection.cursor() as cursor:
            cursor.execute('SELECT temp,day FROM Weather')
            data = cursor.fetchall()
        for d in data:
           response.append(weather_schema.load({'date':d[1].strftime('%Y-%m-%d'),'tavg':d[0]}))
        return({"data":response}),200
