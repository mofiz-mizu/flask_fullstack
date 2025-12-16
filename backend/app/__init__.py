from flask import Flask
from flask_jwt_extended import JWTManager
from .models import db
from .auth import auth_bp
from .crud import crud_bp
import os

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    db.init_app(app)
    JWTManager(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(crud_bp)

    @app.route("/")
    def home():
        return {"status": "API running"}

    with app.app_context():
        db.create_all()

    return app
