import os
from app.config.settings import UPLOAD_DIR
from app.document_rag.services.document_loader import load_pdf
from app.document_rag.services.text_splitter import split_text
from app.document_rag.services.vector_store import build_index

texts = []

for file in os.listdir(UPLOAD_DIR):
    if file.lower().endswith(".pdf"):
        text = load_pdf(os.path.join(UPLOAD_DIR, file))
        texts.extend(split_text(text))

build_index(texts)
print("Index built successfully")
