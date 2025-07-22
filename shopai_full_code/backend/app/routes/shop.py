from flask import Blueprint, request, jsonify
from app.services.utils import dummy_product_search

bp = Blueprint("shop", __name__, url_prefix="/api")

@bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json(force=True)
    query = data.get("query", "")
    products = dummy_product_search(query)
    return jsonify({"products": products})
