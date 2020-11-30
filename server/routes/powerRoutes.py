from flask_restful import Resource
from marshmallow import Schema, fields, INCLUDE
from flask import request
from datetime import datetime,date
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
            holderStart = []
            for i in resultsStart:
                print(i)
                holderStart.append(powerget.load({'powerdate':str(i[0]),'livingtv':i[1],'bedtv':i[2],'oven':i[3],'microwave':i[4],
                                                  'stove':i[5],'dishwasher':i[6],'clotheswasher':i[7],'hvac':i[8],'exhaust':i[9]},unknown=INCLUDE))
            print(holderStart)
            return {'start': holderStart}, 200

    def post(self):
        data = request.json
        print('data')
        data = data['power']
        print(data)
        connection = CreateConnection()
        with connection.cursor() as cursor:
            powdate = date.today()
            for item in data:
                print(item)
                if item is not None:
                    cursor.execute('update power set ' + item[0] + ' =  %s '  + 'where powerdate = %s' ,(item[1],powdate))
                    connection.commit()
        return({'message':'successfully updated'},200)


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