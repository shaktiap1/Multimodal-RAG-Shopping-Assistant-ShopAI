# 🛍️ ShopAI – Your Smart Multimodal Shopping Assistant
**Mentor:** Mr. Pranav Kumar  
**Built with:** Python · Flask · React.js · Firebase · Groq · AssemblyAI · GCP  

---

### 👋 About the Project

Shopping online can be overwhelming — too many options, not enough context. **ShopAI** is built to fix that. It’s your personal shopping assistant powered by Retrieval-Augmented Generation (RAG), voice capabilities, and real-time syncing via Firebase.

This is one of the core modules of my **GTM AI OS** suite — focused on AI-first user experiences.

---

### 🧠 What ShopAI Can Do

- 🧑‍💬 Accepts voice + text queries from users (AssemblyAI-ready)
- 🔎 Uses RAG (Retrieval-Augmented Generation) to deliver relevant answers
- 💬 Chats through a clean React-based UI
- 🔥 Syncs chats in real-time with Firestore
- ⚡️ Backend is modular, fast, and Groq API-ready

---

### 🧪 Try It Locally

#### 🔧 Backend Setup
```bash
cd backend
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
python run.py
```

#### 💻 Frontend Setup
```bash
cd frontend
npm install
npm start
```

#### 🗝️ Environment Variables (Backend)
Create a `.env` file in the `/backend` folder:
```env
GOOGLE_CLOUD_PROJECT=your_project_id
FIREBASE_CREDENTIALS=path/to/firebase_credentials.json
```
