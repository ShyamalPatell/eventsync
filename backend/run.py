from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

@app.route("/api/health")
def health():
    return {"status": "ok", "message": "EventSync backend is running"}

if __name__ == "__main__":
    app.run(debug=True, port=5001)