from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from HelloApiHandler import HelloApiHandler
from flask_pymongo import PyMongo

app = Flask(__name__, static_url_path='', static_folder='../frontend/public')
CORS(app) #comment this on deployment
api = Api(app)
mongodb_client = PyMongo(app, uri="mongodb+srv://when4meet:when4meet@cluster0.qyubt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongodb_client.db

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(HelloApiHandler, '/flask/hello')