#!/bin/bash

# This script demonstrates some popular GitHub CLI (gh) commands.

echo "--- Listing GitHub Repositories (first 5) ---"
gh repo list --limit 5

echo "\n--- Listing GitHub Issues (first 5, open) ---"
gh issue list --limit 5 --state open

echo "\n--- Listing GitHub Pull Requests (first 5, open) ---"
gh pr list --limit 5 --state open

echo "\n--- Showing authenticated GitHub user ---"
gh auth status

echo "\n--- Getting details of a specific repository (e.g., cli/cli) ---"
gh repo view cli/cli

