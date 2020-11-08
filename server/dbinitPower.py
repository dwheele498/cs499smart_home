import psycopg2
import calendar
from datetime import datetime, timedelta
import random
import dbinit as db
from marshmallow import Schema, fields, INCLUDE

connection = db.CreateConnection()
cursor = connection.cursor()
cursor.execute('select selecteddate from weather')
datetable = cursor.fetchall()

cursor.execute('select clotheswasher from water_usage')
clothestable = cursor.fetchall()
# print(clothestable)

cursor.execute('select dishwasher from water_usage')
dishtable = cursor.fetchall()
# print(dishtable)


# used 4 times a week
washer = ((500 * 0.75) / 1000) * 0.12
dryer_formula_wd = ((3000 * .5) / 1000) * 0.12

# used everyday
bathexhaust = ((4500 * .067) / 1000) * 0.12
hvac = ((3500 * 24) / 1000) * 0.12
refrigerator = ((150 * 24) / 1000) * 0.12

clotheswasher_formula_wd = ((500 * .5) / 1000) * 0.12
tvformula_wd = (((636 * 4) / 1000) * 0.12)
bedtv_formula_wd = (((100 * 2) / 1000) * 0.12)
microwave_formula_wd = (((1100 * 0.33) / 1000) * 0.1)
oven_formula_wd = (((4000 * 0.75) / 1000) * 0.12)
dishwasher_formula_wd = (((1800 * 0.75) / 1000) * 0.12)
stove_formula_wd = (((3500 * 0.33) / 1000) * 0.12)


def rand():
    x = random.randint(0, 1)
    if x == 1:
        return 1
    else:
        return 0


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
    light = fields.Float()
    bathexhaust = fields.Float()


def ClearPower():
    with connection.cursor() as cursor:
        cursor.execute('Drop Table power')
        connection.commit()
        cursor.execute('create table power(id serial PRIMARY KEY, powerdate date, livingtv float, bedtv float, '
                       'oven float, microwave float, stove float, dishwasher float, clotheswasher float, dryer float, lights float, hvac float, exhaust float, total float)')
        connection.commit()


def GeneratePowerDBData():
    powerschema = PowerSchema()
    with connection.cursor() as cursor:
        insert_db = 'INSERT INTO power(powerdate,livingtv,bedtv,oven,microwave,stove,' \
                    'dishwasher,clotheswasher,dryer,lights,hvac,exhaust,total) VALUES (%(powerdate)s,' \
                    ' %(livingtv)s, %(bedtv)s, %(oven)s, %(microwave)s, %(stove)s,' \
                    ' %(dishwasher)s,%(clotheswasher)s,%(dryer)s,%(light)s,%(hvac)s,%(exhaust)s,%(total)s)'
        x=0
        y = 0
        for i in datetable:
            date = i[0]
            day = calendar.day_name[date.weekday()]
            if day == 'Monday' or 'tuesday' or 'Wednesday' or 'Thursday' or 'Friday':
                # Formula for cost of power: ((Watts x hours used)/1000 kwh) x 0.12
                liveTv = tvformula_wd * rand()
                bedTv = bedtv_formula_wd * rand()
                microwave = microwave_formula_wd * rand()
                oven = oven_formula_wd * rand()
                b = dishtable[y]
                if b[0] == 0:
                    v = 0
                    y+=1
                else:
                    v = 1
                    y+=1
                dishwasher = dishwasher_formula_wd * v
                # print(day, 'dishwash', dishwasher)
                stove = stove_formula_wd * rand()
                a = clothestable[x]
                if a[0] == 0:
                    j = 0
                    x+=1
                else:
                    j = 1
                    x+=1
                clotheswasher = clotheswasher_formula_wd * j
                if(clotheswasher > 0):
                    dryer = dryer_formula_wd
                else:
                    dryer = 0
                # print(day, 'clotheswash', clotheswasher)
                light = ((60 * random.randint(1, 10)/1000)*.12)

                total = liveTv + bedTv + oven + microwave + dishwasher + stove + clotheswasher + light + dryer
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
                b = dishtable[y]
                if b[0] == 0:
                    v = 0
                    y += 1
                else:
                    v = 1
                    y += 1
                dishwasher = (((1800 * 0.75) / 1000) * 0.12) * v
                # print(day, 'dishwash', dishwasher)
                stove = (((3500 * 0.5) / 1000) * 0.12) * rand()
                a = clothestable[x]
                if a[0] == 0:
                    j = 0
                    x+=1
                else:
                    j = 1
                    x+=1
                clotheswasher = (((500 * .5) / 1000) * 0.12) * j
                if(clotheswasher>0):
                    dryer = ((3000 * .5) / 1000) * 0.12
                else:
                    dryer = 0
                print(day, 'clotheswash', clotheswasher)

                light = ((60*random.randint(1, 17)/100)*.12)
                total = liveTv + bedTv + oven + microwave + dishwasher + stove + clotheswasher + light + dryer
                # print(day, 'total weekend', total)
            date = date.strftime("%Y-%m-%d")
            update_usage = powerschema.load({"powerdate": date, "livingtv": liveTv,
                                             "bedtv": bedTv, "oven": oven, "stove": stove, "microwave": microwave,
                                             "clotheswasher": clotheswasher, "dishwasher": dishwasher,
                                             "dryer": dryer, "hvac": hvac, "exhaust": bathexhaust, "light": light,
                                             'total': total},
                                            unknown=INCLUDE)
            # print(update_usage.get('powerdate'))

            cursor.execute(insert_db, update_usage)
            connection.commit()
            # print("updated table")


GeneratePowerDBData()
#ClearPower()
