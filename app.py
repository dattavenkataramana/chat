from flask import Flask
from flask_cors import CORS

from config import Config
from extensions import db, socketio

from routes.auth_routes import auth_bp
from routes.chat_routes import chat_bp

from socket_events.socket_handler import *

app = Flask(__name__)

app.config.from_object(Config)

CORS(app)

db.init_app(app)

socketio.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(chat_bp)


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    socketio.run(
        app,
        host="0.0.0.0",
        port=5000,
        debug=True
    )