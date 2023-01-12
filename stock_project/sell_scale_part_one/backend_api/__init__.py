from flask import Flask

from .extensions import db

from flask_cors import CORS, cross_origin

''' This file serves as the package initializer for the flask project. 
    It creates the Flask application, sets CORS to be used for axios, 
    and sets the database configuration.
'''
def create_app():
    app = Flask(__name__)
    cors = CORS(app, resources={"/api/portfolio": {"origins": "http://localhost:3000"}})
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.stockdatabase'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app