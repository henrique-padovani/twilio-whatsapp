from flask import jsonify, request
from flask_restful import Resource

class NoRoute(Resource):
    def get(self):
        message = request.json
        return jsonify({'ola':'olaaa'})

