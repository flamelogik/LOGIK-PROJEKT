#!/bin/bash

# GET_gh_view_repo.sh
# Views details of a GitHub repository.
# Corresponds to a GET operation in REST, as it retrieves a specific resource.

# Usage: ./GET_gh_view_repo.sh <owner/repo>

REPO_NAME="$1"

if [ -z "$REPO_NAME" ]; then
  echo "Usage: $0 <owner/repo>"
  exit 1
fi

echo "Viewing repository $REPO_NAME..."
gh repo view "$REPO_NAME"

if [ $? -eq 0 ]; then
  echo "Repository details retrieved successfully."
else
  echo "Failed to retrieve repository details."
fi
