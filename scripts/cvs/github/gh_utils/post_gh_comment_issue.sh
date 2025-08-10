#!/bin/bash

# POST_gh_comment_issue.sh
# Adds a comment to a GitHub issue.
# Corresponds to a POST operation in REST, as it creates a new sub-resource (a comment) on an existing resource.

# Usage: ./POST_gh_comment_issue.sh <issue-number> "Your comment here"

ISSUE_NUMBER="$1"
COMMENT_BODY="$2"

if [ -z "$ISSUE_NUMBER" ] || [ -z "$COMMENT_BODY" ]; then
  echo "Usage: $0 <issue-number> \"Your comment here\""
  exit 1
fi

echo "Adding comment to issue #$ISSUE_NUMBER..."
gh issue comment "$ISSUE_NUMBER" --body "$COMMENT_BODY"

if [ $? -eq 0 ]; then
  echo "Comment added successfully to issue #$ISSUE_NUMBER."
else
  echo "Failed to add comment to issue #$ISSUE_NUMBER."
fi

