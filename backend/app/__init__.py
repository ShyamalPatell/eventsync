import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from app.extensions import db

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})
    db.init_app(app)

    from app.routes.health import health_bp
    app.register_blueprint(health_bp, url_prefix="/api")

    return app