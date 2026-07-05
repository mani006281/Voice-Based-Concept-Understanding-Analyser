from backend.services import evaluate_audio

result = evaluate_audio(
    "uploads/sample.mp4",
    "Artificial Intelligence"
)

print("\n========== RESULT ==========\n")

print("Concept:")
print(result["concept"])

print("\nTranscript:")
print(result["transcript"])

print("\nSimilarity:")
print(result["similarity"])

print("\nFeedback:")
print(result["feedback"])