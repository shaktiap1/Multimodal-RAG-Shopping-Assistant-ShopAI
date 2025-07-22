# ShopAI — Multimodal RAG Shopping Assistant

*Generated on 2025-07-22T14:30:37.271738*

## Tech Stack

- **Backend:** Python · Flask · Groq API · AssemblyAI · Firebase · Google Cloud Storage
- **Frontend:** React · Vite · TailwindCSS
- **RAG:** Simple placeholder retrieval + Groq generation

## Getting Started (Development)

### Backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:FLASK_APP = "run.py"
flask run --port 8000
```

### Frontend

```powershell
cd frontend
npm install
npm run dev
```

The frontend runs on `localhost:5173` and proxies API calls to `localhost:8000`.
