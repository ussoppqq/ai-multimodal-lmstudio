import json
from app.vision_llm.services.prompt_builder import build_vision_prompt
from app.common.llm_client import ask_llm

JSON_PATH = "data/outputs/result.json"

with open(JSON_PATH) as f:
    objects = json.load(f)

prompt = build_vision_prompt(objects)
answer = ask_llm(prompt, "Explain the image")

print("=== DETECTED OBJECTS ===")
for obj in objects:
    print(obj)
    
print("\n=== LLM INTERPRETATION ===")
print(answer)
