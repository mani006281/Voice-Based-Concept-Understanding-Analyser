import os
import sys
import streamlit as st

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from backend.services import evaluate_audio


# -----------------------------------
# Streamlit Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Voice Based Concept Understanding Analyser",
    page_icon="🎤",
    layout="wide"
)


# -----------------------------------
# Application Title
# -----------------------------------

st.title("🎤 Voice Based Concept Understanding Analyser")


# -----------------------------------
# Student Information
# -----------------------------------

student_name = st.text_input(
    "Enter Student Name"
)

st.write(
    "Upload your voice explanation and receive AI-powered evaluation."
)

st.divider()


# -----------------------------------
# Concept Selection
# -----------------------------------

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


# -----------------------------------
# Audio Upload
# -----------------------------------

audio_file = st.file_uploader(
    "Upload Audio",
    type=["wav", "mp3", "mp4", "m4a", "ogg"],
    help="Supported formats: WAV, MP3, MP4, M4A, OGG"
)


# -----------------------------------
# Audio Processing
# -----------------------------------

if audio_file is not None:

    # Create uploads directory
    os.makedirs("uploads", exist_ok=True)

    # Save uploaded audio
    audio_path = os.path.join(
        "uploads",
        os.path.basename(audio_file.name)
    )

    with open(audio_path, "wb") as f:
        f.write(audio_file.getbuffer())

    # Display uploaded audio
    st.subheader("🎧 Uploaded Audio")

    st.audio(audio_file)

    st.success("✅ Audio uploaded successfully!")


    # -----------------------------------
    # Evaluate Button
    # -----------------------------------

    if st.button("🚀 Evaluate"):

        # Validate student name
        if not student_name.strip():

            st.warning(
                "⚠ Please enter your name before evaluating."
            )

            st.stop()


        # -----------------------------------
        # AI Evaluation
        # -----------------------------------

        with st.spinner(
            "Analyzing your voice explanation... Please wait."
        ):

            try:

                result = evaluate_audio(
                    audio_path,
                    concept,
                    student_name.strip()
                )

            except Exception as e:

                st.error(
                    f"❌ Error during evaluation: {str(e)}"
                )

                st.stop()


        # -----------------------------------
        # Evaluation Results
        # -----------------------------------

        st.success("✅ Analysis Completed!")


        # Transcript
        st.subheader("📝 Transcript")

        st.write(
            result["transcript"]
        )


        # Semantic Similarity
        st.subheader("📊 Semantic Similarity")

        st.metric(
            "Similarity Score",
            f'{result["similarity"]:.2f}%'
        )


        # Gemini AI Feedback
        st.subheader("🤖 Gemini AI Feedback")

        st.write(
            result["feedback"]
        )


        # -----------------------------------
        # PDF Download Section
        # -----------------------------------

        st.subheader("📄 Download Evaluation Report")

        try:

            with open(result["pdf_path"], "rb") as pdf_file:

                pdf_data = pdf_file.read()

            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_data,
                file_name=f"{student_name.strip().replace(' ', '_')}_Evaluation_Report.pdf",
                mime="application/pdf"
            )

        except Exception as e:

            st.error(
                f"❌ Unable to download PDF report: {str(e)}"
            )
