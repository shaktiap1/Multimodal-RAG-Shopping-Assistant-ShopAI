import firebase_admin
from firebase_admin import credentials, firestore
import os

if not firebase_admin._apps:
    cred = credentials.Certificate('path/to/your/firebase_credentials.json')
    firebase_admin.initialize_app(cred)

db = firestore.client()

def store_message(user_id, user_msg, bot_msg):
    doc_ref = db.collection('chatlogs').document(user_id)
    doc_ref.set({'last_query': user_msg, 'response': bot_msg})
