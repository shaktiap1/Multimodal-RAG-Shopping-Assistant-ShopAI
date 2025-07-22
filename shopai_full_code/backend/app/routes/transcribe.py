import os, requests
from flask import Blueprint, request, jsonify

bp = Blueprint("transcribe", __name__, url_prefix="/api")

ASSEMBLYAI_URL = "https://api.assemblyai.com/v2/transcript"
AAI_KEY = os.environ.get("ASSEMBLYAI_API_KEY", "YOUR_AAI_KEY")

@bp.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file"}), 400
    audio_file = request.files["audio"]

    # Simple upload & poll pattern
    headers = {"authorization": AAI_KEY}
    upload_response = requests.post(
        "https://api.assemblyai.com/v2/upload",
        headers=headers,
        data=audio_file
    )
    upload_response.raise_for_status()
    audio_url = upload_response.json()["upload_url"]

    transcript_response = requests.post(
        ASSEMBLYAI_URL,
        headers=headers,
        json={"audio_url": audio_url}
    )
    transcript_response.raise_for_status()
    transcript_id = transcript_response.json()["id"]

    # Poll status (simplified, production should use webhook)
    status = "queued"
    while status not in ("completed", "error"):
        poll = requests.get(f"{ASSEMBLYAI_URL}/{transcript_id}", headers=headers)
        poll.raise_for_status()
        data = poll.json()
        status = data["status"]

    if status == "error":
        return jsonify({"error": data.get("error")}), 500

    return jsonify({"text": data["text"]})
