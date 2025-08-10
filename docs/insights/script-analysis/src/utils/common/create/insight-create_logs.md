# Insight: `create_logs.py`

## 1. Module Type

`create_logs.py` is a Python utility module. It provides functions for setting up and managing log files for both shell and Python script executions.

## 2. Purpose

The primary purpose of this module is to standardize and automate the creation of log files for various scripts within the LOGIK-PROJEKT. It ensures that script activities are recorded in a consistent manner, facilitating debugging, auditing, and monitoring.

## 3. Behavior and Functionality

- **`log_shell_script_activity(program_name)`:**
  - Designed to set up logging for shell scripts.
  - Requires `repo_dir` and `projekt_now` environment variables to be set (these are typically set by wrapper scripts or the main application environment).
  - Constructs a log directory path within `logs/shell-logs` relative to `repo_dir`.
  - Creates the log directory if it doesn't exist.
  - Generates a log filename in the format `YYYYMMDD_HHMMSS-program_name.log`.
  - Sets an environment variable `program_log` to the full path of the created log file, allowing other scripts to easily reference it.
  - Returns the path to the created log file.
  - Prints error messages to `sys.stderr` if required environment variables are missing.
- **`log_python_script_activity(program_name)`:**
  - Designed to set up logging for Python scripts.
  - Similar to `log_shell_script_activity`, it requires `repo_dir` and `projekt_now` environment variables.
  - Constructs a log directory path within `logs/python-logs` relative to `repo_dir`.
  - Creates the log directory if it doesn't exist.
  - Generates a log filename in the format `YYYYMMDD_HHMMSS-program_name.log`.
  - Sets an environment variable `program_log` to the full path of the created log file.
  - Returns the path to the created log file.
  - Prints error messages to `sys.stderr` if required environment variables are missing.

## 4. Key Functions

- `log_shell_script_activity(program_name: str) -> str | None`:
  - Purpose: Sets up a dedicated log file for shell script activities.
  - Arguments: `program_name` (the name of the shell script).
  - Returns: The absolute path to the created log file, or `None` if environment variables are missing.
- `log_python_script_activity(program_name: str) -> str | None`:
  - Purpose: Sets up a dedicated log file for Python script activities.
  - Arguments: `program_name` (the name of the Python script).
  - Returns: The absolute path to the created log file, or `None` if environment variables are missing.

## 5. Signals and Slots

This module is a pure utility module and does not interact with PySide6. Therefore, it does not define or use any signals or slots.

## 6. Dependencies and Relationships

- **Standard Python Libraries:** `os` (for environment variables and directory operations), `sys` (for `sys.stderr`).
- **Environment Variables:** Critically depends on the `repo_dir` and `projekt_now` environment variables being set by the calling environment (e.g., a wrapper script or the main application).
- **Relationship to Other Scripts:** This module is intended to be imported and used by other shell and Python scripts within the LOGIK-PROJEKT to ensure consistent logging practices. It provides the foundational setup for where and how logs are stored.

## 7. Other Useful Information

- **Centralized Logging:** By providing dedicated functions for log file creation, this module centralizes the logic for log management, making it easier to maintain and ensuring consistency across different scripts.
- **Time-based Logging:** The use of `projekt_now` (a timestamp) in the log filenames ensures that each script execution gets a unique log file, which is beneficial for tracking and debugging over time.
- **Environment Variable Dependency:** The reliance on environment variables for `repo_dir` and `projekt_now` means that scripts using this module must be executed within an environment where these variables are correctly defined.
