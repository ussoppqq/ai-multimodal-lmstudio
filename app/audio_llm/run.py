from app.audio_llm.services.recorder import record_audio
from app.audio_llm.services.speech_to_text import transcribe_audio
from app.audio_llm.services.prompt_builder import build_audio_prompt
from app.common.llm_client import ask_llm

AUDIO_PATH = "data/audio/input.wav"


def run_audio_pipeline():
    # record
    record_audio(AUDIO_PATH)

    # speech to text
    transcript = transcribe_audio(AUDIO_PATH)

    # build prompt
    prompt = build_audio_prompt(transcript)

    # ask llm
    answer = ask_llm(prompt, "Respond to user speech")

    return {
        "transcript": transcript,
        "answer": answer
    }
