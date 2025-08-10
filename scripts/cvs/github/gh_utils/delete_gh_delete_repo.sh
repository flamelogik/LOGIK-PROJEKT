#!/bin/bash

# DELETE_gh_delete_repo.sh
# Deletes a GitHub repository.
# Corresponds to a DELETE operation in REST, as it removes a resource.

# Usage: ./DELETE_gh_delete_repo.sh <owner/repo>

REPO_NAME="$1"

if [ -z "$REPO_NAME" ]; then
  echo "Usage: $0 <owner/repo>"
  exit 1
fi

echo "Deleting repository $REPO_NAME... This action is irreversible!"
gh repo delete "$REPO_NAME" --confirm

if [ $? -eq 0 ]; then
  echo "Repository $REPO_NAME deleted successfully."
else
  echo "Failed to delete repository $REPO_NAME."
fi
