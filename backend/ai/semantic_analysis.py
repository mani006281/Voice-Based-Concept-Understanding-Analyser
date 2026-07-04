from sentence_transformers import SentenceTransformer
from sentence_transformers import util

# Load the model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(reference_text: str, user_text: str) -> float:
    """
    Calculate semantic similarity between two texts.
    Returns similarity percentage.
    """

    reference_embedding = model.encode(reference_text, convert_to_tensor=True)
    user_embedding = model.encode(user_text, convert_to_tensor=True)

    similarity = util.cos_sim(reference_embedding, user_embedding)

    return round(float(similarity) * 100, 2)