from backend.ai.gemini_feedback import generate_feedback

reference = """
Artificial Intelligence is the simulation of human intelligence by machines that can learn, reason and solve problems.
"""

student = """
Artificial Intelligence helps computers learn and make decisions like humans.
"""

feedback = generate_feedback(reference, student, 81.48)

print(feedback)