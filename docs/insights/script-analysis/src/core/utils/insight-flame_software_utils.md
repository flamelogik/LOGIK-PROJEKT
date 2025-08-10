# Insight: `flame_software_utils.py`

## 1. Module Type

`flame_software_utils.py` is a Python utility module. It provides functions for interacting with Autodesk Flame family software installations.

## 2. Purpose

The primary purpose of this module is to assist in discovering installed Flame, Flare, and Flame Assist versions on a system, sanitizing their names and versions, and providing placeholder functionality for parsing Flame configuration files.

## 3. Behavior and Functionality

- **`get_installed_flame_versions()`:**
  - Scans the `/opt/Autodesk` directory (typical installation path on Linux).
  - Identifies directories that start with common Flame family prefixes (`flame`, `flare`, `flame_assist`).
  - Sorts the discovered Flame directories based on application importance (Flame > Flare > Flame Assist) and then by version number (major, minor, patch, prerelease) in descending order.
  - Returns a list of raw directory names of installed Flame versions.
  - Includes error handling for `PermissionError` and general exceptions.
- **`_sort_key(directory_name)`:**
  - A private helper function used by `get_installed_flame_versions` to define the sorting logic for Flame application directories.
  - Parses the directory name to extract application name, major, minor, patch, and prerelease versions.
  - Assigns an importance value to each application type for sorting.
- **`sanitize_flame_version_name(name)`:**
  - Converts a Flame version name (e.g., 'Flame') to a sanitized, lowercase, underscore-separated format (e.g., 'flame').
- **`sanitize_flame_version_number(app_name)`:**
  - Extracts and sanitizes the version number from a full application name string (e.g., 'flame_2026.1.pr224' -> '2026_1').
  - Removes 'pr' and subsequent numbers and replaces dots with underscores.
- **`parse_flame_config(config_content)`:**
  - Parses the content of a Flame configuration file (e.g., `sysconfig.cfg`) into a Python dictionary.
  - Attempts to parse the `config_content` as a JSON string using `json.loads()`.
  - If successful, returns the resulting dictionary.
  - If `json.JSONDecodeError` occurs, logs an error and returns an empty dictionary.
- **`get_cache_format_id(cache_string)`:**
  - A placeholder function intended to extract a code/ID from a cache string (e.g., '10-bit Log' -> '10bitlog').
  - Currently converts the string to lowercase and removes hyphens and spaces.

## 4. Key Functions

- `get_installed_flame_versions() -> list[str]`:
  - Purpose: Discovers and lists installed Autodesk Flame family software versions.
  - Arguments: None.
  - Returns: A list of strings, each representing an installed Flame version directory name.
- `sanitize_flame_version_name(name: str) -> str`:
  - Purpose: Sanitizes a Flame application name for consistent use.
  - Arguments: `name` (the original Flame application name).
  - Returns: The sanitized name string.
- `sanitize_flame_version_number(app_name: str) -> str`:
  - Purpose: Extracts and sanitizes the version number from a Flame application string.
  - Arguments: `app_name` (the full application name string).
  - Returns: The sanitized version number string.
- `parse_flame_config(config_content: str) -> dict`:
  - Purpose: Parses Flame configuration content.
  - Arguments: `config_content` (the content of a Flame configuration file).
  - Returns: A dictionary representing the parsed configuration.
- `get_cache_format_id(cache_string: str) -> str`:
  - Purpose: (Placeholder) Extracts an ID from a cache format string.
  - Arguments: `cache_string` (the cache format string).
  - Returns: The extracted and sanitized ID string.

## 5. Signals and Slots

This module is a pure utility module and does not interact with PySide6. Therefore, it does not define or use any signals or slots.

## 6. Dependencies and Relationships

- **Standard Python Libraries:** `os`, `re`, `platform`.
- **Operating System:** Heavily relies on the Linux filesystem structure (`/opt/Autodesk`) for discovering Flame installations. The `platform` module is imported but not directly used in the provided functions, suggesting potential future cross-platform considerations.
- **External Flame Software:** This module's core functionality is to interact with and gather information about installed Autodesk Flame family software.
- **Configuration Files:** The `parse_flame_config` function is designed to process Flame configuration files, implying a relationship with how Flame's settings are read and interpreted by the LOGIK-PROJEKT application.

## 7. Other Useful Information

- **Automated Discovery:** The `get_installed_flame_versions` function provides a robust way to automatically detect available Flame versions, which is critical for applications that need to integrate with or manage multiple Flame installations.
- **Version Management:** The sanitization functions are important for standardizing version strings, making them easier to compare, store, and display within the application.
- **Extensibility:** The placeholder functions (`parse_flame_config`, `get_cache_format_id`) indicate areas where more complex parsing and logic can be added as the application's needs evolve regarding Flame configuration and cache management.
