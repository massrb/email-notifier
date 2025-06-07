from flask import Flask, request, jsonify
from utils import send_email  # adjust if needed

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    subject = data.get("subject", "No subject")
    body = data.get("body", "")
    to_email = data.get("to")

    if not to_email or not body:
        return jsonify({"error": "Missing 'to' or 'body' field"}), 400

    try:
        send_email(subject, body, to_email)
        return jsonify({"status": "email sent"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
