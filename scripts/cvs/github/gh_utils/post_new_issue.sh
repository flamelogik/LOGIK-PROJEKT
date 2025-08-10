#!/bin/bash

# post_new_issue.sh
# Creates a new GitHub issue with specified title and body.
# Allows choosing between GitHub or OS identity for the task.

GH_UTILS_DIR="$(dirname "$0")"
GET_USERNAME_SCRIPT="${GH_UTILS_DIR}/get_username.sh"

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
    echo "Usage: $0 --title \"<Issue Title>\" --body \"<Issue Body>\" [--identity <github|os>]"
    echo ""
    echo "Creates a new GitHub issue with the given title and body."
    echo ""
    echo "Flags:"
    echo "  -t, --title    The title of the GitHub issue (required)."
    echo "  -b, --body     The body/description of the GitHub issue (required)."
    echo "  -i, --identity Choose the identity for this task. Options: 'github' (default, if logged in) or 'os'."
    echo "  -h, --help     Display this help message."
    echo "\nExamples:"
    echo "  $0 --title \"Fix login bug\" --body \"Users cannot log in after update.\""
    echo "  $0 -t \"New Feature\" -b \"Implement dark mode.\" --identity github"
    echo "  $0 --title \"Documentation Update\" --body \"Add README for new module.\" --identity os"
    exit 0
}

# Parse command-line arguments
ISSUE_TITLE=""
ISSUE_BODY=""
IDENTITY_CHOICE=""

while (( "$#" )); do
    case "$1" in
        -t|--title)
            if [ -n "$2" ] && [ "${2:0:1}" != "-" ]; then
                ISSUE_TITLE="$2"
                shift 2
            else
                echo "Error: Argument for $1 is missing." >&2
                exit 1
            fi
            ;;
        -b|--body)
            if [ -n "$2" ] && [ "${2:0:1}" != "-" ]; then
                ISSUE_BODY="$2"
                shift 2
            else
                echo "Error: Argument for $1 is missing." >&2
                exit 1
            fi
            ;;
        -i|--identity)
            if [ -n "$2" ] && [ "${2:0:1}" != "-" ]; then
                IDENTITY_CHOICE="$2"
                shift 2
            else
                echo "Error: Argument for $1 is missing." >&2
                exit 1
            fi
            ;;
        -h|--help)
            display_help
            ;;
        -*|--*=)
            echo "Error: Unsupported flag $1" >&2
            display_help
            ;;
        *)
            echo "Error: Unexpected argument $1" >&2
            display_help
            ;;
    esac
done

# Validate required arguments
if [ -z "$ISSUE_TITLE" ] || [ -z "$ISSUE_BODY" ]; then
    echo "Error: --title and --body are required." >&2
    display_help
fi

# Check if get_username.sh exists and is executable
if [ ! -x "$GET_USERNAME_SCRIPT" ]; then
    echo "Error: ${GET_USERNAME_SCRIPT} not found or not executable. Please ensure it exists and has execute permissions." >&2
    exit 1
fi

# Get both GitHub and OS usernames
# Use a temporary file to capture output to avoid issues with multiple lines
TEMP_USERNAME_FILE=$(mktemp)
"$GET_USERNAME_SCRIPT" > "$TEMP_USERNAME_FILE"
USERNAMES=$(cat "$TEMP_USERNAME_FILE")
rm "$TEMP_USERNAME_FILE"

GITHUB_USERNAME=$(echo "$USERNAMES" | head -n 1)
OS_USERNAME=$(echo "$USERNAMES" | tail -n 1)

USERNAME_TO_USE=""

case "$IDENTITY_CHOICE" in
    github)
        if [ -n "$GITHUB_USERNAME" ]; then
            USERNAME_TO_USE="$GITHUB_USERNAME"
        else
            echo "Error: GitHub identity requested, but not logged in to GitHub CLI." >&2
            exit 1
        fi
        ;;
    os)
        USERNAME_TO_USE="$OS_USERNAME"
        ;;
    "") # Default behavior if --identity is not specified
        if [ -n "$GITHUB_USERNAME" ]; then
            USERNAME_TO_USE="$GITHUB_USERNAME"
        else
            USERNAME_TO_USE="$OS_USERNAME"
        fi
        ;;
    *)
        echo "Error: Invalid identity choice '$IDENTITY_CHOICE'. Use 'github' or 'os'." >&2
        exit 1
        ;;
esac

# Check if a username is determined to proceed
if [ -z "$USERNAME_TO_USE" ]; then
    echo "Could not determine a username to proceed. Aborting." >&2
    exit 1
fi

echo "Proceeding with username: '$USERNAME_TO_USE'"

# Validate REPO_NAME
if [ -z "$REPO_NAME" ]; then
    echo "Error: Could not determine repository name from git remote. Ensure you are in a Git repository with a configured 'origin' remote." >&2
    exit 1
fi
echo "Operating on repository: $REPO_NAME"

# Construct the full repository URL
FULL_REPO_URL="https://github.com/$REPO_NAME"
echo "Using full repository URL: $FULL_REPO_URL"

# Create the GitHub issue and capture output
echo "Creating GitHub issue..."
ISSUE_OUTPUT=$(gh issue create --repo "$FULL_REPO_URL" --title "$ISSUE_TITLE" --body "$ISSUE_BODY" 2>&1)
GH_ISSUE_CREATE_EXIT_CODE=$?

if [ $GH_ISSUE_CREATE_EXIT_CODE -eq 0 ]; then
    # Parse the issue number and URL from the output
    ISSUE_URL=$(echo "$ISSUE_OUTPUT" | grep "https://github.com/" | awk '{print $1}')
    ISSUE_NUMBER=$(basename "$ISSUE_URL")

    echo "GitHub issue #$ISSUE_NUMBER created successfully: $ISSUE_URL"

    # Construct branch name
    BRANCH_NAME="gh-task-${ISSUE_NUMBER}"

    # Create and checkout branch
    echo "Creating and checking out new branch: $BRANCH_NAME"
    git checkout -b "$BRANCH_NAME"

    if [ $? -eq 0 ]; then
        echo "Successfully checked out branch $BRANCH_NAME."

        # Create task Markdown file
        TASK_FILE_PATH="/home/pman/workspace/GitHub/phil-man-git-hub/LOGIK-PROJEKT/tasks/gh-task-${ISSUE_NUMBER}.md"
        echo "Creating task documentation file: $TASK_FILE_PATH"
        cat << EOF > "$TASK_FILE_PATH"
# Task: $ISSUE_TITLE

**GitHub Issue:** [$ISSUE_URL]($ISSUE_URL)

## Description
$ISSUE_BODY

## Notes / Sub-tasks
- [ ]

EOF
        if [ $? -eq 0 ]; then
            echo "Task file created successfully."
        else
            echo "Failed to create task file." >&2
        fi

        # Prompt to open VSCode
        read -p "Do you want to open VSCode in the new branch? (yes/no): " open_vscode_choice
        if [[ "$open_vscode_choice" == "yes" ]]; then
            echo "Opening VSCode..."
            code /home/pman/workspace/GitHub/phil-man-git-hub/LOGIK-PROJEKT # Open the project root
        fi

    else
        echo "Failed to create and checkout branch $BRANCH_NAME." >&2
    fi

else
    echo "Failed to create GitHub issue." >&2
    echo "Error details: $ISSUE_OUTPUT" >&2
fi
