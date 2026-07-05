from database.database import SessionLocal
from database.models import Evaluation

db = SessionLocal()

records = db.query(Evaluation).all()

print("\n========== DATABASE RECORDS ==========\n")

for record in records:
    print(f"ID: {record.id}")
    print(f"Student: {record.student_name}")
    print(f"Concept: {record.concept}")
    print(f"Similarity: {record.similarity:.2f}%")
    print("-" * 60)

db.close()