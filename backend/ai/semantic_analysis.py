from functools import lru_cache

from sentence_transformers import SentenceTransformer, util


@lru_cache(maxsize=1)
def load_semantic_model():
    """
    Load the Sentence Transformers model once per process.
    """
    return SentenceTransformer("all-MiniLM-L6-v2", device="cpu")


def calculate_similarity(reference_text: str, user_text: str) -> float:
    """
    Calculate semantic similarity between two texts.
    Returns similarity percentage.
    """

    if not reference_text or not user_text:
        return 0.0

    model = load_semantic_model()

    reference_embedding = model.encode(
        reference_text,
        convert_to_tensor=True
    )

    user_embedding = model.encode(
        user_text,
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        reference_embedding,
        user_embedding
    )

    return round(float(similarity.item()) * 100, 2)
