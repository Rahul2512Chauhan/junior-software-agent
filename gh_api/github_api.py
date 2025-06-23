# gh_api/github_api.py

from github import Github  # ✅ from PyGithub
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = "Rahul2512Chauhan/junior-software-agent"  # 🔁 Replace with your actual repo

g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)


def get_open_issues():
    return repo.get_issues(state="open")


def label_issue(issue_number, label_name):
    issue = repo.get_issue(number=issue_number)
    issue.add_to_labels(label_name)
