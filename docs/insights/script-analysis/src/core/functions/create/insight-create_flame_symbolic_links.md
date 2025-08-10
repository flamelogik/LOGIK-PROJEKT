# Insight: `create_flame_symbolic_links.py`

## 1. Module Type

`create_flame_symbolic_links.py` is a Python utility module. It provides a function for establishing symbolic links between various LOGIK-PROJEKT directories and specific locations within a newly created Autodesk Flame project's setup structure.

## 2. Purpose

The primary purpose of this module is to integrate LOGIK-PROJEKT's shared resources (like scripts, presets, and templates) directly into the Flame project environment using symbolic links. This allows Flame to access these resources as if they were local to the project, promoting consistency and ease of management. It also creates a symbolic link for iteration directories and a reverse link from the Flame setups directory back to the LOGIK-PROJEKT structure for easy access.

## 3. Behavior and Functionality

- **Symbolic Link Creation:** The core functionality is to create `os.symlink` (symbolic links) from source directories (within LOGIK-PROJEKT) to target directories (within the Flame project setups).
- **Link Types:** It creates several types of links:
  - Links for `scripts`, `flame-presets`, and `flame-templates` from LOGIK-PROJEKT into the Flame project's setups directory.
  - A link for `logik_projekt_path/flame/iterations` to `flame_projekt_setups_dir/batch/flame/iterations`.
  - A reverse link from `flame_projekt_setups_dir` back to `logik_projekt_path/flame/setups/{current_workstation}/setups`.
- **Idempotency and Safety Checks:** Before creating a link, it checks:
  - If the source path exists.
  - If the destination path already exists and is a symbolic link pointing to the correct source. If it's a correct link, it logs that it already exists. If it's an existing file/directory or a broken/incorrect symlink, it logs a warning and skips creation to prevent overwriting or errors.
- **Directory Creation:** It ensures that the parent directories for the destination links exist before attempting to create the symlink.
- **Retry Mechanism:** For the `flame_projekt_setups_dir` reverse link, it includes a retry mechanism with a small delay, suggesting that the target directory might not be immediately available after creation by other processes.
- **Logging:** It uses the `logging` module extensively to provide detailed information about each symlink operation, including creation, existing links, warnings for skipped links, and errors.

## 4. Key Functions

- `create_flame_symbolic_links(logik_projekt_path: str, flame_projekt_setups_dir: str, current_workstation: str)`:
  - Purpose: Orchestrates the creation of all specified symbolic links.
  - Arguments: `logik_projekt_path` (absolute path to the LOGIK-PROJEKT root), `flame_projekt_setups_dir` (absolute path to the new Flame project's setups directory), `current_workstation` (name of the current workstation).
  - Behavior: Iterates through predefined link pairs, performs checks, creates symlinks, and logs the process.

## 5. Signals and Slots

This module is a pure utility module and does not interact with PySide6. Therefore, it does not define or use any signals or slots.

## 6. Dependencies and Relationships

- **Standard Python Libraries:** `os`, `logging`, `time`.
- **`src.core.utils.path_utils`:** Imports `path_utils.get_repository_root_dir()` to correctly resolve source paths relative to the project root.
- **Relationship to Project Creation Workflow:** This script is a critical step in the overall project creation process (e.g., called by `projekt_creator.py`). It establishes the necessary connections between the LOGIK-PROJEKT repository and the newly created Flame project, making shared resources accessible.
- **Operating System:** Relies on the operating system's support for symbolic links (`os.symlink`, `os.path.islink`, `os.readlink`). This implies it's primarily designed for Unix-like systems (Linux, macOS).

## 7. Other Useful Information

- **Resource Sharing:** Symbolic links are an efficient way to share common resources across multiple projects without duplicating data, saving disk space and simplifying updates.
- **Workflow Integration:** By linking LOGIK-PROJEKT resources directly into the Flame project structure, it seamlessly integrates custom tools and configurations into the artist's workflow.
- **Debugging:** The detailed logging helps in diagnosing issues related to symbolic link creation, which can sometimes be tricky due to permissions or existing files.
- **Robustness:** The checks for existing links and the retry mechanism contribute to the script's robustness, allowing it to be run multiple times without causing errors or unintended side effects.