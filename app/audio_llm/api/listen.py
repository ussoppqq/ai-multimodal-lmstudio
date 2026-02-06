from fastapi import APIRouter
from app.audio_llm.run import run_audio_pipeline

router = APIRouter()

@router.post("/listen")
def listen_audio():
    result = run_audio_pipeline()

    return {
        "transcript": result["transcript"],
        "answer": result["answer"]
    }
