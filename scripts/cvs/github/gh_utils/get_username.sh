#!/bin/bash

# get_username.sh
# Returns both the GitHub username (if logged in) and the local OS username.
# Output:
# Line 1: GitHub username (empty if not logged in)
# Line 2: Local OS username

# Function to get GitHub username
get_github_username() {
    local gh_status_output
    local github_username=""

    # Run gh auth status and capture both stdout and stderr
    gh_status_output=$(gh auth status 2>&1)
    local gh_status_exit_code=$?

    if [ $gh_status_exit_code -eq 0 ]; then
        # Use sed to extract the username which is between "account " and " (keyring)"
        github_username=$(echo "$gh_status_output" | sed -n 's/.*account \([^ ]*\) (keyring).*/\1/p')
    fi

    echo "$github_username"
}

# Function to get local system username
get_local_username() {
    whoami
}

# Output GitHub username (or empty string)
get_github_username

# Output local OS username
get_local_username
