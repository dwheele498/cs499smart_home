from datetime import time
import homedashboard.server.dbinit as db
import homedashboard.smarthome.src.cost as c
import timeit
import threading




# door is closed
door = True


def gettavg():
    return db.GenerateWeatherDbData.WeatherSchema.tavg


def getdate():
    return db.GenerateWeatherDbData.WeatherSchema.date






