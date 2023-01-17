import os
from datetime import datetime

from bson import ObjectId, json_util
from flask import Flask
from flask.json import JSONEncoder
import socketio

from root.core.views import core
from root.globals import db, login_manager, socketio
from root.users.views import users
from root.button.views import button


class MongoJsonEncoder(JSONEncoder):
    """Adjustments to the Flask json encoder for MongoEngine support"""

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)


def create_app():
    #Create the flask application

    # Initiate app
    app = Flask(__name__)
    app.json_encoder = MongoJsonEncoder

    # Update app.config from environment variables
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["MONGODB_SETTINGS"] = [
        {
            "db": "playerData",
            "alias": "playerData",
            "authentication_source": "admin",
            "host": os.getenv("PLAYERDATA_HOST"),
            "port": int(os.getenv("MONGODB_PORT")),
            "username": os.getenv("MONGODB_USERNAME"),
            "password": os.getenv("MONGODB_PASSWORD"),
        },
        {
            "db": "randomData",
            "alias": "randomData",
            "authentication_source": "admin",
            "host": os.getenv("RANDOMDATA_HOST"),
            "port": int(os.getenv("MONGODB_PORT")),
            "username": os.getenv("MONGODB_USERNAME"),
            "password": os.getenv("MONGODB_PASSWORD"),
        }
    ]

    # register blueprints
    app.register_blueprint(core, url_prefix="")
    app.register_blueprint(users, url_prefix="/users")
    app.register_blueprint(button, url_prefix="/button")
    
    # initialise database with MongoDB settings
    db.init_app(app)
    
    """
    with app.app_context():
        print(f"Connected to database: {db.connection}")
    """

    # initialize login manager
    login_manager.init_app(app)
    login_manager.login_view = "users.login"

    socketio.init_app(app)

    return app

