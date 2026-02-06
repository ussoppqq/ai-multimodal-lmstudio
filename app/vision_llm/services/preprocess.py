from PIL import Image

def preprocess_image(path: str):
    return Image.open(path).convert("RGB")
