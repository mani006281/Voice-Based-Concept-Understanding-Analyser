import os

# Add FFmpeg to PATH for this Python process
os.environ["PATH"] = (
    r"C:\ffmpeg-8.1.2-essentials_build\bin"
    + os.pathsep
    + os.environ.get("PATH", "")
)

import whisper

# Load Whisper model
model = whisper.load_model("base")


def transcribe_audio(audio_path: str) -> str:
    result = model.transcribe(audio_path)
    return result["text"]