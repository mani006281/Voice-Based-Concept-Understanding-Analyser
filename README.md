# 🎤 Voice-Based Concept Understanding Analyser

> An AI-powered system that evaluates a student's conceptual understanding from voice explanations using Speech-to-Text, Semantic Similarity Analysis, and Google Gemini AI.

---
# Demo link

https://drive.google.com/file/d/1XJV4o_8Oq670-tRmO0tpXm5ypKoNKZ-j/view


# 📌 Project Overview

The **Voice-Based Concept Understanding Analyser** is an AI-powered educational application developed as part of the **SmartBridge Internship**.

The system allows students to explain concepts using their voice. The uploaded audio is converted into text using **OpenAI Whisper**, compared with the reference answer using **Sentence Transformers**, and evaluated using **Google Gemini AI**.

The application generates intelligent feedback, calculates semantic similarity, stores evaluation history in a SQLite database, and generates downloadable PDF reports.

---

# 🎯 Objectives

- Convert student voice explanations into text.
- Evaluate conceptual understanding using AI.
- Generate semantic similarity scores.
- Provide AI-generated personalized feedback.
- Store evaluation history.
- Generate downloadable evaluation reports.

---

# ✨ Features

- 🎤 Voice Upload
- 📝 Speech-to-Text using OpenAI Whisper
- 🧠 Semantic Similarity Analysis
- 🤖 AI Feedback using Google Gemini
- 📊 Similarity Score
- 👤 Student Name Input
- 📄 PDF Report Generation
- 📚 Evaluation History
- 📈 Dashboard with Analytics
- 💾 SQLite Database Storage
- 🌐 Multi-Page Streamlit Interface

---

# 🏗 System Workflow

```text
Student
     │
     ▼
Upload Voice
     │
     ▼
OpenAI Whisper
(Speech → Text)
     │
     ▼
Reference Concept
     │
     ▼
Semantic Similarity
(Sentence Transformers)
     │
     ▼
Google Gemini AI
     │
     ▼
AI Feedback
     │
     ▼
SQLite Database
     │
     ▼
Dashboard + History + PDF Report
```

---

# 🛠 Technology Stack

## Programming Language

- Python

## Frontend

- Streamlit

## Backend

- Python

## Artificial Intelligence

- OpenAI Whisper
- Google Gemini AI
- Sentence Transformers

## Database

- SQLite
- SQLAlchemy ORM

## PDF Generation

- ReportLab

## Data Analysis

- Pandas

## Visualization

- Matplotlib

---

# 📂 Project Structure

```
Voice-Based-Concept-Understanding-Analyser/

│── backend/
│── frontend/
│── database/
│── reports/
│── uploads/
│── data/
│── models/
│── utils/
│── static/
│── requirements.txt
│── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/mani006281/Voice-Based-Concept-Understanding-Analyser.git
```

Move into the project directory.

```bash
cd Voice-Based-Concept-Understanding-Analyser
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install Requirements

```bash
pip install -r requirements.txt
```

Run Application

```bash
streamlit run frontend/streamlit_app.py
```

---

# 📊 Modules

### Module 1

Speech Recognition

- Upload Voice
- Convert Voice into Text

---

### Module 2

Semantic Analysis

- Compare Student Answer
- Calculate Similarity Score

---

### Module 3

AI Feedback

- Concept Understanding
- Strengths
- Missing Concepts
- Suggestions

---

### Module 4

Database

- Save Evaluation
- Store Student History

---

### Module 5

Reports

- Generate PDF
- Download Evaluation Report

---

### Module 6

Dashboard

- Total Evaluations
- Highest Score
- Average Score
- Student Statistics
- Charts

---

# 📸 Screenshots

Add screenshots here:

- Home Page
- Evaluation Result
- Dashboard
- History
- PDF Report

---

# 🎯 Future Enhancements

- Live Voice Recording
- Authentication System
- Teacher Dashboard
- Cloud Database
- Mobile Responsive UI
- Email Report Generation
- Multi-language Support
- Performance Analytics

---

# 👨‍💻 Team Details

**Project**

Voice-Based Concept Understanding Analyser

**Developed For**

SmartBridge Internship

**Team Size**

5 Members

**Team Leader**

Penugonda Mani Kumar

**Team Members**
1.Penugonda Mani Kumar(Team Led)
2.Koppula Dilip kumar
3.Boddu Joshitha
4.Donda Bhavani
5.Chimmili Lakshmi Lavanya

**College**

GIET Engineering College

**Department**

Information Technology

---

# 📌 GitHub Repository

https://github.com/mani006281/Voice-Based-Concept-Understanding-Analyser

---

# ⭐ Acknowledgements

- SmartBridge
- GIET Engineering College
- OpenAI Whisper
- Google Gemini AI
- Streamlit
- Sentence Transformers
- SQLAlchemy
- ReportLab

---

# 📄 License

This project was developed for educational purposes as part of the SmartBridge Internship Program.
