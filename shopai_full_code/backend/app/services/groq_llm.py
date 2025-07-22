import os, requests

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_KEY = os.environ.get("GROQ_API_KEY", "YOUR_GROQ_API_KEY")

headers = {
    "Authorization": f"Bearer {GROQ_KEY}",
    "Content-Type": "application/json"
}

def _chat(messages, model="mixtral-8x7b-32768"):
    body = {
        "model": model,
        "messages": messages,
        "temperature": 0.7
    }
    resp = requests.post(GROQ_API_URL, headers=headers, json=body, timeout=60)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]

def generate_caption(image_path: str) -> str:
    """Call Groq GPT to generate an image caption (placeholder logic)."""
    prompt = f"You are an expert image captioning model. Provide a concise caption for the image at path: {image_path}"
    return _chat([{"role": "user", "content": prompt}])

def chat_with_context(question: str, context: str) -> str:
    return _chat([
        {"role": "system", "content": "You are a helpful shopping assistant."},
        {"role": "assistant", "content": context},
        {"role": "user", "content": question}
    ])
