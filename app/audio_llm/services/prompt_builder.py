def build_audio_prompt(transcript: str) -> str:
    prompt = f"""
You are a helpful AI assistant.

The user said:
"{transcript}"

Please respond clearly and helpfully.
"""
    return prompt.strip()
