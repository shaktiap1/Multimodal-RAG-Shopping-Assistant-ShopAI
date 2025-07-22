import firebase_admin
from firebase_admin import credentials, firestore
import os

_app = None
_db = None

def init_firebase():
    global _app, _db
    if _app:
        return _db
    cred_path = os.environ.get("FIREBASE_CRED_JSON", "serviceAccount.json")
    cred = credentials.Certificate(cred_path)
    _app = firebase_admin.initialize_app(cred)
    _db = firestore.client()
    return _db

def store_chat(session_id: str, message: dict):
    db = init_firebase()
    db.collection("sessions").document(session_id).collection("messages").add(message)
