# Static Analysis: `src/core/utils/ocio_utils.py`

## Overview
The `ocio_utils.py` module provides utility functions for interacting with OpenColorIO (OCIO) configurations. This includes discovering OCIO configurations on the system, extracting their names, and resolving full paths from relative paths.

## Dependencies
- **Python Standard Library**: `os`

## Class: `GetOCIOConfigs`

### Purpose
To discover all valid OCIO configurations within a specified base directory and provide them in a structured format.

### Initialization (`__init__`)
- Initializes with a `base_dir` (defaults to `"/opt/Autodesk/colour_mgmt/configs"`).

### Methods

#### `get_ocio_configs(self) -> list[tuple[str, str]]`
- **Purpose**: To discover all valid OCIO configurations within the `base_dir`.
- **Arguments**: None.
- **Logic**:
    - Initializes an empty list `ocio_configs`.
    - Walks the directory tree starting from `base_dir` using `os.walk()`.
    - For each directory found:
        - Skips directories containing `"flame_internal_use"`.
        - Checks if `"config.ocio"` exists in the current directory's files.
        - If `"config.ocio"` is found:
            - Constructs the `ocio_cfg_path`.
            - Determines the `relative_dir` of the current OCIO config relative to `base_dir`.
            - Extracts the `ocio_name` using `get_ocio_name()`.
            - Appends a tuple `(relative_dir, ocio_name)` to `ocio_configs`.
- Returns the `ocio_configs` list.

## Function: `get_ocio_details_from_relative_path(relative_path: str) -> tuple[str, str]`

### Purpose
To resolve the full path and name of an OCIO configuration given its relative path.

### Arguments
- `relative_path` (str): The relative path to the OCIO configuration (e.g., `"ACES/ACEScg/config.ocio"`).

### Logic
- Defines the `base_dir` for OCIO configurations.
- Constructs the `full_path` to the OCIO configuration file by joining `base_dir` and `relative_path`.
- Extracts the `ocio_name` using `get_ocio_name()`.
- Returns a tuple `(ocio_name, full_path)`.

## Function: `get_ocio_name(ocio_config_string: str) -> str`

### Purpose
To extract the OCIO name from a given OCIO configuration string.

### Arguments
- `ocio_config_string` (str): The OCIO configuration string.

### Logic
- If the `ocio_config_string` contains a slash (`/`), it assumes the name is the last part of the path, with `.ocio` removed.
- Otherwise, it returns the `ocio_config_string` as is.

## Observations
- This module is crucial for the application's color management features, allowing it to discover and utilize system-wide OCIO configurations.
- The `GetOCIOConfigs` class provides a robust way to scan for OCIO setups, with a filter for internal Flame configurations.
- The `get_ocio_details_from_relative_path` function is useful for converting relative paths (often stored in preferences) into absolute paths for direct access.
- The `get_ocio_name` function correctly extracts the OCIO name from a path string.

## Function: `GetOCIOConfigs(base_dir="/opt/Autodesk/colour_mgmt/configs")`

### Purpose
To discover all valid OCIO configurations within a specified base directory.

### Arguments
- `base_dir` (str, optional): The base directory to search for OCIO configurations. Defaults to `"/opt/Autodesk/colour_mgmt/configs"`.

### Logic
- Initializes an empty list `ocio_configs`.
- Walks the directory tree starting from `base_dir` using `os.walk()`.
- For each directory found:
    - Skips directories containing `"flame_internal_use"`.
    - Checks if `"config.ocio"` exists in the current directory's files.
    - If `"config.ocio"` is found:
        - Constructs the `ocio_cfg_path`.
        - Determines the `relative_dir` of the current OCIO config relative to `base_dir`.
        - Extracts the `ocio_name` using `get_ocio_config_name()`.
        - Appends a tuple `(relative_dir, ocio_name)` to `ocio_configs`.
- Returns the `ocio_configs` list.

## Function: `get_ocio_details_from_relative_path(relative_path: str) -> tuple[str, str]`

### Purpose
To resolve the full path and name of an OCIO configuration given its relative path.

### Arguments
- `relative_path` (str): The relative path to the OCIO configuration (e.g., `"ACES/ACEScg"`).

### Logic
- Defines the `base_dir` for OCIO configurations.
- Constructs the `full_path` to the `config.ocio` file by joining `base_dir`, `relative_path`, and `"config.ocio"`.
- Extracts the `ocio_name` using `get_ocio_config_name()`.
- Returns a tuple `(ocio_name, full_path)`.

## Function: `get_ocio_name(ocio_config_string: str) -> str`

### Purpose
(Placeholder) To extract the OCIO name from a given OCIO configuration string.

### Arguments
- `ocio_config_string` (str): The OCIO configuration string.

### Logic
- Currently, this is a placeholder function.
- If the `ocio_config_string` contains a slash (`/`), it assumes the name is the last part of the path, with `.ocio` removed.
- Otherwise, it returns the `ocio_config_string` as is.

## Observations
- This module is crucial for the application's color management features, allowing it to discover and utilize system-wide OCIO configurations.
- The `GetOCIOConfigs` function provides a robust way to scan for OCIO setups, with a filter for internal Flame configurations.
- The `get_ocio_config_name` function demonstrates basic text parsing to extract information from configuration files.
- The `get_ocio_details_from_relative_path` function is useful for converting relative paths (often stored in preferences) into absolute paths for direct access.
- The `get_ocio_name` function is a placeholder, indicating that more sophisticated parsing might be needed for various OCIO string formats.