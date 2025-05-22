from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from bot import get_hint
import os
import traceback

app = Flask(__name__)
frontend_origin = "https://glx.globallogic.com"
CORS(app, resources={r"/ask": {"origins": frontend_origin}}, allow_headers="", methods=["POST", "OPTIONS"])

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = frontend_origin
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
    return response

@app.route("/ask", methods=["POST", "OPTIONS"])
def ask():
    if request.method == "OPTIONS":
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = frontend_origin
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
        return response, 204

    data = request.get_json()
    question = data.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        hint = get_hint(question)
        return jsonify({"hint": hint})
    except Exception as e:
        print(f"[❌] Internal Error: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
