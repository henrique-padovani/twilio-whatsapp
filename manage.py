from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from os import environ

from src.app import getApp

from src.main.entities.ChatBot import Bot
from src.main.db.pgAdmin import MenagerDB
from src.main.db.MessageDB import MessageDB


print("GLOBAL")

def setUp():
    print("\n\n\n INICIO")

    Bot.getChatBot('Teste')
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

    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=environ.get('PORT'))
    print("\n\n\nmain fim \n\n")
