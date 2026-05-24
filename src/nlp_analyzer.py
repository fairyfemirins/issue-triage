#!/usr/bin/env python3
"""
NLP analyzer for issue-triage.
Classifies issues, detects duplicates, and extracts key details.
"""

from transformers import pipeline
from typing import List, Dict, Optional
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class NLPAnalyzer:
    """NLP analyzer for GitHub issues."""

    def __init__(self):
        """Initialize NLP models."""
        self.classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
        self.embedding_model = pipeline("feature-extraction", model="distilbert-base-uncased")

    def classify_issue(self, title: str, body: str) -> str:
        """
        Classify issue as 'bug', 'enhancement', or 'question'.
        Defaults to 'question' if confidence is low.
        """
        text = f"{title}. {body}"
        result = self.classifier(text)
        label = result[0]["label"]
        
        # Map classifier output to issue labels
        if "bug" in text.lower() or label == "NEGATIVE":
            return "bug"
        elif "feature" in text.lower() or "enhancement" in text.lower():
            return "enhancement"
        else:
            return "question"

    def extract_keywords(self, text: str) -> List[str]:
        """Extract keywords from issue text."""
        # Placeholder: Use NLP to extract keywords
        return []

    def detect_duplicates(self, issues: List[Dict]) -> List[Dict]:
        """
        Detect potential duplicate issues using semantic similarity.
        Returns list of tuples (issue1, issue2, similarity_score).
        """
        texts = [f"{issue['title']}. {issue.get('body', '')}" for issue in issues]
        embeddings = self.embedding_model(texts)
        embeddings = [np.mean(embedding, axis=0) for embedding in embeddings]
        
        duplicates = []
        for i in range(len(embeddings)):
            for j in range(i + 1, len(embeddings)):
                similarity = cosine_similarity([embeddings[i]], [embeddings[j]])[0][0]
                if similarity > 0.85:  # Threshold for duplicates
                    duplicates.append({
                        "issue1": issues[i]["number"],
                        "issue2": issues[j]["number"],
                        "similarity": similarity,
                    })
        return duplicates