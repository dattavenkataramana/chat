from app import app
from extensions import db

from models.user_model import User


with app.app_context():

    db.create_all()

    if not User.query.filter_by(
        username="ram"
    ).first():

        user1 = User(
            username="ram",
            password="123456"
        )

        db.session.add(user1)

    if not User.query.filter_by(
        username="priya"
    ).first():

        user2 = User(
            username="priya",
            password="123456"
        )

        db.session.add(user2)

    db.session.commit()

    print("Users Created")