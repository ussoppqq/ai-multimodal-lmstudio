import requests
from app.config.settings import LM_STUDIO_BASE_URL, LM_STUDIO_MODEL

def ask_llm(context: str, question: str) -> str:
    payload = {
        "model": LM_STUDIO_MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Answer ONLY based on the provided context. "
                    "If the answer is not in the context, say "
                    "'Informasi tidak ditemukan dalam dokumen.'"
                )
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{question}"
            }
        ]
    }

    response = requests.post(
        f"{LM_STUDIO_BASE_URL}/chat/completions",
        json=payload
    )
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
