from flask import Blueprint, render_template
from flask_socketio import SocketIO, emit
from flask_login import current_user, login_required, login_user, logout_user

from root.globals import db, socketio

button = Blueprint("button", __name__)


@button.route("/click")
@login_required
def beta_button():
    """:VVP:"""
    return render_template("button/button.html")

