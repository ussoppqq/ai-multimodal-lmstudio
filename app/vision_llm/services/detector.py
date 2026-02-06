from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_objects(image):
    return model(image)

def extract_objects(results):
    objects = []

    for r in results:
        for box in r.boxes:
            objects.append({
                "label": r.names[int(box.cls)],
                "confidence": float(box.conf)
            })

    return objects
