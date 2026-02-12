from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ===============================
# IMPORT ROUTERS
# ===============================
from app.document_rag.api import upload, query
from app.audio_llm.api import listen
from app.vision_llm.api import vision


# ===============================
# FASTAPI APP
# ===============================
app = FastAPI(
    title="AI Multimodal LM Studio",
    description="Document RAG, Vision Detection, and Audio Interaction API",
    version="1.0.0"
)


# ===============================
# CORS MIDDLEWARE (IMPORTANT FOR REACT)
# ===============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ===============================
# DOCUMENT RAG
# ===============================
app.include_router(
    upload.router,
    prefix="/docs",
    tags=["Document RAG"]
)

app.include_router(
    query.router,
    prefix="/docs",
    tags=["Document RAG"]
)


# ===============================
# AUDIO LLM
# ===============================
app.include_router(
    listen.router,
    prefix="/audio",
    tags=["Audio LLM"]
)


# ===============================
# VISION LLM
# ===============================
app.include_router(
    vision.router,
    prefix="/vision",
    tags=["Vision LLM"]
)


# ===============================
# ROOT ENDPOINT
# ===============================
@app.get("/")
def root():
    return {
        "status": "running",
        "services": [
            "document_rag",
            "audio_llm",
            "vision_llm"
        ]
    }
