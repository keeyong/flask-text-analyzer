from flask import Blueprint, jsonify, request, current_app
from .text_stats import analyze_text

bp = Blueprint("api", __name__)

@bp.get("/health")
def health():
    return jsonify({"status": "ok"}), 200

@bp.post("/analyze")
def analyze():
    # Basic JSON parsing with minimal validation (intentionally simple for review)
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")
    top = data.get("top", 5)

    if not isinstance(text, str):
        return jsonify({"error": "'text' must be a string"}), 400
    if not isinstance(top, int) or top < 0:
        return jsonify({"error": "'top' must be a non-negative integer"}), 400

    wpm = current_app.config.get("WORDS_PER_MINUTE", 200)
    report = analyze_text(text, top=top, words_per_minute=wpm)
    return jsonify(report), 200
