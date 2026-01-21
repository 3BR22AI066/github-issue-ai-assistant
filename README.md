###🤖 AI-Powered GitHub Issue Assistant

Turn GitHub issues into structured, actionable insights using an AI-native, API-first architecture.

This project demonstrates how developer issues can be automatically analyzed to extract summaries, issue type, priority, labels, and potential impact — enabling faster triage and better product decision-making.

##🚀 Features

🔍 Analyze any public GitHub issue by repository URL & issue number

🧠 Generate structured insights:

Summary

Issue type (bug / documentation / enhancement / other)

Priority score

Suggested labels

Potential impact

⚡ FastAPI backend with clean REST interface

🎨 Lightweight Streamlit frontend for rapid MVP demonstration

🛡️ Stable, deterministic reasoning (no flaky external LLM dependencies)

##🧩 Architecture Overview

Frontend (Streamlit)
        |
        v
Backend API (FastAPI)
        |
        v
GitHub REST API  →  Issue Analyzer (LLM-style reasoning layer)

The system is intentionally designed with a decoupled reasoning layer, allowing future integration of live LLM providers without changing the API contract.

##📁 Project Structure

github-issue-ai-assistant/
│
├── backend/
│   ├── main.py              # FastAPI app & API routes
│   ├── github_client.py     # GitHub issue fetch logic
│   ├── llm_analyzer.py      # Structured issue analysis logic
│
├── frontend/
│   └── app.py               # Streamlit UI
│
├── requirements.txt
└── README.md

##🛠️ Tech Stack

Backend: FastAPI, Requests

Frontend: Streamlit

APIs: GitHub REST API

Language: Python 3.10+

Architecture Style: API-first, AI-native MVP

###How to Run Locally
##1️⃣ Clone the Repository
git clone <your-github-repo-url>
cd github-issue-ai-assistant

##How to Run Locally
1️⃣ Clone the Repository
git clone <your-github-repo-url>
cd github-issue-ai-assistant

##3️⃣ Start Backend (FastAPI)
cd backend
uvicorn main:app --reload
Verify backend:

http://127.0.0.1:8000/docs

##4️⃣ Start Frontend (Streamlit)

Open a new terminal:

cd frontend
streamlit run app.py

###📌 Example Usage

Repository URL:
https://github.com/facebook/react

Issue Number:
1

##Output:

{
  "summary": "Run each test in its own iframe",
  "type": "documentation",
  "priority_score": "2",
  "suggested_labels": ["testing", "ui"],
  "potential_impact": "May affect users depending on usage and severity"
}