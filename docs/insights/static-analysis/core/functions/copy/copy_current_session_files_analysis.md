# Static Analysis: `src/core/functions/copy/copy_current_session_files.py`

## Overview
The `copy_current_session_files.py` script defines a function to copy current session-related files, including preferences and logs, to a specified project directory. It uses `rsync` for directory synchronization and `shutil.copy` for individual file copying.

## Dependencies
- **Python Standard Library**: `os`, `logging`, `sys`, `shutil`, `glob`, `pathlib`
- **Local Modules (src.core.functions.get)**:
    - `src.core.functions.get.get_application_paths.GetApplicationPaths`
- **Local Modules (src.core.utils)**:
    - `src.core.utils.path_utils.get_repository_root_dir`

## Function: `copy_current_session_files(logik_projekt_path: str, current_workstation: str)`

### Purpose
To copy session-specific files and the latest session log to a designated project log directory.

### Arguments
- `logik_projekt_path` (str): The absolute path to the LOGIK-PROJEKT's root directory.
- `current_workstation` (str): The name of the current workstation.

### Logic
1.  **Determine Paths**:
    - Gets the project root using `get_repository_root_dir()`.
    - Constructs the source path for session preferences using `GetApplicationPaths.SESSION_PREFERENCES_DIR`.
    - Constructs the destination path for session files within the `logik_projekt_path` under a `logs/current_workstation` subdirectory.

2.  **Create Destination Directory**:
    - Ensures the `session_files_destination` directory exists, creating it and any necessary parent directories if they don't.

3.  **Rsync Session Preferences**:
    - Checks if the `session_files_source` exists and is a directory.
    - Executes an `rsync` command to copy files from `session_files_source` to `session_files_destination`.
    - Uses `rsync -avh --ignore-existing` for archive mode, human-readable output, and to avoid overwriting existing files.
    - Logs the execution and success/failure of the `rsync` command.

4.  **Copy Latest Session Log**:
    - Constructs the path to the session logs directory using `GetApplicationPaths.SESSION_LOGS_DIR`.
    - Uses `glob.glob` to find all `.log` files recursively within the session logs directory.
    - If log files are found, it identifies the `latest_log_file` based on modification time.
    - Copies the `latest_log_file` to the `log_file_destination` using `shutil.copy`.
    - Logs the success/failure of the copy operation.

### Error Handling
- Catches `FileNotFoundError` if the project root is not found.
- Catches general `Exception` for any other unexpected errors during the process.
- Logs informative messages for warnings (e.g., source directory not found) and errors.

## Observations
- The script relies on external `rsync` command execution via `os.system()`, which can be less secure and harder to manage than Python's `subprocess` module for more complex scenarios.
- The `get_repository_root_dir` function is a common utility for scripts within a Git repository.
- The use of `pathlib.Path` for path manipulation is modern and readable.
- The logging is well-implemented, providing clear feedback on the script's operations.
- The script handles cases where source directories or log files might be missing gracefully.
