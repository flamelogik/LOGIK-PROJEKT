#!/bin/bash

# PATCH_gh_close_issue.sh
# Closes a GitHub issue.
# Corresponds to a PATCH operation in REST, as it performs a partial update to the resource's state.

# Usage: ./PATCH_gh_close_issue.sh <issue-number>

ISSUE_NUMBER="$1"

if [ -z "$ISSUE_NUMBER" ]; then
  echo "Usage: $0 <issue-number>"
  exit 1
fi

echo "Closing issue #$ISSUE_NUMBER..."
gh issue close "$ISSUE_NUMBER"

if [ $? -eq 0 ]; then
  echo "Issue #$ISSUE_NUMBER closed successfully."
else
  echo "Failed to close issue #$ISSUE_NUMBER."
fi
