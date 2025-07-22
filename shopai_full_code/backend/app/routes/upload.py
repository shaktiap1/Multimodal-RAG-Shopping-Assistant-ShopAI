import os, uuid, mimetypes
from flask import Blueprint, request, jsonify, current_app

bp = Blueprint("upload", __name__, url_prefix="/api")

@bp.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file in request"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    # Save file
    uid = uuid.uuid4().hex
    filename = f"{uid}-{file.filename}"
    save_path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    file.save(save_path)

    return jsonify({"filename": filename, "mimetype": mimetypes.guess_type(filename)[0]})
