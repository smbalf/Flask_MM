from flask import Blueprint, render_template, request, session
from flask_socketio import emit
from flask_login import current_user, login_required

from root.users.models import User
from root.globals import socketio

button = Blueprint("button", __name__)

def msg_callback():
    """For use with emit"""
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
    user_sid = data["user_id"]
    user = User.objects(id=user_id).first()
    user.gold = user_gold
    session[user_sid] = user
    user.save()
    """if request.namespace != "/update_gold":
        user.save()
        print("SAVING DATA DUE TO DIFFERENT PATH")"""

@socketio.on('disconnect')
@login_required
def save_on_dc():
    user_sid = str(current_user.id)
    try:
        if user_sid in session['_user_id']:
            user = session[user_sid]
            user.save()
            print("SAVING DUE TO LOGOUT")
        else:
            print("FAILED TO SAVE ON DC")
            print(current_user.id)
    except KeyError:
        print("KeyError - user session not saved yet")