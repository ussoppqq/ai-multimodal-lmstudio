import pickle
import faiss
import numpy as np
import requests
from sentence_transformers import SentenceTransformer

from app.config.settings import (
    LM_STUDIO_BASE_URL,
    LM_STUDIO_MODEL,
    INDEX_DIR,
)

# CONFIG
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

INDEX_PATH = f"{INDEX_DIR}/index.faiss"
DOCS_PATH = f"{INDEX_DIR}/docs.pkl"

TOP_K = 3
TEMPERATURE = 0.2

# LOAD EMBEDDING MODEL
print("Loading embedding model...")
embedder = SentenceTransformer(EMBEDDING_MODEL)

# LOAD INDEX & DOCS
print("Loading FAISS index...")
index = faiss.read_index(INDEX_PATH)

print("Loading documents...")
with open(DOCS_PATH, "rb") as f:
    documents = pickle.load(f)

# SEARCH FUNCTION
def retrieve_context(query, top_k=TOP_K):
    query_embedding = embedder.encode([query]).astype("float32")
    _, indices = index.search(query_embedding, top_k)

    return "\n\n".join(
        documents[idx] for idx in indices[0] if idx < len(documents)
    )

# ASK LM STUDIO
def ask_lmstudio(context, question):
    payload = {
        "model": LM_STUDIO_MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Kamu adalah asisten AI. "
                    "Jawablah HANYA berdasarkan konteks yang diberikan. "
                    "Jika jawaban tidak ada di konteks, katakan "
                    "'Informasi tidak ditemukan dalam dokumen.'"
                )
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{question}"
            }
        ],
        "temperature": TEMPERATURE
    }

    response = requests.post(
        f"{LM_STUDIO_BASE_URL}/chat/completions",
        json=payload
    )
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]

# MAIN LOOP
if __name__ == "__main__":
    print("\n=== RAG LM Studio CLI Ready ===\n")

    while True:
        question = input("Tanya (ketik 'exit' untuk keluar): ")
        if question.lower() == "exit":
            break

        context = retrieve_context(question)
        answer = ask_lmstudio(context, question)

        print("\n--- JAWABAN ---")
        print(answer)
        print("\n----------------\n")
