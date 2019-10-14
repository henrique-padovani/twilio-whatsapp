from flask import Flask, jsonify, request
from flask_restful import Resource, Api

from src.app import getApp
from src.main.controllers.whatsappController import WhatsApp
from src.main.entities.ChatBot import getChatBot
from src.main.db.pgAdmin import MenagerDB
from src.main.db.MessageDB import MessageDB


print("GLOBAL")

def setUp():
    print("\n\n\n INICIO")

    # chatbot = getChatBot('Teste')
    menagerDB = MenagerDB('twiliodatabase')

    messageDB = MessageDB(menagerDB)
    MessageDB.createTable(MessageDB, menagerDB)
    MessageDB.saveMessage("mensagem skmsakm")

    print("\n\n\n FIM\n\n")
    return




if __name__ == '__main__':
    print("\n\n\nmain inicio \n\n")
    setUp()
    app = getApp()

    app.run(debug=True, use_reloader=False)
    print("\n\n\nmain fim \n\n")
