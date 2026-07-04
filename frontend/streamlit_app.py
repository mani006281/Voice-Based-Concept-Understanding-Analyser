import os
import sys
import streamlit as st

# Allow importing from the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.speech_to_text import transcribe_audio

st.set_page_config(
    page_title="Voice Based Concept Understanding Analyser",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 Voice Based Concept Understanding Analyser")

st.write("Upload your voice explanation and receive AI-powered feedback.")

st.divider()

concept = st.selectbox(
    "Select a Concept",
    [
        "Artificial Intelligence",
        "Machine Learning",
        "Cloud Computing",
        "Python",
        "Data Structures"
    ]
)

audio_file = st.file_uploader(
    "Upload Audio File",
    type=["wav", "mp3", "m4a"]
)

if audio_file is not None:

    os.makedirs("uploads", exist_ok=True)

    audio_path = os.path.join("uploads", audio_file.name)

    with open(audio_path, "wb") as f:
        f.write(audio_file.getbuffer())

    st.success("Audio uploaded successfully!")

    st.audio(audio_file)

    if st.button("Convert Speech to Text"):

        with st.spinner("Transcribing..."):

            transcript = transcribe_audio(audio_path)

        st.subheader("Transcript")

        st.write(transcript)