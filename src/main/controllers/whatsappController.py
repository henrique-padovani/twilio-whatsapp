from flask import jsonify, request
from flask_restful import Resource
from src.main.db.MessageDB import MessageDB
from src.main.entities.ChatBot import Bot
from os import environ
from twilio.rest import Client

ACCOUNT_SID = environ.get('ACCOUNT_SID')
AUTH_TOKEN = environ.get('AUTH_TOKEN')

mybot_whats = 'whatsapp:+14155238886'

class WhatsApp(Resource):
    def post(self):
        message = request.form.to_dict()
        
        body = message['Body']
        to = message['From']
        
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        msg = Bot.getBotResponse(body)
        client.messages.create(body=msg, from_=mybot_whats, to=to)

        MessageDB.saveMessage(str(message))
        return jsonify("Rodou...")

