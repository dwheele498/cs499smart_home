from dotenv import load_dotenv
from flask import Flask, json, request
from os import getenv

from routes.demo import demo_blueprint

load_dotenv()
app = Flask(__name__)

@app.route('/', methods=['GET']) # GET is default, but specify anyway to be clear
def status():
    return json.jsonify({
        'message': 'Server is running at {}'.format(request.host_url)
    })
    
# So that this file doesn't get out of hand,
# register routes in other modules.
# Here is an example

app.register_blueprint(demo_blueprint, url_prefix='/demo')

if __name__ == '__main__':
    app.run(
        host=getenv('FLASK_HOST'), 
        port=getenv('FLASK_PORT'),
        debug=getenv('FLASK_DEBUG')
    )