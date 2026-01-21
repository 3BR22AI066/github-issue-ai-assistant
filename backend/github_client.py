import os
import requests

GITHUB_API = "https://api.github.com"

def fetch_issue_data(repo_url: str, issue_number: int):
    try:
        owner, repo = repo_url.rstrip("/").split("/")[-2:]

        headers = {}
        if os.getenv("GITHUB_TOKEN"):
            headers["Authorization"] = f"token {os.getenv('GITHUB_TOKEN')}"

        issue_resp = requests.get(
            f"{GITHUB_API}/repos/{owner}/{repo}/issues/{issue_number}",
            headers=headers
        )

        if issue_resp.status_code != 200:
            return None

        issue = issue_resp.json()

        comments_resp = requests.get(
            issue["comments_url"],
            headers=headers
        )

        comments = []
        if comments_resp.status_code == 200:
            comments = [c["body"] for c in comments_resp.json()]

        return {
            "title": issue.get("title", ""),
            "body": issue.get("body", ""),
            "comments": comments
        }

    except Exception:
        return None
