import os
from dotenv import load_dotenv

# Load environment variables from the local .env file
load_dotenv()

# Read the Gemini API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Validate the API key
if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY is missing. "
        "Configure it in your local .env file or "
        "in Streamlit Community Cloud secrets."
    )