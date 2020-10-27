import psycopg2
import calendar
from datetime import datetime, timedelta
import random


def GenerateWaterDbData():
    """
    Clears water_usage table and inserts pseudo-random values for the previous 90 days.
    req.
    from datetime import datetime, timedelta
    import calendar
    from random import random
    ref.
    https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/
    """
    def randomWaterTrigger():
        #4/7 is .571... So if a dishwasher runs 4 times a week it
        #has a 57% chance of being run any day. Right?
        #That's what I'm going for here.
        roll = random.randint(1, 100)
        if roll < 58:
            return int(1)
        else:
            return int(0)
    #rate is galons used per cycle
    #ratio is percentage of hotwater percyle, 1 = 100%
    #durration is how long a cycle takes in minutes
    class waterFixture:
        def __init__(self, rate, ratio, duration):
            self.rate = rate
            self.ratio = ratio
            self.duration = duration

    clothesW = waterFixture(20, .85, 30)
    shower = waterFixture(25, .65, 20)
    bath = waterFixture(30, .65, 30)
    dish = waterFixture(6, 1, 45)
    i = 0
    #print("i\tdate\tmonth\tyear\tclothes\tshower\tbathe\tdish")
    #generates last 90 days
    postgres_insert_query = """ INSERT INTO water_usage (id, day, month, year, clotheswasher, shower, bath, dishwasher) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
    postgres_update_query = """ UPDATE water_usage set id = %s, day = %s, month = %s, year = %s, clotheswasher = %s, shower = %s, bath = %s, dishwasher = %s WHERE id = %s """
    print("updating 90 rows from water_usage...")
    for i in range(90):
        #datetimeobject
        my_date = datetime.now() - timedelta(days = i)
        my_weekday = calendar.day_name[my_date.weekday()]
        if ("Monday" == my_weekday or "Tuesday" == my_weekday or "Wednesday" == my_weekday or "Thursday" == my_weekday or "Friday" == my_weekday):
            dailyClothesWasher = (clothesW.rate * randomWaterTrigger())
            dailyShower = (shower.rate * 2)
            dailyBath = (bath.rate * 2)
            dailyDishWasher = (dish.rate * randomWaterTrigger())
        elif ("Sunday" == my_weekday or "Saturday" == my_weekday):
            dailyClothesWasher = (clothesW.rate * randomWaterTrigger())
            dailyShower = (shower.rate * 3)
            dailyBath = (bath.rate * 3)
            dailyDishWasher = (dish.rate * randomWaterTrigger())
        #send to db(index(year,month,day))
        #record_to_insert = (i, my_date.day,my_date.month,my_date.year,dailyClothesWasher,dailyShower,dailyBath,dailyDishWasher)
        record_to_update = (i, my_date.day,my_date.month,my_date.year,dailyClothesWasher,dailyShower,dailyBath,dailyDishWasher, i)
        connection = psycopg2.connect(
            database="Team3DB",
            user="Team3",
            password="3Team3",
            host='127.0.0.1',
            port='5432'
        )
        cursor = connection.cursor()
        #cursor.execute(postgres_insert_query, record_to_insert)
        cursor.execute(postgres_update_query, record_to_update) 
        #print(i,"\t",my_date.day,"\t",my_date.month,"\t",my_date.year,"\t",dailyClothesWasher,"\t",dailyShower,"\t",dailyBath,"\t",dailyDishWasher)
        connection.commit()
        cursor.close()
        connection.close()
    print("update complete")