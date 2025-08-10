# Insight: `ocio_utils.py`

## 1. Module Type

`ocio_utils.py` is a Python utility module. It provides functions for discovering and extracting information from OpenColorIO (OCIO) configurations.

## 2. Purpose

The primary purpose of this module is to help the application locate and identify available OCIO configurations on the system, particularly those installed with Autodesk products, and to extract their names and paths.

## 3. Behavior and Functionality

- **`GetOCIOConfigs` Class:**
  - **`__init__(self, base_dir="/opt/Autodesk/colour_mgmt/configs")`:** Initializes with a `base_dir`.
  - **`get_ocio_configs(self)`:**
    - Traverses a specified `base_dir` (defaulting to `/opt/Autodesk/colour_mgmt/configs`).
    - Searches for `config.ocio` files within subdirectories.
    - Excludes directories containing `"flame_internal_use"`.
    - For each found `config.ocio` file, it determines its relative path and attempts to extract its name using `get_ocio_name`.
    - Returns a list of tuples, where each tuple contains the relative directory and the OCIO configuration name.
- **`get_ocio_details_from_relative_path(relative_path)`:**
  - Constructs the full path to an OCIO configuration file based on a given `relative_path` and the default `base_dir`.
  - Retrieves the OCIO configuration name using `get_ocio_name`.
  - Returns a tuple containing the OCIO name and its full path.
- **`get_ocio_name(ocio_config_string)`:**
  - Extracts the OCIO name from a given OCIO configuration string.
  - If the `ocio_config_string` contains a slash (`/`), it assumes the name is the last part of the path, with `.ocio` removed.
  - Otherwise, it returns the `ocio_config_string` as is.

## 4. Key Functions

- `GetOCIOConfigs(base_dir: str = "/opt/Autodesk/colour_mgmt/configs")`:
  - Purpose: Discovers all OCIO configurations within a specified base directory.
  - Arguments: `base_dir` (the directory to search within).
  - Returns: A list of tuples, each containing the relative directory and the name of an OCIO configuration.
- `get_ocio_details_from_relative_path(relative_path: str) -> tuple[str, str]`:
  - Purpose: Retrieves the OCIO name and full path given a relative path to an OCIO configuration.
  - Arguments: `relative_path` (the relative path to the OCIO configuration).
  - Returns: A tuple containing the OCIO name and its full absolute path.
- `get_ocio_name(ocio_config_string: str) -> str`:
  - Purpose: Extracts the OCIO name from a given OCIO config string.
  - Arguments: `ocio_config_string` (the OCIO configuration string).
  - Returns: The extracted OCIO name.

## 5. Signals and Slots

This module is a pure utility module and does not interact with PySide6. Therefore, it does not define or use any signals or slots.

## 6. Dependencies and Relationships

- **Standard Python Libraries:** `os` (for file system operations).
- **External OCIO Configurations:** This module is designed to interact with and parse actual OCIO configuration files (`config.ocio`) found on the system.
- **Operating System:** Relies on a specific directory structure (`/opt/Autodesk/colour_mgmt/configs`) typical of Linux installations for Autodesk products.
- **Relationship to Color Management Workflow:** This module is a foundational component for any color management features within the LOGIK-PROJEKT application, allowing it to discover and present available OCIO configurations to the user.

## 7. Other Useful Information

- **Automated Discovery:** The `GetOCIOConfigs` class provides a robust way to automatically find OCIO configurations, which is essential for applications that need to integrate with various color pipelines.
- **Flexibility:** The `base_dir` argument in `GetOCIOConfigs` allows for searching in different locations if needed, although the default is specific to Autodesk installations.
- **Clarity:** The `get_ocio_name` function correctly extracts the OCIO name from a path string.

## 4. Key Functions

- `get_ocio_config_name(file_path: str) -> str | None`:
  - Purpose: Extracts the name from an OCIO configuration file.
  - Arguments: `file_path` (the absolute path to the `config.ocio` file).
  - Returns: The OCIO configuration name as a string, or `None` if not found or an error occurs.
- `GetOCIOConfigs(base_dir: str = "/opt/Autodesk/colour_mgmt/configs") -> list[tuple[str, str]]`:
  - Purpose: Discovers all OCIO configurations within a specified base directory.
  - Arguments: `base_dir` (the directory to search within).
  - Returns: A list of tuples, each containing the relative directory and the name of an OCIO configuration.
- `get_ocio_details_from_relative_path(relative_path: str) -> tuple[str, str]`:
  - Purpose: Retrieves the OCIO name and full path given a relative path to an OCIO configuration.
  - Arguments: `relative_path` (the relative path to the OCIO configuration).
  - Returns: A tuple containing the OCIO name and its full absolute path.
- `get_ocio_name(ocio_config_string: str) -> str`:
  - Purpose: (Placeholder) Extracts the OCIO name from a given OCIO config string.
  - Arguments: `ocio_config_string` (the OCIO configuration string).
  - Returns: The extracted OCIO name.

## 5. Signals and Slots

This module is a pure utility module and does not interact with PySide6. Therefore, it does not define or use any signals or slots.

## 6. Dependencies and Relationships

- **Standard Python Libraries:** `os` (for file system operations).
- **External OCIO Configurations:** This module is designed to interact with and parse actual OCIO configuration files (`config.ocio`) found on the system.
- **Operating System:** Relies on a specific directory structure (`/opt/Autodesk/colour_mgmt/configs`) typical of Linux installations for Autodesk products.
- **Relationship to Color Management Workflow:** This module is a foundational component for any color management features within the LOGIK-PROJEKT application, allowing it to discover and present available OCIO configurations to the user.

## 7. Other Useful Information

- **Automated Discovery:** The `GetOCIOConfigs` function provides a robust way to automatically find OCIO configurations, which is essential for applications that need to integrate with various color pipelines.
- **Flexibility:** The `base_dir` argument in `GetOCIOConfigs` allows for searching in different locations if needed, although the default is specific to Autodesk installations.
- **Placeholder for Complex Parsing:** The `get_ocio_name` function is a placeholder, indicating that more sophisticated parsing logic might be required in the future to handle different ways OCIO configurations might be referenced or named.
