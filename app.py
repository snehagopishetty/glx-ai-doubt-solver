from flask import Flask, request, jsonify
from flask_cors import CORS
from bot import get_hint
import os

app = Flask(__name__)
CORS(app, resources={r"/ask": {"origins": "*"}}, supports_credentials=True)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')  # Or 'https://glx.globallogic.com'
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        hint = get_hint(question)
        return jsonify({"hint": hint})
    except Exception as e:
        print(f"[❌] Internal Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # app.run(port=5000, debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
