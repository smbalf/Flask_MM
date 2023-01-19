from flask import Blueprint, render_template, request
from flask_socketio import emit
from flask_login import current_user, login_required

from root.users.models import User
from root.globals import socketio

button = Blueprint("button", __name__)

def msg_callback():
    print("MESSAGE RECEIVED BY CLIENT CONFIRMED!")


@button.route("/click")
@login_required
def beta_button():
    return render_template("button/button.html", 
                            user_id = str(current_user.id), 
                            user_gold = current_user.gold)

@socketio.on("update_gold")
def update_gold(data):
    user_id = data["user_id"]
    user_gold = data["user_gold"]
    user = User.objects(id=user_id).first()
    user.gold = user_gold
    if not request.path == "/click":
        user.save()
        print("SAVING DATA DUE TO DIFFERENT PATH")
        pass

@socketio.on('disconnect')
def save_on_dc():
    print("SAVING DUE TO LOGOUT")