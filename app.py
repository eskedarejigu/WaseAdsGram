from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "status": "online",
        "service": "AdsGram Reward API"
    })


@app.get("/api/adsgram/reward")
def reward():
    user_id = request.args.get("userid", "").strip()

    if not user_id.isdigit() or int(user_id) <= 0:
        return jsonify({
            "ok": False,
            "error": "Invalid Telegram user ID"
        }), 400

    return jsonify({
        "ok": True,
        "message": "Reward callback received",
        "reward_credited": False
    })
