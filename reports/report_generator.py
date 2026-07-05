from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os


def generate_pdf(student_name, concept, transcript, similarity, feedback):

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{student_name.replace(' ', '_')}_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>Voice Based Concept Understanding Analyser</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Student Name:</b> {student_name}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Concept:</b> {concept}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Date:</b> {datetime.now().strftime('%d-%m-%Y %H:%M')}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Transcript</b>", styles["Heading2"]))
    story.append(Paragraph(transcript, styles["BodyText"]))

    story.append(Paragraph("<br/><b>Semantic Similarity</b>", styles["Heading2"]))
    story.append(Paragraph(f"{similarity:.2f}%", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Gemini AI Feedback</b>", styles["Heading2"]))
    story.append(Paragraph(feedback.replace("\n", "<br/>"), styles["BodyText"]))

    doc.build(story)

    return filename