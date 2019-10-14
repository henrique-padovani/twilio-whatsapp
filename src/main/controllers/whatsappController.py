from flask import jsonify, request
from flask_restful import Resource
from src.main.db.MessageDB import MessageDB

class WhatsApp(Resource):
    def post(self):
        message = request.json
        MessageDB.saveMessage(message)
        return jsonify(request.json)

