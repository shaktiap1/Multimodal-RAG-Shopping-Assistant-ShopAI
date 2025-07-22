from flask import Blueprint, request, jsonify
from app.services.groq_llm import generate_caption

bp = Blueprint("caption", __name__, url_prefix="/api")

@bp.route("/caption", methods=["POST"])
def caption():
    data = request.get_json(force=True)
    image_path = data.get("image_path")
    if not image_path:
        return jsonify({"error": "image_path is required"}), 400

    caption_text = generate_caption(image_path)
    return jsonify({"caption": caption_text})
