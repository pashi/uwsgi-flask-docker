# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)
CORS(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    def post(self):
        name = "world"
        try:
          d = request.get_json(force=True)
          name = d['name']
        except:
          pass
        return {'hello': name}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)

