from backend.ai.semantic_analysis import calculate_similarity

reference = """
Artificial Intelligence is the simulation of human intelligence by machines that can learn, reason, and solve problems.
"""

user = """
Artificial Intelligence helps computers learn and make decisions like humans.
"""

score = calculate_similarity(reference, user)

print("\nSemantic Similarity Score:")
print(score, "%")