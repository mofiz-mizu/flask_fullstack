from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    user = User(
        name=data["name"],
        email=data["email"],
        password_hash=generate_password_hash(data["password"]),
        role=data.get("role", "user")
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(success=True)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if not user or not check_password_hash(user.password_hash, data["password"]):
        return jsonify(error="Invalid credentials"), 401
    token = create_access_token(identity={"id": user.id, "role": user.role})
    return jsonify(access_token=token)
