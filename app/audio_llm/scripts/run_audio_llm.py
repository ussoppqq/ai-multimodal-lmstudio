from app.audio_llm.services.recorder import record_audio
from app.audio_llm.services.speech_to_text import transcribe_audio
from app.audio_llm.services.prompt_builder import build_audio_prompt
from app.common.llm_client import ask_llm
from app.audio_llm.services.text_to_speech import speak

AUDIO_PATH = "data/audio/input.wav"

if __name__ == "__main__":
    print("=== AUDIO → LLM PIPELINE ===")

    # 1. record audio
    record_audio(AUDIO_PATH)

    # 2. speech to text
    transcript = transcribe_audio(AUDIO_PATH)
    print(f"\nUser said: {transcript}")

    # 3. build prompt
    prompt = build_audio_prompt(transcript)

    # 4. ask LLM
    answer = ask_llm(prompt, "Respond to user speech")

    print("\n=== LLM RESPONSE ===")
    print(answer)

    # optional voice output
    # speak(answer)
