from fastapi import APIRouter, UploadFile, File
import os
from app.vision_llm.services.preprocess import preprocess_image
from app.vision_llm.services.detector import detect_objects, extract_objects
from app.vision_llm.services.visualize import save_result
from app.vision_llm.services.save_json import save_detection_json
from app.vision_llm.services.prompt_builder import build_vision_prompt
from app.common.llm_client import ask_llm

router = APIRouter()

@router.post("/detect")
async def detect_vision(file: UploadFile = File(...)):
    os.makedirs("data/outputs", exist_ok=True)
    image_path = f"data/outputs/{file.filename}"
    with open(image_path, "wb") as f:
        f.write(await file.read())

    image = preprocess_image(image_path)
    results = detect_objects(image)
    save_result(results, f"data/outputs/result.jpg")
    objects = extract_objects(results)
    save_detection_json(objects, f"data/outputs/result.json")

    prompt = build_vision_prompt(objects)
    answer = ask_llm(prompt, "Jelaskan gambar ini")

    return {
        "detected_objects": objects,
        "llm_answer": answer
    }
