import whisper

print("Loading Whisper model...")
model = whisper.load_model("base")  


def transcribe_audio(audio_path: str) -> str:
    print("Transcribing audio...")
    result = model.transcribe(audio_path)
    return result["text"].strip()
