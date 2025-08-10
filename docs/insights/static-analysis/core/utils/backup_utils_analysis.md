# Static Analysis: `src/core/utils/backup_utils.py`

## Overview
The `backup_utils.py` module provides utility functions for managing project backups, primarily by constructing and executing `rsync` commands. It includes functions for generating the `rsync` command string, running the backup, and determining the path to the backup script.

## Dependencies
- **Python Standard Library**: `subprocess`, `os`

## Function: `get_rsync_backup_command(projekt_summary_data, source_dir, dest_dir)`

### Purpose
To construct a comprehensive `rsync` command string based on provided project summary data, source directory, and destination directory. This command is designed to perform a robust backup operation, including logging and exclusion of specified files.

### Arguments
- `projekt_summary_data` (dict): A dictionary containing project-specific information, such as `projekt_name` and `flame_workstation_name`.
- `source_dir` (str): The absolute path to the source directory to be backed up.
- `dest_dir` (str): The absolute path to the destination directory where the backup will be stored.

### Logic
1.  **Extract Data**: Retrieves `projekt_name` and `flame_workstation_name` from `projekt_summary_data`, using default values if keys are missing.
2.  **Define Log Directory**: Constructs a path for `rsync` logs within the `dest_dir` and ensures this directory exists.
3.  **Define Log and Exclusion Files**: 
    - `log_file`: Path for the `rsync` log file, named after the project.
    - `exclusion_file`: Path to the `exclusion_list.txt` specific to the project and workstation, located within the `source_dir`'s backup structure.
4.  **Construct Command**: Builds a list representing the `rsync` command and its arguments:
    - `rsync` executable.
    - `-av`: Archive mode (recursive, preserves permissions, timestamps, etc.), verbose output.
    - `--copy-links`: Copies symlinks as symlinks.
    - `--exclude='.DS_Store'`: Excludes macOS-specific desktop files.
    - `--log-file={log_file}`: Specifies the log file for `rsync` output.
    - `--exclude-from={exclusion_file}`: Specifies a file containing patterns of files/directories to exclude from the backup.
    - `source_dir`: The source directory.
    - `dest_dir`: The destination directory.
5.  **Return**: Returns the constructed `rsync_command` as a list of strings.

### Error Handling
- Includes `os.makedirs(..., exist_ok=True)` to safely create the log directory.
- Does not explicitly handle `FileNotFoundError` for `exclusion_file` within this function; `rsync` itself would likely report an error if the file is missing.

## Function: `run_rsync_backup(rsync_command)`

### Purpose
To execute the `rsync` backup command constructed by `get_rsync_backup_command`.

### Arguments
- `rsync_command` (list): A list of strings representing the `rsync` command and its arguments.

### Logic
1.  **Execute Command**: Uses `subprocess.run()` to execute the `rsync_command`.
    - `check=True`: Raises a `CalledProcessError` if the command returns a non-zero exit code.
2.  **Log Success**: If the command completes successfully, prints a success message.

### Error Handling
- Catches `subprocess.CalledProcessError`: If the `rsync` command fails (returns a non-zero exit code). Prints an error message including the exception details.

## Function: `get_rsync_backup_script_path(projekt_summary_data)`

### Purpose
To construct and return the expected absolute path to the generated backup script for a given project.

### Arguments
- `projekt_summary_data` (dict): A dictionary containing project-specific information, such as `logik_projekt_name`, `current_workstation`, and `logik_projekt_path`.

### Logic
1.  **Extract Data**: Retrieves `logik_projekt_name`, `current_workstation`, and `logik_projekt_path` from `projekt_summary_data`, using default values if keys are missing.
2.  **Construct Path**: Builds the `backup_script_path` by joining various components from `projekt_summary_data` and predefined subdirectories.
3.  **Return**: Returns the constructed `backup_script_path` as a string.

### Error Handling
- No explicit error handling within this function; it assumes valid input data for path construction.

## Observations
- This module centralizes the logic for `rsync`-based backups, making it reusable across the application.
- The use of `subprocess.run` for executing `rsync` is a robust and recommended approach for running external commands in Python, allowing for error checking.
- The functions are designed to work with a `projekt_summary_data` dictionary, promoting a consistent data flow.
- The `get_rsync_backup_command` function is highly configurable through its arguments and the use of an exclusion file.
