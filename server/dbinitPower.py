import psycopg2
import calendar
from datetime import datetime, timedelta
import random
import homedashboard.server.dbinit as db
from marshmallow import Schema, fields, INCLUDE

connection = db.CreateConnection()
cursor = connection.cursor()
cursor.execute('select selecteddate from weather')
datetable = cursor.fetchall()


# used 4 times a week
washer = ((500 * 0.75) / 1000) * 0.12
dryer = ((3000 * .5) / 1000) * 0.12

# used everyday
bathexhaust = ((4500 * .067) / 1000) * 0.12
hvac = ((3500 * 24) / 1000) * 0.12
refrigerator = ((150 * 24) / 1000) * 0.12

stove = 0
dishwasher = 0
clotheswasher = 0
dryer = 0
light = 0



def rand():
    x = random.randint(0, 1)
    if x == 1:
        return 1
    else:
        return 0


def randwash():
    pass


class PowerSchema(Schema):
    powerdate = fields.Date()
    livingtv = fields.Float()
    bedtv = fields.Float()
    oven = fields.Float()
    microwave = fields.Float()
    stove = fields.Float()
    dishwasher = fields.Float()
    clotheswasher = fields.Float()
    dryer = fields.Float()
    hvac = fields.Float()
    bathexhaust = fields.Float()


def ClearPower():
    with connection.cursor() as cursor:
        cursor.execute('Drop Table power')
        connection.commit()
        cursor.execute('create table power(id serial PRIMARY KEY, powerdate date, livingtv float, bedtv float, '
                       'oven float, microwave float, stove float, dishwasher float, clotheswasher float, dryer float, lights float, hvac float, exhaust float)')
        connection.commit()


def GeneratePowerDBData():
    powerschema = PowerSchema()
    # with connection.cursor() as cursor:
    # insert_db = 'INSERT INTO power(powerdate,livingtv,bedtv,oven,microwave,stove,dishwasher,clotheswasher,dryer,light,hvac,exhaust) VALUES (%f, %f, $f, %f, %f, %f, %f,%f,%f,%f,%f)'
    update_db = 'UPDATE power set id = %s, day = %s livingTv = %s, bedTv = %s, oven = %s, microwave = %s, stove = %s, dishwasher = %s, clotheswasher = %s, dryer = %s, lights = %s, hvac = %s  WHERE id = %s'
    for i in datetable:
        date = i[0]
        day = calendar.day_name[date.weekday()]
        if day == 'Monday' or 'tuesday' or 'Wednesday' or 'Thursday' or 'Friday':
            # Formula for cost of power: ((Watts x hours used)/1000 kwh) x 0.12
            liveTv = (((636 * 4) / 1000) * 0.12) * rand()
            #print(day, 'livetv', liveTv)
            bedTv = (((100 * 2) / 1000) * 0.12) * rand()
            # print(day,'bedtv' , bedTv)
            microwave = (((1100 * 0.33) / 1000) * 0.1) * rand()
            # print(day, 'microwave', microwave)
            oven = (((4000 * 0.75) / 1000) * 0.12) * rand()
            # print(day, 'oven', oven)
            total = liveTv + bedTv + oven + microwave
            # print(day,'total' ,total)
        elif day == 'Saturday' or 'Sunday':
            liveTv = (((636 * 8) / 1000) * 0.12) * rand()
            # print(day, 'livetv weekend', liveTv)
            bedTv = (((100 * 4) / 1000) * 0.12) * rand()
            # print(day, 'bedtv weekend', bedTv)
            microwave = (((1100 * 0.5) / 1000) * 0.12) * rand()
            # print(day, 'microwave weekend', microwave)
            oven = (((4000 * 1) / 1000) * 0.12) * rand()
            # print(day, 'oven weekend', oven)
            total = liveTv + bedTv + oven + microwave
            # print(day, 'total weekend', total)
        date = date.strftime("%Y-%m-%d")
        #update_usage = 'UPDATE power set id = %s, day = %s livingTv = %s, bedTv = %s, oven = %s, microwave = %s, stove = %s, dishwasher = %s, clotheswasher = %s, dryer = %s, lights = %s, hvac = %s  WHERE id = %s'
        #update_usage = (i, date, liveTv, bedTv, oven, microwave, stove, dishwasher, clotheswasher, dryer, light, hvac, bathexhaust, i)
        update_usage = powerschema.load({"powerdate": date, "livingtv": liveTv,
                                         "bedtv": bedTv, "oven": oven, "microwave": microwave, "clotheswasher": washer,
                                         "dryer": dryer, "hvac": hvac}, unknown=INCLUDE)
        # print(update_usage.get('powerdate'))
        cursor.execute(update_db, update_usage)
        connection.commit()
        # print("updated table")


GeneratePowerDBData()
# ClearPower()
