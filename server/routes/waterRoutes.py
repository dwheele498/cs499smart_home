from flask_restful import Resource
from marshmallow import Schema, fields, INCLUDE
from flask import request
from datetime import datetime,date
import psycopg2
from dbGen.dbinitWeather import CreateConnection
from dbGen.dbinitWater import Prediction


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
    def get(self):
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

    def post(self):
        # data = waterGet.load(request.args, unknown=INCLUDE)
        data = request.json
        data = data['water']
        print(data)
        connection = CreateConnection()
        with connection.cursor() as cursor:
            wadate = date.today()
            for item in data:
                if item is not None:
                    cursor.execute('update water_usage set ' + item[0] + ' = ' + item[0] + ' + %s  where waterdate = %s', (item[1],wadate))
                    connection.commit()
        return({'message':'ok'},200)


class WaterPrediction(Resource):
    def get(self):
        data = Prediction()
        data = data.rename(columns={'ds':'Dates','yhat':'Estimate Total Water'})
        data = data.astype({'Dates':'str'})
        # data = data.to_json(orient='records')
        return(data.values.tolist()),200