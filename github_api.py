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
        """Fetch all open issues from the repository. Mock response for testing."""
        # Mock response for testing
        return [
            {
                "number": 1,
                "title": "Bug: Application crashes on startup",
                "body": "The application crashes immediately after launch.",
            },
            {
                "number": 2,
                "title": "Feature request: Add dark mode",
                "body": "Please add a dark mode option to the settings.",
            },
            {
                "number": 3,
                "title": "Question: How to configure the API?",
                "body": "I'm having trouble configuring the API. Can someone help?",
            },
        ]

    def apply_label(self, issue_number: int, labels: List[str]) -> bool:
        """Apply labels to an issue. Mock response for testing."""
        print(f"[DRY RUN] Applied labels {labels} to issue #{issue_number}")
        return True

    def post_comment(self, issue_number: int, comment: str) -> bool:
        """Post a comment on an issue. Mock response for testing."""
        print(f"[DRY RUN] Posted comment on issue #{issue_number}: {comment}")
        return True

    def get_issue(self, issue_number: int) -> Dict:
        """Get details of a specific issue. Mock response for testing."""
        return {
            "number": issue_number,
            "title": "Mock Issue",
            "body": "This is a mock issue for testing.",
        }