import os
import logging

from flask import Flask, jsonify, request

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/")
def home():
    return jsonify({
        "status": "online",
        "service": "AdsGram Reward API",
        "bot": "Waserecbot"
    }), 200


@app.get("/api/adsgram/reward")
def adsgram_reward():
    user_id = request.args.get("userid", "").strip()

    if not user_id.isdigit():
        return jsonify({
            "ok": False,
            "error": "Invalid Telegram user ID"
        }), 400

    if int(user_id) <= 0:
        return jsonify({
            "ok": False,
            "error": "Invalid Telegram user ID"
        }), 400

    # Diagnostic mode only.
    # Do not credit points until callback authentication
    # and duplicate-reward protection are implemented.

    logger.info("Reward callback received")

    return jsonify({
        "ok": True,
        "message": "Reward callback received",
        "reward_credited": False
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
