from flask_restful import Resource
from marshmallow import Schema, fields, INCLUDE
from flask import request
from datetime import datetime
import psycopg2
from dbGen.weatherDbGen import CreateConnection


class WaterGetSchema(Schema):
    date: fields.Str()
    clotheswasher: fields.Int()
    dishwasher: fields.Int()
    shower: fields.Int()
    bath: fields.Int()


class WaterRequestSchema(Schema):
    end: fields.String(required=False)
    start: fields.String(required=False)


waterRequest = WaterRequestSchema()

waterGet = WaterGetSchema()


class WaterGetMonthly(Resource):
    def get(cls):
        dates = waterRequest.load(request.args,unknown=INCLUDE)
        start = dates.get('start')
        end = dates.get('end')
        connection = CreateConnection()
        with connection.cursor() as cursor:
            cursor.execute('select waterdate,dishwasher,clotheswasher,shower,bath from water_usage where waterdate>=%s',
                           (start,))
            holderEnd = []
            resultsStart = cursor.fetchall()
            if start[1] != end[1]:
                cursor.execute('select waterdate,dishwasher,clotheswasher,shower,bath from water_usage where waterdate <=%s',
                               (end,))
                resultsEnd = cursor.fetchall()

                for i in resultsEnd:
                    holderEnd.append((waterGet.load({'date':str(i[0]),'dishwasher':i[1],'clotheswasher':i[2],'shower':i[3],'bath':i[4]},unknown=INCLUDE)))
            holderStart = []
            for i in resultsStart:
                holderStart.append(waterGet.load({'date':str(i[0]),'dishwasher':i[1],'clotheswasher':i[2],'shower':i[3],'bath':i[4]},unknown=INCLUDE))
            print(holderStart)
            return {'start': holderStart, 'end':holderEnd}, 200