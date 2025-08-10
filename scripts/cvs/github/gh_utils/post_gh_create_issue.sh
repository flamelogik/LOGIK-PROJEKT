#!/bin/bash

# POST_gh_create_issue.sh
# Creates a new GitHub issue.
# Corresponds to a POST operation in REST, as it creates a new resource.

# Usage: ./POST_gh_create_issue.sh "Issue Title" "Issue Body"

ISSUE_TITLE="$1"
ISSUE_BODY="$2"

if [ -z "$ISSUE_TITLE" ]; then
  echo "Usage: $0 \"Issue Title\" [\"Issue Body\"]"
  exit 1
fi

gh issue create --title "$ISSUE_TITLE" --body "$ISSUE_BODY"

if [ $? -eq 0 ]; then
  echo "Issue created successfully."
else
  echo "Failed to create issue."
fi

