from flask_restful import Resource
from marshmallow import Schema, fields, INCLUDE
from flask import request
from datetime import datetime
import psycopg2
import json
from dbGen.dbinitWeather import CreateConnection
from dbGen.dbinitPower import Prediction, GenerateScreenStats

class PowerSchema(Schema):
    powerdate = fields.String()
    livingtv = fields.Int()
    bedtv = fields.Int()
    oven = fields.Int()
    microwave = fields.Int()
    stove = fields.Int()
    dishwasher = fields.Int()
    clotheswasher = fields.Int()
    dryer = fields.Int()
    hvac = fields.Int()
    bathexhaust = fields.Int()

class PowerRequestSchema(Schema):
    start: fields.Date()
    end: fields.Date()


powerget = PowerSchema()

powerrequest = PowerRequestSchema()


class PowerGetMonthly(Resource):
    def get(self):
        dates = powerrequest.load(request.args,unknown=INCLUDE)
        start = dates.get('start')
        end = dates.get('end').split('-')
        connection = CreateConnection()
        with connection.cursor() as cursor:
            cursor.execute('select powerdate,livingtv,bedtv,oven,microwave,stove,dishwasher,clotheswasher,hvac,exhaust from power where powerdate>=%s and powerdate<=%s',
                           (start,datetime.today()))
            # holderEnd = []
            resultsStart = cursor.fetchall()
            # if start[1] != end[1]:
            #     cursor.execute('select month,day,dishwasher,clotheswasher,shower,bath from water_usage where month=%s and day<=%s',
            #                    (end[1], end[2]))
            #     resultsEnd = cursor.fetchall()

                # for i in resultsEnd:
                #     holderEnd.append((waterGet.load({'month':i[0],'day':i[1],'dishwasher':i[2],'clotheswasher':i[3],'shower':i[4],'bath':i[5]},unknown=INCLUDE)))
            holderStart = []
            for i in resultsStart:
                print(i)
                holderStart.append(powerget.load({'powerdate':str(i[0]),'livingtv':i[1],'bedtv':i[2],'oven':i[3],'microwave':i[4],
                                                  'stove':i[5],'dishwasher':i[6],'clotheswasher':i[7],'hvac':i[8],'exhaust':i[9]},unknown=INCLUDE))
            print(holderStart)
            return {'start': holderStart}, 200

    def post(self):
        data = powerget.load(request.args, unknown=INCLUDE)
        connection = CreateConnection()
        with connection.cursor() as cursor:
            date = data.get('powerdate')
            for item in ['livingtv', 'bedtv', 'oven', 'microwave', 'stove', 'dishwasger', 'clotheswasher', 'hvac', 'exhaust']:
                if data.get(item) is not None:
                    cursor.execute('update power set ' + str(item) + ' = ' + str(item) + ' + ' + str(data.get(item)) + ' where powerdate::date = %s', [date])
                    connection.commit()


class PowerPrediction(Resource):
    def get(self):
        data = Prediction()
        data = data.rename(columns={'ds': 'Dates', 'yhat': 'Total Power Usage'})
        data = data.astype({'Dates': 'str'})
        # data = data.to_json(orient='records')
        return (data.values.tolist()), 200

class ScreenStats(Resource):
    def get(self):
        data = GenerateScreenStats()
        print(data)
        return({'data':data}),200