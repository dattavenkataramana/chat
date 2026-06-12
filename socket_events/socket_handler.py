from flask_socketio import emit

from extensions import socketio
from extensions import db

from models.message_model import Message

online_users = set()


@socketio.on("connect")
def handle_connect():
    print("User connected")


@socketio.on("disconnect")
def handle_disconnect():
    print("User disconnected")


@socketio.on("join")
def handle_join(data):

    user_id = data.get("user_id")

    online_users.add(user_id)

    emit(
        "online_users",
        list(online_users),
        broadcast=True
    )


@socketio.on("send_message")
def handle_send_message(data):

    sender_id = data.get("sender_id")
    receiver_id = data.get("receiver_id")
    message = data.get("message")

    new_message = Message(
        sender_id=sender_id,
        receiver_id=receiver_id,
        message=message
    )

    db.session.add(new_message)
    db.session.commit()

    emit(
        "receive_message",
        new_message.to_dict(),
        broadcast=True
    )


@socketio.on("typing")
def handle_typing(data):

    emit(
        "user_typing",
        data,
        broadcast=True,
        include_self=False
    )