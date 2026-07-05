import json
from pathlib import Path

from reports.report_generator import generate_pdf
from database.database import SessionLocal
from database.models import Evaluation

from backend.ai.speech_to_text import transcribe_audio
from backend.ai.semantic_analysis import calculate_similarity
from backend.ai.gemini_feedback import generate_feedback


BASE_DIR = Path(__file__).resolve().parent.parent
CONCEPT_FILE = BASE_DIR / "data" / "concepts.json"


def get_reference_answer(concept_name: str):
    with open(CONCEPT_FILE, "r", encoding="utf-8") as file:
        concepts = json.load(file)

    return concepts.get(concept_name)


def evaluate_audio(audio_path: str, concept_name: str, student_name: str):

    # Get reference answer
    reference = get_reference_answer(concept_name)

    # Convert speech to text
    transcript = transcribe_audio(audio_path)

    # Calculate semantic similarity
    similarity = calculate_similarity(reference, transcript)

    # Generate Gemini AI feedback
    feedback = generate_feedback(
        reference,
        transcript,
        similarity
    )

    # Save evaluation to SQLite database
    db = SessionLocal()

    record = Evaluation(
        student_name=student_name,
        concept=concept_name,
        transcript=transcript,
        similarity=similarity,
        feedback=feedback
    )

    db.add(record)
    db.commit()
    db.close()

    # Generate PDF report
    pdf_path = generate_pdf(
        student_name,
        concept_name,
        transcript,
        similarity,
        feedback
    )

    # Return results to Streamlit
    return {
        "concept": concept_name,
        "reference": reference,
        "transcript": transcript,
        "similarity": similarity,
        "feedback": feedback,
        "pdf_path": pdf_path
    }