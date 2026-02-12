from fastapi import APIRouter, UploadFile, File, BackgroundTasks
import os

from app.config.settings import UPLOAD_DIR
from app.document_rag.services.document_loader import load_pdf
from app.document_rag.services.text_splitter import split_text
from app.document_rag.services.vector_store import build_index

router = APIRouter()

def process_document(file_path):
    text = load_pdf(file_path)
    chunks = split_text(text)
    build_index(chunks)


@router.post("/")
async def upload_file(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...)
):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # jalan di background
    background_tasks.add_task(process_document, file_path)

    return {
        "message": "File uploaded. Indexing in progress."
    }
