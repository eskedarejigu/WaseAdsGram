import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({"status": "online"})

@app.get("/api/adsgram/reward")
def adsgram_reward():
    user_id = request.args.get("userid", "").strip()

    if not user_id.isdigit() or int(user_id) <= 0:
        return jsonify({"ok": False, "error": "Invalid user ID"}), 400

    webhook_url = os.environ.get("TBC_REWARD_WEBHOOK_URL")

    if not webhook_url:
        return jsonify({"ok": False, "error": "TBC webhook not configured"}), 503

    response = requests.post(
        webhook_url,
        json={"user_id": int(user_id), "points": 2},
        timeout=15
    )

    response.raise_for_status()

    return jsonify({
        "ok": True,
        "message": "Reward forwarded to TBC"
    })
