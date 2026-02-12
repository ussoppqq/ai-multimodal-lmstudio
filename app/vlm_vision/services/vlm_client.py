import base64
import requests

LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "llava-v1.6-mistral"


def encode_image(path: str):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def ask_vlm(image_path: str, prompt: str):

    image_base64 = encode_image(image_path)

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ]
    }

    response = requests.post(LM_STUDIO_URL, json=payload)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
