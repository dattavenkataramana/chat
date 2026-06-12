from flask import Blueprint, request, jsonify

from extensions import db
from models.message_model import Message

chat_bp = Blueprint(
    "chat_bp",
    __name__,
    url_prefix="/api/chat"
) 


@chat_bp.route("/send-message", methods=["POST"])
def send_message():

    data = request.get_json()

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

    return jsonify({
        "success": True,
        "message": "Message sent"
    }) 



@chat_bp.route("/messages", methods=["GET"])
def get_messages():

    sender_id = request.args.get("sender_id")
    receiver_id = request.args.get("receiver_id")

    messages = Message.query.filter(
        (
            (Message.sender_id == sender_id)
            &
            (Message.receiver_id == receiver_id)
        )
        |
        (
            (Message.sender_id == receiver_id)
            &
            (Message.receiver_id == sender_id)
        )
    ).order_by(
        Message.created_at.asc()
    ).all()

    return jsonify(
        [msg.to_dict() for msg in messages]
    )


@chat_bp.route("/clear-chat", methods=["DELETE"])
def clear_chat():

    Message.query.delete()

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Chat cleared"
    })