#!/usr/bin/env python3
"""
CLI for issue-triage.
Autonomously triage GitHub issues using AI.
"""

import click
from typing import Optional
from github_api import GitHubAPI
from nlp_analyzer import NLPAnalyzer


@click.command()
@click.option("--repo", required=True, help="GitHub repository in format 'owner/repo'")
@click.option("--token", required=True, help="GitHub personal access token")
@click.option("--dry-run", is_flag=True, help="Run without making changes")
def main(repo: str, token: str, dry_run: bool):
    """Autonomously triage GitHub issues."""
    github = GitHubAPI(token, repo)
    nlp = NLPAnalyzer()
    
    click.echo(f"Fetching open issues from {repo}...")
    issues = github.fetch_open_issues()
    
    for issue in issues:
        issue_number = issue["number"]
        title = issue["title"]
        body = issue.get("body", "")
        
        # Classify issue
        label = nlp.classify_issue(title, body)
        click.echo(f"Issue #{issue_number}: {title} -> {label}")
        
        # Apply label if not in dry-run mode
        if not dry_run:
            success = github.apply_label(issue_number, [label])
            if success:
                click.echo(f"Applied label '{label}' to issue #{issue_number}")
            else:
                click.echo(f"Failed to apply label to issue #{issue_number}")
    
    # Detect duplicates
    duplicates = nlp.detect_duplicates(issues)
    for dup in duplicates:
        click.echo(f"Potential duplicate: Issue #{dup['issue1']} and Issue #{dup['issue2']} (similarity: {dup['similarity']:.2f})")


if __name__ == "__main__":
    main()