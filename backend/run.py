import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})
db = SQLAlchemy(app)

@app.route("/api/health")
def health():
    return {"status": "ok", "message": "EventSync backend is running"}

@app.route("/api/db-check")
def db_check():
    try:
        with app.app_context():
            db.session.execute(db.text("SELECT 1"))
        return {"status": "ok", "message": "Database connection successful"}
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)