from flask import Blueprint, request, jsonify

from models.user_model import User

auth_bp = Blueprint(
    "auth_bp",
    __name__,
    url_prefix="/api/auth"
)


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(
        username=username,
        password=password
    ).first()

    if not user:
        return jsonify({
            "success": False,
            "message": "Invalid username or password"
        }), 401

    return jsonify({
        "success": True,
        "user": user.to_dict()
    })