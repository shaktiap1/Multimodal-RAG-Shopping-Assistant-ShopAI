# ShopAI: Multimodal RAG Shopping Assistant

An AI-powered multimodal assistant for real-time product search and recommendations, using RAG + Groq + Firebase.

## Features
- Adaptive Retrieval-Augmented Generation engine
- Real-time Firestore sync for chat memory
- Flask backend with React frontend
- Voice-enabled input via AssemblyAI

## Run Instructions

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

### Frontend
```bash
cd frontend
npm install
npm start
```
