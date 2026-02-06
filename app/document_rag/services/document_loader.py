import re
from pathlib import Path
from pypdf import PdfReader
from app.config.settings import PROCESSED_DIR

Path(PROCESSED_DIR).mkdir(parents=True, exist_ok=True)

def clean_text(text: str) -> str:
    text = text.replace("\r", "\n")
    text = re.sub(r"\n\d+\n", "\n", text)
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    text = " ".join(lines)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"-\s+", "", text)

    return text.strip()

def load_pdf(path: str) -> str:
    reader = PdfReader(path)
    raw_text = ""

    for page in reader.pages:
        if page.extract_text():
            raw_text += page.extract_text() + "\n"

    cleaned = clean_text(raw_text)

    out_path = Path(PROCESSED_DIR) / (Path(path).stem + ".txt")
    out_path.write_text(cleaned, encoding="utf-8")

    return cleaned
