import psycopg2
import calendar
from datetime import datetime, timedelta
import random
import homedashboard.server.dbinit as db

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


def GeneratePowerDBDate():
    insert_db = 'INSERT INTO power(id, day,month,year,livingroomTv,BedroomTv,Oven,Microwave) VALUE (%s, %s, $s, %s, %s, %s, %s)'
    update_db = 'UPDATE power set id = %s, day = %s, month = %s, year = %s, livingroomTv = %s, bedroomTv = %s, Oven = %s, Microwave = %s WHERE id = %s'
    for i in range(90):
        date = datetime.now() - timedelta(days=i)
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
        update_usage = (i, date.day, date.month, liveTv, bedTv, oven, microwave, total, i)
        connection = psycopg2.connect(
            database="Team3DB",
            user="Team3",
            password="3Team3",
            host='127.0.0.1',
            port='5432'
        )
        cursor = connection.cursor()
        cursor.execute(update_db, update_usage)
        connection.commit
        cursor.close()
        connection.close()
        print("updated table")


print(GeneratePowerDBDate())
