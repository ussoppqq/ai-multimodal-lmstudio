from fastapi import APIRouter, UploadFile, File
import os
from app.config.settings import UPLOAD_DIR

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    path = os.path.join(UPLOAD_DIR, file.filename)

    with open(path, "wb") as f:
        f.write(await file.read())

    return {
        "message": "File uploaded successfully",
        "filename": file.filename
    }
