from flask import jsonify, request
from flask_restful import Resource
from src.main.db.MessageDB import MessageDB
from src.main.entities.ChatBot import ChatBot

from twilio.rest import Client

ACCOUNT_SID = 'ACc5382bd8ed2e7f906347594a71a8cd75'
AUTH_TOKEN = '909cfa79c4508fc7506e4c9c545f5a8a'
mybot_whats = 'whatsapp:+14155238886'

class WhatsApp(Resource):
    def post(self):
        message = request.form.to_dict()
        
        body = message['Body']
        to = message['From']
        
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        msg = ChatBot.getBotResponse(body)
        client.messages.create(body=msg, from_=mybot_whats, to=to)

        MessageDB.saveMessage(str(message))
        return jsonify("Rodou...") 

