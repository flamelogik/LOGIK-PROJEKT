# GitHub Issue Workflow

This document outlines a standard workflow for addressing problems or implementing features using GitHub Issues, ensuring that work is isolated and does not break existing functionality.

## Workflow Tasks:

1.  **Create a GitHub Issue:**
    *   **Purpose:** To formally document the problem, track its progress, and facilitate discussion.
    *   **Action:** Use `gh issue create` to open a new issue in your repository. Provide a clear title and a detailed description of the problem or feature request.

2.  **Create a New Branch for the Issue:**
    *   **Purpose:** To isolate your work on this specific problem from the main development line. This ensures that your changes don't break existing functionality while you're working on them.
    *   **Action:** Use `git checkout -b <branch-name>` (e.g., `git checkout -b fix/issue-123-bug-description` or `git checkout -b feat/new-feature-name`). It's good practice to include the issue number or a brief, descriptive name in the branch name.

3.  **Implement the Solution/Feature:**
    *   **Purpose:** Write the necessary code to fix the problem or implement the new feature.
    *   **Action:** Make your code changes in your local working directory within the newly created branch.

4.  **Commit Changes:**
    *   **Purpose:** To save your work incrementally and create a clear, traceable history of your changes.
    *   **Action:** Use `git add .` to stage your changes, and then `git commit -m "<Type>: <brief description> (<optional: fixes #<issue-number>>)"` to commit them. Referencing the issue number in the commit message (e.g., `fixes #123`) is a best practice as GitHub will automatically link the commit to the issue and can even close the issue when the pull request is merged.

5.  **Push the Branch to GitHub:**
    *   **Purpose:** To make your work visible on GitHub, allowing for collaboration, review, and continuous integration checks.
    *   **Action:** Use `git push -u origin <branch-name>`. The `-u` flag sets the upstream branch, so subsequent pushes from this branch can simply be `git push`.

6.  **Create a Pull Request (PR):**
    *   **Purpose:** To formally propose your changes for review and eventual merging into the main branch (or another target branch). This is where your team can review the code, suggest improvements, and ensure it meets quality standards.
    *   **Action:** Use `gh pr create`. The GitHub CLI will guide you through creating the PR, often pre-filling the title and description based on your branch name and commit messages. Ensure you link it to the issue you created in Task 1.

7.  **Review and Merge the Pull Request:**
    *   **Purpose:** To get feedback on your changes and integrate them into the main codebase.
    *   **Action:** Once the PR is approved by reviewers and passes any automated checks (like tests or linting), it can be merged into the target branch (e.g., `main`).

8.  **Delete the Branch (Optional but Recommended):**
    *   **Purpose:** To keep your repository clean and organized by removing branches that have already been merged.
    *   **Action:** After the PR is merged, you can delete the local branch with `git branch -d <branch-name>` and the remote branch with `git push origin --delete <branch-name>`. GitHub often offers to delete the branch automatically after merging a PR.
