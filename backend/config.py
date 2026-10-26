import os
from dotenv import load_dotenv

# Load environment variables from .env during local development
load_dotenv()

# Read Gemini API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Validate API key
if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY is missing. "
        "Set it in your .env file or deployment environment."
    )
