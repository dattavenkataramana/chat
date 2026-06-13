from flask import Flask
from flask_cors import CORS

from config import Config
from extensions import db, socketio

from routes.auth_routes import auth_bp
from routes.chat_routes import chat_bp

from models.user_model import User

from socket_events.socket_handler import *

app = Flask(__name__)

app.config.from_object(Config)

CORS(app)

db.init_app(app)

socketio.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(chat_bp)


@app.route("/")
def home():
    return {
        "status": "success",
        "message": "Chat Backend Running"
    }


with app.app_context():

    db.create_all()

    # Create default users if they don't exist
    if not User.query.filter_by(username="ram").first():
        db.session.add(
            User(
                username="ram",
                password="123456"
            )
        )

    if not User.query.filter_by(username="priya").first():
        db.session.add(
            User(
                username="priya",
                password="123456"
            )
        )

    db.session.commit()


if __name__ == "__main__":
    socketio.run(
        app,
        host="0.0.0.0",
        port=5000,
        debug=True
    )