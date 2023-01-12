"""
Global variables and objects to import into other modules.

Kept separate from the factory to avoid infinite import loops 
when importing these global objects into multiple modules.
"""
from flask_login import LoginManager
from flask_mongoengine import MongoEngine

# Database setup
db = MongoEngine()

# Login manager setup
login_manager = LoginManager()