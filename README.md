# issue-triage
**Autonomous GitHub Issue Triage Assistant**

An open-source CLI tool to autonomously triage, label, and prioritize GitHub issues using AI.

## Problem Statement
Open-source maintainers and developers often struggle with managing and triaging GitHub issues. Issues can be:
- Poorly labeled or unlabeled.
- Missing critical information (e.g., reproduction steps, environment details).
- Duplicates or spam.
- Unprioritized, leading to delays in addressing critical bugs.

`issue-triage` automates this process, saving maintainers time and improving project health.

## Features
- **Fetch Open Issues**: Retrieve all open issues from a GitHub repository.
- **Classify Issues**: Automatically label issues as `bug`, `enhancement`, or `question`.
- **Detect Duplicates**: Identify potential duplicate issues using title similarity.
- **Dry-Run Mode**: Test the tool without making changes to GitHub.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/femirins/issue-triage.git
   cd issue-triage
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the tool in dry-run mode:
```bash
python3 main.py --repo "owner/repo" --token "your_github_token" --dry-run
```

To apply changes to GitHub:
```bash
python3 main.py --repo "owner/repo" --token "your_github_token"
```

## Technical Architecture
### Overview
`issue-triage` consists of three main components:
1. **GitHub API Wrapper** (`github_api.py`): Handles interactions with the GitHub API (fetching issues, applying labels, posting comments).
2. **NLP Analyzer** (`nlp_analyzer.py`): Classifies issues and detects duplicates using rule-based matching.
3. **CLI** (`cli.py`): Provides a command-line interface for users to interact with the tool.

### Workflow
1. **Fetch Issues**: The tool retrieves all open issues from the specified repository.
2. **Classify Issues**: Each issue is classified as `bug`, `enhancement`, or `question` based on its title and body.
3. **Detect Duplicates**: The tool identifies potential duplicate issues using title similarity.
4. **Apply Labels**: Labels are applied to issues (unless in dry-run mode).

### Future Enhancements
- **Machine Learning**: Replace the rule-based classifier with a fine-tuned NLP model.
- **GitLab/Bitbucket Support**: Extend the tool to support other issue trackers.
- **Automated Comments**: Post comments on issues to request missing information.

## License
This project is licensed under the **MIT License**.