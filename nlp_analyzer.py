#!/usr/bin/env python3
"""
Simplified NLP analyzer for issue-triage.
Uses rule-based classification instead of ML.
"""

from typing import List, Dict


class NLPAnalyzer:
    """Rule-based NLP analyzer for GitHub issues."""

    def classify_issue(self, title: str, body: str) -> str:
        """
        Classify issue as 'bug', 'enhancement', or 'question'.
        Uses keyword matching for simplicity.
        """
        text = f"{title}. {body}".lower()
        
        if "bug" in text or "error" in text or "crash" in text:
            return "bug"
        elif "feature" in text or "enhancement" in text or "improve" in text:
            return "enhancement"
        else:
            return "question"

    def detect_duplicates(self, issues: List[Dict]) -> List[Dict]:
        """
        Detect potential duplicates using title similarity.
        Returns list of tuples (issue1, issue2, similarity_score).
        """
        duplicates = []
        for i in range(len(issues)):
            for j in range(i + 1, len(issues)):
                title1 = issues[i]["title"].lower()
                title2 = issues[j]["title"].lower()
                similarity = len(set(title1.split()) & set(title2.split())) / max(len(set(title1.split())), 1)
                if similarity > 0.5:  # Threshold for duplicates
                    duplicates.append({
                        "issue1": issues[i]["number"],
                        "issue2": issues[j]["number"],
                        "similarity": similarity,
                    })
        return duplicates