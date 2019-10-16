from flask import jsonify, request
from flask_restful import Resource
from src.main.db.MessageDB import MessageDB

class WhatsApp(Resource):
    def post(self):
        message = request.form.to_dict()
        print("request.form: " + str(request.form))
        MessageDB.saveMessage(str(message))
        return jsonify("Rodou...")

