from fastapi import FastAPI

from app.document_rag.api import upload, query
from app.audio_llm.api import listen

app = FastAPI(title="AI Multimodal LM Studio")

# ===============================
# DOCUMENT RAG
# ===============================
app.include_router(upload.router, prefix="/docs", tags=["Document RAG"])
app.include_router(query.router, prefix="/docs", tags=["Document RAG"])

# ===============================
# AUDIO LLM
# ===============================
app.include_router(listen.router, prefix="/audio", tags=["Audio LLM"])

@app.get("/")
def root():
    return {
        "status": "running",
        "services": [
            "document_rag",
            "audio_llm",
            "vision_llm (script)"
        ]
    }
