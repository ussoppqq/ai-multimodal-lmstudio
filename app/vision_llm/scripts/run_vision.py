from app.vision_llm.services.preprocess import preprocess_image
from app.vision_llm.services.detector import detect_objects, extract_objects
from app.vision_llm.services.visualize import save_result
from app.vision_llm.services.save_json import save_detection_json
import os

IMAGE_PATH = "data/images/sample.jpg"
IMAGE_OUT = "data/outputs/result.jpg"
JSON_OUT = "data/outputs/result.json"

if __name__ == "__main__":
    os.makedirs("data/outputs", exist_ok=True)

    image = preprocess_image(IMAGE_PATH)
    results = detect_objects(image)

    # 1. SAVE IMAGE (INI WAJIB ADA)
    save_result(results, IMAGE_OUT)

    # 2. SAVE JSON
    objects = extract_objects(results)
    save_detection_json(objects, JSON_OUT)

    print("Vision detection completed")
    print(f"- Image saved to {IMAGE_OUT}")
    print(f"- JSON saved to {JSON_OUT}")
