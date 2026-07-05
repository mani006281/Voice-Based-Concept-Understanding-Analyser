import os
import sys
import streamlit as st
import pandas as pd

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.database import SessionLocal
from database.models import Evaluation

st.set_page_config(
    page_title="Evaluation History",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Evaluation History")

db = SessionLocal()

records = db.query(Evaluation).all()

db.close()

if len(records) == 0:
    st.warning("No evaluations found.")
else:

    data = []

    for record in records:

        data.append({
            "ID": record.id,
            "Student": record.student_name,
            "Concept": record.concept,
            "Similarity (%)": round(record.similarity, 2)
        })

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True
    )