from flask import Flask, request, jsonify
from flask_cors import CORS
from bot import get_hint

app = Flask(__name__)
CORS(app)

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
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
