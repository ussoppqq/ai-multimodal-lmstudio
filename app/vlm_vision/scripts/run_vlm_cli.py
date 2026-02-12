import os
from app.vlm_vision.services.vlm_client import ask_vlm

IMAGE_PATH = "data/images/sample1.jpg"


def main():
    print("=== VLM VISION CLI ===")

    if not os.path.exists(IMAGE_PATH):
        print(f"Image not found: {IMAGE_PATH}")
        return

    prompt = (
        "Jelaskan apa yang terjadi pada gambar ini secara objektif "
        "dan singkat tanpa membuat asumsi berlebihan."
    )

    print("Sending image to VLM...")

    answer = ask_vlm(IMAGE_PATH, prompt)

    print("\n=== VLM EXPLANATION ===")
    print(answer)


if __name__ == "__main__":
    main()
