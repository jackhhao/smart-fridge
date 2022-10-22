from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
from utils import config

class DB(object):
    @staticmethod
    def init_client(app):
        DB.client_db = PyMongo(app).db

    @staticmethod
    def init_engine(app):
        DB.engine_db = MongoEngine()
        DB.engine_db.init_app(app)