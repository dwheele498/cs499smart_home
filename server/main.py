from dotenv import load_dotenv
from flask import Flask, json, request
from os import getenv

load_dotenv()
app = Flask(__name__)

@app.route('/', methods=['GET']) # GET is default, but specify anyway to be clear
def status():
    return json.jsonify({
        'message': 'Server is running at {}'.format(request.host_url)
    })

if __name__ == '__main__':
    app.run(
        host=getenv('FLASK_HOST'), 
        port=getenv('FLASK_PORT'),
        debug=getenv('FLASK_DEBUG')
    )