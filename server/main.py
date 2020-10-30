from flask import Flask, json, request
from flask_restful import Api
from os import getenv
from routes.weatherRoutes import WeatherDataMonthly
from routes.waterRoutes import WaterGetMonthly
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(WeatherDataMonthly,"/monthlyweatherdata")
api.add_resource(WaterGetMonthly,"/monthlywaterdata")

if __name__ == '__main__':
    app.run(
        port=5000,debug=True
    )