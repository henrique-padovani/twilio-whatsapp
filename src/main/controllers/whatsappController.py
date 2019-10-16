from flask import jsonify, request
from flask_restful import Resource
from src.main.db.MessageDB import MessageDB

class WhatsApp(Resource):
    def post(self):
        message = request.form.to_dict()
        print(message['Body'])
        MessageDB.saveMessage(str(message))
        return jsonify("Rodou...")

