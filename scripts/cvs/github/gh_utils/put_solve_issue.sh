#!/bin/bash

# put_solve_issue.sh
# Automates the process of pushing an issue branch, creating a PR, merging it,
# and cleaning up branches.

# Function to get the current repository name (owner/repo) from git remote
get_repo_name() {
    local remote_url=$(git remote get-url origin 2>/dev/null)
    if [ -z "$remote_url" ]; then
        echo ""
        return
    fi

    # Extract owner/repo from the URL
    # Handles both https://github.com/owner/repo.git and git@github.com:owner/repo.git
    echo "$remote_url" | sed -E 's/.*github.com[/:]([^/]+)\/([^.]+)(\.git)?/\1\/\2/'
}

REPO_NAME=$(get_repo_name)

# Function to display help message
display_help() {
    echo "Usage: $0 <issue-number> [--help]"
    echo ""
    echo "Automates the process of pushing an an issue branch, creating a Pull Request,"
    echo "merging it into the main branch, and cleaning up the branches."
    echo ""
    echo "Arguments:"
    echo "  <issue-number> The number of the GitHub issue to solve."
    echo ""
    echo "Flags:"
    echo "  -h, --help     Display this help message."
    echo "\nExamples:"
    echo "  $0 123"
}

# Parse command-line arguments
ISSUE_NUMBER=""

if [[ "$#" -eq 0 ]]; then
    display_help
    exit 1
fi

while (( "$#" )); do
    case "$1" in
        -h|--help)
            display_help
            ;;
        *)
            ISSUE_NUMBER="$1"
            shift
            ;;
    esac
done

if [ -z "$ISSUE_NUMBER" ]; then
    echo "Error: Issue number is required." >&2
    display_help
    exit 1
fi

BRANCH_NAME="gh-task-${ISSUE_NUMBER}"
MAIN_BRANCH="main"

# Validate REPO_NAME
if [ -z "$REPO_NAME" ]; then
    echo "Error: Could not determine repository name from git remote. Ensure you are in a Git repository with a configured 'origin' remote." >&2
    exit 1
fi
echo "Operating on repository: $REPO_NAME"

# Check for jq dependency
if ! command -v jq &> /dev/null
then
    echo "Error: jq is not installed. Please install jq to use this script." >&2
    exit 1
fi

# Construct the full repository URL
FULL_REPO_URL="https://github.com/$REPO_NAME"
echo "Using full repository URL: $FULL_REPO_URL"

# 1. Ensure current branch is the issue branch
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$CURRENT_BRANCH" != "$BRANCH_NAME" ]; then
    echo "Error: You are currently on branch '$CURRENT_BRANCH'. Please switch to '$BRANCH_NAME' to solve the issue." >&2
    exit 1
fi

# 2. Push the current branch to remote
echo "Pushing branch '$BRANCH_NAME' to remote..."
git push origin "$BRANCH_NAME"
if [ $? -ne 0 ]; then
    echo "Error: Failed to push branch to remote." >&2
    exit 1
fi

# 3. Create a Pull Request
echo "Creating Pull Request for '$BRANCH_NAME'..."
PR_URL=$(gh pr create --repo "$FULL_REPO_URL" --base "$MAIN_BRANCH" --head "$BRANCH_NAME" --title "Fix/Feat: gh-task-${ISSUE_NUMBER}" --body "Closes #${ISSUE_NUMBER}" --fill --json url -t "Fix/Feat: gh-task-${ISSUE_NUMBER}" | jq -r '.url')

if [ $? -ne 0 ]; then
    echo "Error: Failed to create Pull Request." >&2
    exit 1
fi
echo "Pull Request created: $PR_URL"

# 4. Merge the Pull Request
echo "Merging Pull Request..."
gh pr merge "$BRANCH_NAME" --repo "$FULL_REPO_URL" --squash --delete-branch --auto

if [ $? -ne 0 ]; then
    echo "Error: Failed to merge Pull Request." >&2
    exit 1
fi
echo "Pull Request merged successfully."

# 5. Switch back to main branch
echo "Switching back to '$MAIN_BRANCH' branch..."
git checkout "$MAIN_BRANCH"
if [ $? -ne 0 ]; then
    echo "Error: Failed to switch back to '$MAIN_BRANCH' branch." >&2
    exit 1
fi

# 6. Pull latest changes on main
echo "Pulling latest changes on '$MAIN_BRANCH'..."
git pull origin "$MAIN_BRANCH"
if [ $? -ne 0 ]; then
    echo "Error: Failed to pull latest changes on '$MAIN_BRANCH'." >&2
    exit 1
fi

echo "Workflow completed for issue #$ISSUE_NUMBER."