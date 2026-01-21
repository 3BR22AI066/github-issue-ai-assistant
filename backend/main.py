from fastapi import FastAPI, Query
from backend.github_client import fetch_issue_data
from backend.llm_analyzer import analyze_issue_with_llm

app = FastAPI(title="AI-Powered GitHub Issue Assistant")

@app.get("/")
def root():
    return {"status": "Backend is running"}

@app.post("/analyze-issue")
def analyze_issue(
    repo_url: str = Query(...),
    issue_number: int = Query(...)
):
    issue_data = fetch_issue_data(repo_url, issue_number)
    return analyze_issue_with_llm(issue_data)
