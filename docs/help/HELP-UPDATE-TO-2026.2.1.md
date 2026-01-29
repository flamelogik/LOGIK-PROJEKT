# LOGIK-PROJEKT: Help Guide - Update to LOGIK-PROJEKT 2026.2.1

**Last updated:** October 30, 2025

---

## What is release-2026.2.1?

`release-2026.2.1` is a stable branch of LOGIK-PROJEKT tested and verified to work with Autodesk Flame 2026.2.1.

It contains all necessary updates and documentation for this version.

No code changes are required for this update.

---

## If you have forked and renamed your repository, and renamed your main branch

If you have forked LOGIK-PROJEKT and renamed your repository and/or your main branch (for example, to `LOGIK-PROJEKT-HECAT/release-hecat`):

- Your renamed branch will NOT automatically receive updates from the upstream `release-2026.2.1` branch.
- To update your branch with the latest changes, you must manually fetch and merge or rebase from the upstream `release-2026.2.1` branch into your renamed branch.
- The branch name change only affects your workflow and does not impact the upstream repository or future releases.

---

## How do I update my fork or local copy?

- Backup your current LOGIK-PROJEKT directory

- Follow these four steps to update your fork or local copy:

1. This step ensures that your local repository is linked to and can download from the official LOGIK-PROJEKT repository.
   
    ```bash
    # Add the upstream repository:
    git remote add upstream https://github.com/flamelogik/LOGIK-PROJEKT.git
    ```

2. This downloads the latest changes from the official LOGIK-PROJEKT repository to your local machine.

    ```bash
    # Fetch the upstream repository:
    git fetch upstream
    ```

3. Switch to your working branch where you want to apply the updates (e.g., your renamed release branch).

    ```bash
    # Checkout your branch:
    git checkout release-hecat  # or your renamed branch: 'release-my-release'
    ```

4. Integrate the latest changes from the official release-2026.2.1 branch into your branch. Resolve any merge conflicts if prompted.

    ```bash
    # Merge the upstream branch into your branch:
    git merge upstream/release-2026.2.1
    ```
---

## What if I want to stay on an older version?

Updates to `release-2026.2.1` are optional unless you need compatibility with Autodesk Flame 2026.2.1.
