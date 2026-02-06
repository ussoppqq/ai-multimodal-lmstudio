import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from app.config.settings import INDEX_DIR, EMBEDDING_MODEL

FAISS_PATH = os.path.join(INDEX_DIR, "index.faiss")
DOCS_PATH = os.path.join(INDEX_DIR, "docs.pkl")

model = SentenceTransformer(EMBEDDING_MODEL)

def build_index(chunks: list[str]):
    os.makedirs(INDEX_DIR, exist_ok=True)

    embeddings = model.encode(chunks, show_progress_bar=True)
    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, FAISS_PATH)

    with open(DOCS_PATH, "wb") as f:
        pickle.dump(chunks, f)

def load_index():
    index = faiss.read_index(FAISS_PATH)
    with open(DOCS_PATH, "rb") as f:
        documents = pickle.load(f)
    return index, documents

def search(index, documents, query: str, k: int = 3):
    query_vec = model.encode([query]).astype("float32")
    _, indices = index.search(query_vec, k)
    return [documents[i] for i in indices[0]]
