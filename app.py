from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from bot import get_hint
import os
import traceback

app = Flask(__name__)
CORS(app, origins=["https://glx.globallogic.com"], methods=["POST", "OPTIONS"])

@app.route("/ask", methods=["POST", "OPTIONS"])
def ask():
    if request.method == "OPTIONS":
        return '', 204 # preflight response


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
