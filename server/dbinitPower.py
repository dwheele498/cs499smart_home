import psycopg2
import calendar
from datetime import datetime
import random
from .dbinit import CreateConnection
from marshmallow import Schema, fields

connection = CreateConnection()

# used 4 times a week
washer = ((500 * 0.75) / 1000) * 0.12
dryer = ((3000 * .5) / 1000) * 0.12

# used everyday
bathexhaust = ((4500 * .067) / 1000) * 0.12
hvac = ((3500 * 24) / 1000) * 0.12
refrigerator = ((150 * 24) / 1000) * 0.12


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


def ClearPower():
    with connection.cursor() as cursor:
        cursor.execute('Drop Table power')
        connection.commit()
        cursor.execute('create table power(id serial PRIMARY KEY, powerdate date, livingtv int, bedtv int, '
                       'oven int, microwave int, stove int, dishwasher int, clotheswasher int, dryer int, lights int, hvac int, exhaust int)')
        connection.commit()

def GeneratePowerDBDate():
    powerschema = PowerSchema()
    with connection.cursor() as cursor:
        insert_db = 'INSERT INTO power(powerdate,livingtv,bedtv,oven,microwave,stove,' \
                    'dishwasher,clotheswasher,dryer,light,hvac,exhaust) ' \
                    'VALUES (%s, %s, $s, %s, %s, %s, %s,%s,%s,%s,%s)'
        # update_db = 'UPDATE power set id = %s, day = %s, month = %s, year = %s, livingroomTv = %s, bedroomTv = %s, Oven = %s, Microwave = %s WHERE id = %s'
        for i in range(90):
            date = datetime.now().replace(day=i)
            day = calendar.day_name[date.weekday()]
            if day == 'Monday' or 'tuesday' or 'Wednesday' or 'Thursday' or 'Friday':
                # Formula for cost: ((Watts x hours used)/1000 kwh) x 0.12
                liveTv = (((636 * 4) / 1000) * 0.12) * rand()
                print(day, 'livetv',liveTv)
                bedTv = (((100 * 2) / 1000) * 0.12) * rand()
                print(day,'bedtv' , bedTv)
                microwave = (((1100 * 0.33) / 1000) * 0.1) * rand()
                print(day, 'microwave', microwave)
                oven = (((4000 * 0.75) / 1000) * 0.12) * rand()
                print(day, 'oven', oven)
                total = liveTv + bedTv + oven + microwave
                print(day,'total' ,total)
            elif day == 'Saturday' or 'Sunday':
                liveTv = (((636 * 8) / 1000) * 0.12) * rand()
                print(day, 'livetv weekend', liveTv)
                bedTv = (((100 * 4) / 1000) * 0.12) * rand()
                print(day, 'bedtv weekend', bedTv)
                microwave = (((1100 * 0.5) / 1000) * 0.12) * rand()
                print(day, 'microwave weekend', microwave)
                oven = (((4000 * 1) / 1000) * 0.12) * rand()
                print(day, 'oven weekend', oven)
                total = liveTv + bedTv + oven + microwave
                print(day, 'total weekend', total)
            update_usage = powerschema.load({"date":date, "livingtv":liveTv,"bedtv":bedTv,"oven":oven,"microwave":microwave,"clotheswasher":washer,"dryer":dryer, "hvac":hvac})
            # cursor = connection.cursor()
            cursor.execute(insert_db, update_usage)
            connection.commit()
            print("updated table")

#GeneratePowerDBDate()
#ClearPower()
