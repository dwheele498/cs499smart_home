from flask import Flask, json, request
from flask_restful import Api
from os import getenv
from routes.weatherRoutes import WeatherDataMonthly, GetWeatherPrediction
from routes.waterRoutes import WaterGetMonthly
from routes.powerRoutes import PowerGetMonthly
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/', methods=['GET']) # GET is default, but specify anyway to be clear
def status():
    return json.jsonify({
        'message': 'Server is running at {}'.format(request.host_url)
    })
    
# So that this file doesn't get out of hand,
# register routes in other modules.
# Here is an example

api.add_resource(WeatherDataMonthly,"/monthlyweatherdata")
api.add_resource(WaterGetMonthly,"/monthlywaterdata")
api.add_resource(PowerGetMonthly,"/monthlypowerdata")
api.add_resource(GetWeatherPrediction,'/monthlyweatherprediction')

if __name__ == '__main__':
    app.run(
        port=5000,debug=True
    )