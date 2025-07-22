from flask import Blueprint, request, jsonify
from app.services.rag_engine import answer_query

bp = Blueprint("rag", __name__, url_prefix="/api")

@bp.route("/query", methods=["POST"])
def rag_query():
    data = request.get_json(force=True)
    question = data.get("question", "")
    context = data.get("context", "")
    answer = answer_query(question, context)
    return jsonify({"answer": answer})
