"""
Core views
"""
from flask import Blueprint, render_template
from flask_socketio import SocketIO, emit

from root.globals import db, socketio

core = Blueprint("core", __name__)


# LANDING PAGE
@core.route("/")
def index():
    return render_template("core/index.html")

@socketio.on('my event')
def handle_my_event(msg):
    print("Event received: " + str(msg))
    data = db.connection
    for x in data:
        emit('my response', x, broadcast=True)

@socketio.on('connect')
def handle_connect():
    print("Client Connected")