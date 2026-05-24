#!/usr/bin/env python3
"""
GitHub API wrapper for issue-triage.
Handles fetching issues, applying labels, and posting comments.
"""

import requests
from typing import List, Dict, Optional


class GitHubAPI:
    """Wrapper for GitHub API interactions."""

    def __init__(self, token: str, repo: str):
        """
        Initialize GitHub API wrapper.
        
        Args:
            token (str): GitHub personal access token.
            repo (str): Repository in format "owner/repo".
        """
        self.token = token
        self.repo = repo
        self.base_url = f"https://api.github.com/repos/{repo}"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
        }

    def fetch_open_issues(self) -> List[Dict]:
        """Fetch all open issues from the repository."""
        url = f"{self.base_url}/issues?state=open"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def apply_label(self, issue_number: int, labels: List[str]) -> bool:
        """Apply labels to an issue."""
        url = f"{self.base_url}/issues/{issue_number}/labels"
        response = requests.post(url, headers=self.headers, json=labels)
        return response.status_code == 200

    def post_comment(self, issue_number: int, comment: str) -> bool:
        """Post a comment on an issue."""
        url = f"{self.base_url}/issues/{issue_number}/comments"
        response = requests.post(url, headers=self.headers, json={"body": comment})
        return response.status_code == 201

    def get_issue(self, issue_number: int) -> Dict:
        """Get details of a specific issue."""
        url = f"{self.base_url}/issues/{issue_number}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()