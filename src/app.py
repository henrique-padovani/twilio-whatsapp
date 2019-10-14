from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from src.main.controllers.whatsappController import WhatsApp
from src.main.controllers.noroute import NoRoute

def getApp():
    print("getApp + name:" + str(__name__))
    app = Flask("__main__")
    app.url_map.strict_slashes = False
    api = Api(app)
    
    api.add_resource(WhatsApp, '/whatsApp')
    api.add_resource(NoRoute, '/')
    # app.run(debug=True)
    print("get app FIM")
    return app
