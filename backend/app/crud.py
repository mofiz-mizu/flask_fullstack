from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, Item

crud_bp = Blueprint("crud", __name__, url_prefix="/api/items")

@crud_bp.route("", methods=["POST"])
@jwt_required()
def create_item():
    user = get_jwt_identity()
    data = request.json
    item = Item(name=data["name"], description=data["description"], owner_id=user["id"])
    db.session.add(item)
    db.session.commit()
    return jsonify(success=True)

@crud_bp.route("", methods=["GET"])
@jwt_required()
def list_items():
    items = Item.query.all()
    return jsonify([{"id": i.id, "name": i.name, "description": i.description} for i in items])
