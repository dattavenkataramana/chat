from datetime import datetime

from extensions import db


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    sender_id = db.Column(
        db.Integer,
        nullable=False
    )

    receiver_id = db.Column(
        db.Integer,
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    is_seen = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "message": self.message,
            "is_seen": self.is_seen,
            "created_at": self.created_at.strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }