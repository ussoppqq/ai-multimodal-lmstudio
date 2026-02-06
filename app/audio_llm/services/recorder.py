import sounddevice as sd
import soundfile as sf
import os

SAMPLE_RATE = 16000
CHANNELS = 1
DURATION = 5  # seconds


def record_audio(output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print("Recording... Speak now")
    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="float32"
    )
    sd.wait()

    sf.write(output_path, audio, SAMPLE_RATE)
    print(f"Audio saved to {output_path}")
