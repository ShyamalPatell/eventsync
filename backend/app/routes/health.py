from flask import Blueprint
from app.extensions import db

health_bp = Blueprint("health", __name__)

@health_bp.route("/health")
def health():
    return {"status": "ok", "message": "EventSync backend is running"}

@health_bp.route("/db-check")
def db_check():
    try:
        db.session.execute(db.text("SELECT 1"))
        return {"status": "ok", "message": "Database connection successful"}
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500