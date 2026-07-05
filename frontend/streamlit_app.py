import os
import sys
import streamlit as st

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.services import evaluate_audio

st.set_page_config(
    page_title="Voice Based Concept Understanding Analyser",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 Voice Based Concept Understanding Analyser")

student_name = st.text_input(
    "Enter Student Name"
)

st.write("Upload your voice explanation and receive AI-powered evaluation.")

st.divider()

concept = st.selectbox(
    "Select Concept",
    [
        "Artificial Intelligence",
        "Machine Learning",
        "Cloud Computing",
        "Python",
        "Data Structures"
    ]
)

audio_file = st.file_uploader(
    "Upload Audio",
    type=["wav", "mp3", "mp4", "m4a"]
)

if audio_file is not None:

    os.makedirs("uploads", exist_ok=True)

    audio_path = os.path.join("uploads", audio_file.name)

    with open(audio_path, "wb") as f:
        f.write(audio_file.getbuffer())

    st.audio(audio_file)

    if st.button("🚀 Evaluate"):

        # Check whether the student entered a name
        if not student_name.strip():
            st.warning("⚠ Please enter your name before evaluating.")
            st.stop()

        with st.spinner("Analyzing... Please wait..."):

            result = evaluate_audio(
                audio_path,
                concept,
                student_name
            )

        st.success("✅ Analysis Completed!")

        st.subheader("📝 Transcript")
        st.write(result["transcript"])

        st.subheader("📊 Semantic Similarity")
        st.metric("Similarity Score", f'{result["similarity"]}%')

        st.subheader("🤖 Gemini AI Feedback")
        st.write(result["feedback"])

        # -----------------------------
        # PDF Download Section
        # -----------------------------
        st.subheader("📄 Download Evaluation Report")

        with open(result["pdf_path"], "rb") as pdf_file:
            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_file,
                file_name=f"{student_name}_Evaluation_Report.pdf",
                mime="application/pdf"
            )