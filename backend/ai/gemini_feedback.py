from google import genai
from backend.config import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)


def generate_feedback(reference_text, student_text, similarity_score):
    prompt = f"""
You are an expert evaluator.

Reference Answer:
{reference_text}

Student Answer:
{student_text}

Similarity Score:
{similarity_score}%

Give feedback in this format:

Concept Understanding:
Strengths:
Missing Concepts:
Suggestions:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text