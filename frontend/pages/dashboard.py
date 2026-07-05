import os
import sys
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.database import SessionLocal
from database.models import Evaluation

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Voice Evaluation Dashboard")

# -----------------------------
# Fetch Data from Database
# -----------------------------
db = SessionLocal()
records = db.query(Evaluation).all()
db.close()

if not records:
    st.warning("No evaluations found.")
    st.stop()

# -----------------------------
# Convert Database Records to DataFrame
# -----------------------------
df = pd.DataFrame([
    {
        "student_name": r.student_name,
        "concept": r.concept,
        "similarity": r.similarity
    }
    for r in records
])

# -----------------------------
# Dashboard Metrics
# -----------------------------
total = len(df)

highest = df["similarity"].max()

average = df["similarity"].mean()

students = df["student_name"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("📄 Total Evaluations", total)
col2.metric("🏆 Highest Score", f"{highest:.2f}%")
col3.metric("📈 Average Score", f"{average:.2f}%")
col4.metric("👨‍🎓 Students", students)

# -----------------------------
# Student Performance Chart
# -----------------------------
st.divider()

st.subheader("📊 Student Performance")

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(
    df["student_name"],
    df["similarity"]
)

ax.set_xlabel("Students")
ax.set_ylabel("Similarity Score (%)")
ax.set_title("Student Similarity Scores")

plt.xticks(rotation=20)

st.pyplot(fig)

# -----------------------------
# Concept Distribution Chart
# -----------------------------
st.divider()

st.subheader("🥧 Concept Distribution")

concept_counts = df["concept"].value_counts()

fig2, ax2 = plt.subplots(figsize=(6, 6))

ax2.pie(
    concept_counts,
    labels=concept_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

ax2.set_title("Evaluations by Concept")

st.pyplot(fig2)