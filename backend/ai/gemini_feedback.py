from google import genai
from google.genai.errors import ServerError
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

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except ServerError:
        return """
Concept Understanding:
AI feedback is temporarily unavailable.

Strengths:
Generated locally.

Missing Concepts:
Unable to analyze because the Gemini service is busy.

Suggestions:
Please try again after a few minutes.
"""

    except Exception as e:
        return f"Error generating feedback: {str(e)}"