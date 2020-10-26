from flask_restful import Resource
from marshmallow import Schema, fields, INCLUDE
from flask import request
from datetime import datetime
import psycopg2
from dbGen.weatherDbGen import CreateConnection


class WaterGetSchema(Schema):
    month: fields.Str()
    day: fields.Str()
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
        start = dates.get('start').split('-')
        end = dates.get('end').split('-')
        connection = CreateConnection()
        with connection.cursor() as cursor:
            cursor.execute('select month,day,dishwasher,clotheswasher,shower,bath from water_usage where month=%s',
                           (start[1],))
            holderEnd = []
            resultsStart = cursor.fetchall()
            if start[1] != end[1]:
                cursor.execute('select month,day,dishwasher,clotheswasher,shower,bath from water_usage where month=%s and day<=%s',
                               (end[1], end[2]))
                resultsEnd = cursor.fetchall()

                for i in resultsEnd:
                    holderEnd.append((waterGet.load({'month':i[0],'day':i[1],'dishwasher':i[2],'clotheswasher':i[3],'shower':i[4],'bath':i[5]},unknown=INCLUDE)))
            holderStart = []
            for i in resultsStart:
                holderStart.append(waterGet.load({'month':i[0],'day':i[1],'dishwasher':i[2],'clotheswasher':i[3],'shower':i[4],'bath':i[5]},unknown=INCLUDE))
            print(holderStart)
            return {'start': holderStart, 'end':holderEnd}, 200