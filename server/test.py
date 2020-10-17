from flask_restful import Resource
from marshmallow import Schema,fields
from flask import request

class PostSchema(Schema):
    oToTwenty = fields.Int()
    aMessage = fields.Str()

post_schema = PostSchema()

class TestRequest(Resource):
    @classmethod
    def get(cls):
        return{"message":"Test response"},200


class PostTest(Resource):
    @classmethod
    def post(cls):
        data = post_schema.load(request.get_json())
        return {"message":data},200
