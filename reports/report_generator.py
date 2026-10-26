from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from pathlib import Path
from html import escape
from uuid import uuid4


# Get project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Directory for generated reports
REPORTS_DIR = BASE_DIR / "reports"


def generate_pdf(student_name, concept, transcript, similarity, feedback):

    # Create reports directory if it doesn't exist
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # Generate a unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id = uuid4().hex[:8]

    filename = REPORTS_DIR / f"evaluation_{timestamp}_{unique_id}.pdf"

    # Create PDF document
    doc = SimpleDocTemplate(
        str(filename),
        pagesize=(595.27, 841.89),
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    story = []

    # Report title
    story.append(
        Paragraph(
            "Voice Based Concept Understanding Analyser",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    # Student information
    story.append(
        Paragraph(
            f"<b>Student Name:</b> {escape(str(student_name))}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Concept:</b> {escape(str(concept))}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Date:</b> {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 20))

    # Transcript
    story.append(
        Paragraph("Transcript", styles["Heading2"])
    )

    story.append(
        Paragraph(
            escape(str(transcript)).replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 15))

    # Semantic similarity
    story.append(
        Paragraph("Semantic Similarity", styles["Heading2"])
    )

    story.append(
        Paragraph(
            f"{float(similarity):.2f}%",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 15))

    # Gemini feedback
    story.append(
        Paragraph("Gemini AI Feedback", styles["Heading2"])
    )

    story.append(
        Paragraph(
            escape(str(feedback)).replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    # Generate PDF
    doc.build(story)

    return str(filename)
