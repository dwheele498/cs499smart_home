# from dotenv import load_dotenv
from flask import Flask, json, request
from flask_restful import Api
from os import getenv
from test import TestRequest, PostTest, WeatherDataMonthly
from flask_cors import CORS

from routes.demo import demo_blueprint
# load_dotenv()
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

app.register_blueprint(demo_blueprint, url_prefix='/demo')
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