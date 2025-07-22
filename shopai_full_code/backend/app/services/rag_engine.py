from .groq_llm import chat_with_context

# In a real RAG setup you'd vectorize and retrieve. Placeholder:
SAMPLE_KB = {
    "nike shoes": "Nike shoes are known for their comfort and style.",
    "iphone 15": "iPhone 15 features a new A18 chip and improved battery life."
}

def fetch_context(query: str) -> str:
    # Simplified keyword lookup
    for k, v in SAMPLE_KB.items():
        if k in query.lower():
            return v
    return "No additional context available."

def answer_query(question: str, context: str = "") -> str:
    if not context:
        context = fetch_context(question)
    return chat_with_context(question, context)
