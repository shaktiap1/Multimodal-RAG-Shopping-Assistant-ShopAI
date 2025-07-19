from flask import Blueprint, request, jsonify
from app.rag_engine import query_rag
from app.firebase_sync import store_message

main = Blueprint('main', __name__)

@main.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    user_id = request.json.get('user_id')
    response = query_rag(user_input)
    store_message(user_id, user_input, response)
    return jsonify({'response': response})
