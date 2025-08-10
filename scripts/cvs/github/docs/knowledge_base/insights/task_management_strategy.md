# Task Management Strategy

This document outlines a strategy for managing tasks within the repository, integrating a `tasks` directory, a `tasks.md` file, and a `gh-task` numbering system.

## 1. The `tasks/` Directory:
*   **Purpose:** This directory will serve as a container for individual task-related files. For complex tasks, you might want to create a separate Markdown file (e.g., `tasks/gh-task-123-detailed-plan.md`) or even a sub-directory to hold more detailed notes, research, or specific sub-task breakdowns.
*   **Content:** Could include:
    *   Detailed task descriptions beyond what fits in a GitHub Issue.
    *   Research notes.
    *   Design decisions specific to a task.
    *   Checklists for sub-tasks.
    *   Temporary scripts or data related to a task.

## 2. The `tasks.md` File:
*   **Purpose:** This will be your central, high-level task registry. It provides a quick overview of all active, pending, or recently completed tasks. It acts as a "table of contents" for your tasks.
*   **Content:** A simple, structured list of tasks, ideally linking directly to their corresponding GitHub Issues and any detailed task files in the `tasks/` directory.
*   **Structure Suggestion:**

    ```markdown
    # Project Tasks

    This document lists all active and recently completed tasks for the project.
    Each task is linked to its corresponding GitHub Issue for detailed tracking and discussion.

    ## Active Tasks

    *   [gh-task-1: Implement User Authentication](https://github.com/your-org/your-repo/issues/1) - Assigned to @username
        *   [Detailed Plan](tasks/gh-task-1-detailed-plan.md)
    *   [gh-task-2: Refactor Database Schema](https://github.com/your-org/your-repo/issues/2) - Assigned to @anotheruser

    ## Completed Tasks (Last 30 days)

    *   [gh-task-120: Fix Login Bug](https://github.com/your-org/your-repo/issues/120) - Completed by @username (2025-07-10)
    *   [gh-task-119: Update Dependencies](https://github.com/your-org/your-repo/issues/119) - Completed by @anotheruser (2025-07-05)

    ## Backlog / Future Tasks

    *   [gh-task-3: Add Admin Dashboard](https://github.com/your-org/your-repo/issues/3)
    *   [gh-task-4: Improve Performance of API Endpoint](https://github.com/your-org/your-repo/issues/4)
    ```

## 3. The `gh-task` Numbering System:
*   **Concept:** This system directly leverages GitHub's existing issue numbering. A `gh-task-N` will correspond directly to GitHub Issue #N.
*   **Benefits:**
    *   **Simplicity:** No need for a separate, redundant numbering system.
    *   **Integration:** Seamlessly links your local task documentation with GitHub's powerful issue tracking features (discussions, labels, milestones, projects, etc.).
    *   **Traceability:** Easy to trace work from a local task file to its GitHub Issue, associated commits, and pull requests.
*   **Usage:**
    *   **Branch Names:** `fix/gh-task-123-login-bug` or `feat/gh-task-456-new-feature`.
    *   **Commit Messages:** `Fix: Login issue (fixes #123)` or `Feat: Added new feature (closes #456)`.
    *   **Local Task Files:** `tasks/gh-task-123-login-bug-details.md`.

## Initial Steps to Start:

1.  **Create the `tasks/` directory:**
    `mkdir -p /home/pman/workspace/GitHub/phil-man-git-hub/LOGIK-PROJEKT/tasks`
2.  **Create the `tasks.md` file:**
    `touch /home/pman/workspace/GitHub/phil-man-git-hub/LOGIK-PROJEKT/tasks.md`
3.  **Add the initial structure to `tasks.md`** (as suggested above).
