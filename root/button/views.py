from flask import Blueprint, render_template
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
    return render_template("button/button.html", user_id = str(current_user.id))

@socketio.on("update_gold")
def update_gold(data):
    user_id = data["user_id"]
    user = User.objects(id=user_id).first()
    user.gold += 1
    user.save()
    emit("update_gold_response", {"gold": user.gold}) # removed callback=msg_callback as worked fine..
    print(user.gold)


