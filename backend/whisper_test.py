from backend.ai.speech_to_text import transcribe_audio

text = transcribe_audio("uploads/sample.mp4")

print("\nTranscript:\n")
print(text)