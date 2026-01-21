import json
import os
import re
from huggingface_hub import InferenceClient

client = InferenceClient(
    model="google/flan-t5-large",
    token=os.getenv("HF_TOKEN")
)

def extract_json(text: str):
    """
    Extract first JSON object from text using regex.
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return json.loads(match.group())
    raise ValueError("No JSON found")

def analyze_issue_with_llm(issue_data: dict):
    """
    Deterministic AI-style analysis (LLM-safe fallback).
    """

    title = issue_data.get("title", "").lower()
    body = issue_data.get("body", "").lower()
    comments = " ".join(issue_data.get("comments", [])).lower()

    text = f"{title} {body} {comments}"

    # ---- TYPE HEURISTIC ----
    if any(k in text for k in ["bug", "error", "crash", "fails", "broken"]):
        issue_type = "bug"
        priority = "4"
    elif any(k in text for k in ["feature", "enhancement", "support", "add"]):
        issue_type = "feature_request"
        priority = "3"
    elif any(k in text for k in ["doc", "documentation", "readme"]):
        issue_type = "documentation"
        priority = "2"
    elif any(k in text for k in ["how", "why", "what", "question"]):
        issue_type = "question"
        priority = "2"
    else:
        issue_type = "other"
        priority = "1"

    # ---- LABELS ----
    labels = []
    if "test" in text:
        labels.append("testing")
    if "performance" in text:
        labels.append("performance")
    if "ui" in text:
        labels.append("ui")
    if not labels:
        labels = ["needs-triage"]

    return {
        "summary": issue_data.get("title", "GitHub issue analysis"),
        "type": issue_type,
        "priority_score": priority,
        "suggested_labels": labels,
        "potential_impact": "May affect users depending on usage and severity"
    }
