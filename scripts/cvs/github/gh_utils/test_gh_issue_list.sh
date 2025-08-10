#!/bin/bash

# test_gh_issue_list.sh
# Simple script to test gh issue list functionality.

REPO_NAME="$(git remote get-url origin | sed -E 's/.*github.com[/:]([^/]+)\/([^.]+)(\.git)?/\1\/\2/')"

if [ -z "$REPO_NAME" ]; then
    echo "Error: Could not determine repository name." >&2
    exit 1
fi

echo "Attempting to list issues for repository: $REPO_NAME"

# Try listing issues with explicit --repo
gh issue list --repo "$REPO_NAME"

if [ $? -eq 0 ]; then
    echo "gh issue list successful."
else
    echo "gh issue list failed." >&2
fi
