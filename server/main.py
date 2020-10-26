# from dotenv import load_dotenv
from flask import Flask, json, request
from flask_restful import Api
from os import getenv
from test import TestRequest, PostTest, WeatherDataMonthly
from flask_cors import CORS

# load_dotenv()
app = Flask(__name__)
api = Api(app)
CORS(app)

    
# So that this file doesn't get out of hand,
# register routes in other modules.
# Here is an example

api.add_resource(TestRequest,"/test")
api.add_resource(PostTest,"/posttest")
api.add_resource(WeatherDataMonthly,"/monthlyweatherdata")

if __name__ == '__main__':
    app.run(
        # host=getenv('FLASK_HOST'), 
        # port=getenv('FLASK_PORT'),
        # debug=getenv('FLASK_DEBUG')
        port=5000,debug=True
    )