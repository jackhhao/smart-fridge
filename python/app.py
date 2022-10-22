from flask import Flask

from database.db import DB
from utils import config
# from database.models import *

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = config["MONGO_URI"]
    app.config["MONGODB_SETTINGS"] = {
        "host": config["MONGO_URI"]
    }

    DB.init_client(app)
    DB.init_engine(app)
    register_blueprints(app)
    return app

def register_blueprints(app):
    from api import bp as main_bp
    app.register_blueprint(main_bp)

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
