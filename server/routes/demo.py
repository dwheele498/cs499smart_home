# This file can be deleted
# Just an example for now
# Use blueprints to register routes
from flask import Blueprint, json, request

demo_blueprint = Blueprint('demo_blueprint', __name__)

@demo_blueprint.route('', methods=['GET'])
def demo():
    return json.jsonify({
        'message': 'Hello from demo blueprint'
    })

@demo_blueprint.route('/echo', methods=['POST'])
def echo():
    return json.jsonify(request.json)