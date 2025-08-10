# Static Analysis: `src/core/utils/flame_software_utils.py`

## Overview
The `flame_software_utils.py` module provides utility functions for interacting with Autodesk Flame family software. This includes detecting installed versions, sanitizing version names and numbers, and placeholder functions for parsing Flame configuration files and extracting cache format IDs.

## Dependencies
- **Python Standard Library**: `os`, `re`, `platform`

## Function: `get_installed_flame_versions() -> list[str]`

### Purpose
To discover and return a sorted list of installed Autodesk Flame, Flare, and Flame Assist versions on the system by scanning a predefined directory (`/opt/Autodesk`).

### Arguments
None.

### Logic
1.  **Define Search Parameters**: Sets the `directory` to `/opt/Autodesk` and defines `flame_family_prefixes` (e.g., `"flame"`, `"flare"`).
2.  **`_sort_key` (Nested Function)**:
    - This helper function is used as a key for sorting the discovered Flame directories.
    - It parses directory names using a regular expression to extract application name, major, minor, patch versions, and prerelease information.
    - It assigns an importance value to each application type (`flame` > `flare` > `flame_assist`).
    - It returns a tuple `(app_value, major, minor, patch, prerelease_value)` for sorting, ensuring Flame versions are grouped and sorted correctly.
3.  **Scan Directory**: 
    - Checks if the `directory` exists. If not, prints an error and returns an empty list.
    - Lists all entries in the `directory`.
    - Filters entries to include only directories that start with a `flame_family_prefix`.
4.  **Sort Versions**: Sorts the filtered `flame_dirs` using the `_sort_key` function in reverse order (newest versions first).
5.  **Return**: Returns the sorted list of raw directory names (e.g., `["flame_2026.1.pr224", "flare_2025", ...]`).

### Error Handling
- Catches `PermissionError` if access to `/opt/Autodesk` is denied. Prints an error message and returns an empty list.
- Catches general `Exception` for any other unexpected errors during the scanning process. Prints an error message and returns an empty list.

## Function: `sanitize_flame_version_name(name: str) -> str`

### Purpose
To sanitize a Flame version name by converting it to lowercase and replacing spaces with underscores (e.g., `'Flame'` -> `'flame'`).

### Arguments
- `name` (str): The Flame application name.

### Logic
- Converts the input `name` to lowercase.
- Replaces all spaces with underscores.

## Function: `sanitize_flame_version_number(app_name: str) -> str`

### Purpose
To extract and sanitize the version number from a full Flame application name string (e.g., `'flame_2026.1.pr224'` -> `'2026_1'`).

### Arguments
- `app_name` (str): The full application name string.

### Logic
- Uses a regular expression (`r"_(\d+(?:\.\d+)*(?:\.pr\d+)?)$"`) to find the version part of the `app_name`.
- If a match is found, it extracts the version part.
- It then removes any `".pr\d+"` substrings and replaces dots (`.`) with underscores (`_`).
- Returns the sanitized version string.
- If no version part is found, returns an empty string.

## Function: `parse_flame_config(config_content: str) -> dict`

### Purpose
To parse the content of a Flame configuration file (e.g., `sysconfig.cfg`) into a Python dictionary.

### Arguments
- `config_content` (str): The string content of the configuration file.

### Logic
- Attempts to parse the `config_content` as a JSON string using `json.loads()`.
- If successful, returns the resulting dictionary.
- If `json.JSONDecodeError` occurs, logs an error and returns an empty dictionary.

## Function: `get_cache_format_id(cache_string: str) -> str`

### Purpose
(Placeholder) To extract a code or ID from a cache format string (e.g., `'10-bit Log'` -> `'10bitlog'`).

### Arguments
- `cache_string` (str): The cache format string.

### Logic
- Currently, this is a placeholder function. It converts the input string to lowercase and removes hyphens and spaces.

## Observations
- This module is essential for the application's ability to interact with and understand the installed Flame environment.
- The `get_installed_flame_versions` function provides robust version detection and sorting, which is critical for presenting accurate options to the user.
- The sanitization functions (`sanitize_flame_version_name`, `sanitize_flame_version_number`) ensure that version strings are consistently formatted for internal use.
- The placeholder functions (`parse_flame_config`, `get_cache_format_id`) indicate areas for future development where more complex parsing or data extraction logic might be implemented.
