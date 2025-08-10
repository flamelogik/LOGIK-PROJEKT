#!/bin/bash

# GET_gh_list_issues.sh
# Lists GitHub issues.
# Corresponds to a GET operation in REST, as it retrieves resources.

# Usage: ./GET_gh_list_issues.sh [state] [limit]
# Example: ./GET_gh_list_issues.sh open 10

ISSUE_STATE="${1:-open}" # Default to 'open' if not provided
ISSUE_LIMIT="${2:-5}"   # Default to 5 if not provided

echo "Listing ${ISSUE_LIMIT} ${ISSUE_STATE} issues..."
gh issue list --limit "$ISSUE_LIMIT" --state "$ISSUE_STATE"

if [ $? -eq 0 ]; then
  echo "Issue list retrieved successfully."
else
  echo "Failed to retrieve issue list."
fi
