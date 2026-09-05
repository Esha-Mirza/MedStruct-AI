"""
Flask frontend for the Medical Note Structuring tool.

This file ONLY renders the UI and forwards requests to the existing
FastAPI backend (main.py, unchanged) running on http://localhost:8000.
No extraction logic lives here.
"""
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

FASTAPI_URL = "http://localhost:8000/extract/"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/extract", methods=["POST"])
def extract():
    """Proxy the note to the FastAPI backend, exactly as app.py (Streamlit) did."""
    note = request.form.get("note", "").strip()

    if not note:
        return jsonify({"error": "Please paste a clinical note."}), 400

    try:
        response = requests.post(FASTAPI_URL, data={"note": note}, timeout=240)
    except requests.exceptions.ConnectionError:
        return jsonify({
            "error": "Cannot connect to backend. Make sure FastAPI (main.py) is running on port 8000."
        }), 502
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    if response.status_code != 200:
        return jsonify({"error": f"Backend error: {response.status_code}"}), 502

    data = response.json().get("structured", {})
    return jsonify({"structured": data})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
