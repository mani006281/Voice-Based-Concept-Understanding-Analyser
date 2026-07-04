from fastapi import FastAPI

app = FastAPI(title="Voice Based Concept Understanding Analyser")

@app.get("/")
def home():
    return {
        "message": "Voice Based Concept Understanding Analyser API Running"
    }