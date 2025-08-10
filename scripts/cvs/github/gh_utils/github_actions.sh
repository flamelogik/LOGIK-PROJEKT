#!/bin/bash

# github_actions.sh
# Provides a numbered menu to activate various GitHub CLI (gh) utility scripts.

GH_UTILS_DIR="$(dirname "$0")"

function display_menu() {
    echo "\nGitHub Actions Menu:"
    echo "--------------------"
    echo "1. Create GitHub Issue (post_gh_create_issue.sh)"
    echo "2. List GitHub Issues (get_gh_list_issues.sh)"
    echo "3. Close GitHub Issue (patch_gh_close_issue.sh)"
    echo "4. Comment on GitHub Issue (post_gh_comment_issue.sh)"
    echo "5. Delete GitHub Repository (delete_gh_delete_repo.sh)"
    echo "6. View GitHub Repository (get_gh_view_repo.sh)"
    echo "7. Run Popular gh Commands (popular_gh_commands.sh)"
    echo "0. Exit"
    echo "--------------------"
}

function run_script() {
    local script_name="$1"
    shift
    local full_path="${GH_UTILS_DIR}/${script_name}"
    if [ -f "$full_path" ]; then
        echo "\n--- Running ${script_name} ---"
        "$full_path" "$@"
        echo "--- Finished ${script_name} ---"
    else
        echo "Error: Script ${script_name} not found at ${full_path}"
    fi
}

while true; do
    display_menu
    read -p "Enter your choice: " choice

    case $choice in
        1)
            read -p "Enter issue title: " title
            read -p "Enter issue body (optional): " body
            run_script "post_gh_create_issue.sh" "$title" "$body"
            ;;
        2)
            read -p "Enter issue state (open, closed, all - default: open): " state
            read -p "Enter limit (number - default: 5): " limit
            run_script "get_gh_list_issues.sh" "$state" "$limit"
            ;;
        3)
            read -p "Enter issue number to close: " issue_num
            run_script "patch_gh_close_issue.sh" "$issue_num"
            ;;
        4)
            read -p "Enter issue number to comment on: " issue_num
            read -p "Enter comment body: " comment_body
            run_script "post_gh_comment_issue.sh" "$issue_num" "$comment_body"
            ;;
        5)
            read -p "Enter repository name (owner/repo): " repo_name
            echo "WARNING: Deleting a repository is irreversible!"
            read -p "Are you sure you want to delete $repo_name? (yes/no): " confirm
            if [[ "$confirm" == "yes" ]]; then
                run_script "delete_gh_delete_repo.sh" "$repo_name"
            else
                echo "Repository deletion cancelled."
            fi
            ;;
        6)
            read -p "Enter repository name (owner/repo): " repo_name
            run_script "get_gh_view_repo.sh" "$repo_name"
            ;;
        7)
            run_script "popular_gh_commands.sh"
            ;;
        0)
            echo "Exiting. Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter a number from the menu."
            ;;
    esac
    read -p "Press Enter to continue..." # Pause after each action
done
