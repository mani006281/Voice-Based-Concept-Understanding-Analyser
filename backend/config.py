import os
from dotenv import load_dotenv

# Load environment variables from .env when running locally.
load_dotenv()

# Works with local .env and cloud environment variables.
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY is missing. "
        "Configure it in your local .env file or "
        "in Streamlit Community Cloud secrets."
    )