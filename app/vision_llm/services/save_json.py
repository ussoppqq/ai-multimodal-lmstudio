import json
import os

def save_detection_json(objects, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(objects, f, indent=2)
