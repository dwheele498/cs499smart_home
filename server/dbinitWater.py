import psycopg2
import calendar
from datetime import datetime, timedelta
import random
from dbinit import CreateConnection
import pandas as pd
from fbprophet import Prophet


def ClearTable():
    connection = CreateConnection()
    with connection.cursor() as cursor:
        cursor.execute('Drop Table water_usage')
        connection.commit()
        cursor.execute('create table water_usage(id serial PRIMARY KEY, waterdate date, '
                       'clotheswasher float, shower float, bath float, dishwasher float)')
        connection.commit()

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
    connection = CreateConnection()
    #print("i\tdate\tmonth\tyear\tclothes\tshower\tbathe\tdish")
    #generates last 90 days
    postgres_insert_query = """ INSERT INTO water_usage (waterdate, clotheswasher, shower, bath, dishwasher) 
    VALUES (%s, %s, %s, %s, %s) """
    # postgres_update_query = """ UPDATE water_usage set id = %s, day = %s, month = %s, year = %s, clotheswasher = %s, shower = %s, bath = %s, dishwasher = %s WHERE id = %s """
    print("updating 90 rows from water_usage...")
    daterange = pd.date_range(end=datetime.today(), start=datetime.today().replace(month=datetime.today().month-2))
    for i in daterange:
        #datetimeobject
        # my_date = datetime.now() - timedelta(days = i)
        my_date = i
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
        record_to_update = (my_date,dailyClothesWasher,dailyShower,dailyBath,dailyDishWasher)
        with connection.cursor() as cursor:
            cursor.execute(postgres_insert_query, record_to_update)
            connection.commit()
        cursor.close()
    connection.close()
    print("update complete")

def Prediction():
    connection = CreateConnection()
    with connection.cursor() as cursor:
        cursor.execute("Select selectedDate,tavg from weather where selectedDate >= %s and selectedDate <= %s",('2020-01-01',date.today()))
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=["ds","y"])
        m = Prophet()
        m.fit(df)
        future = m.make_future_dataframe(periods=30,include_history=False)
        prediction = m.predict(future)
        return (prediction[['ds','yhat']])



GenerateWaterDbData()
#ClearTable()