import os
import platform
from functools import lru_cache

# Configure FFmpeg for local Windows development
if platform.system() == "Windows":
    ffmpeg_path = r"C:\ffmpeg-8.1.2-essentials_build\bin"

    if os.path.isdir(ffmpeg_path):
        os.environ["PATH"] = (
            ffmpeg_path
            + os.pathsep
            + os.environ.get("PATH", "")
        )

import whisper


@lru_cache(maxsize=1)
def load_whisper_model():
    """
    Load Whisper only once per Python process.
    """
    return whisper.load_model("base")


def transcribe_audio(audio_path: str) -> str:
    """
    Convert an audio file into text using Whisper.
    """

    model = load_whisper_model()

    result = model.transcribe(
        audio_path,
        fp16=False
    )

    return result["text"].strip()
