# Static Analysis: `src/core/utils/config_utils.py`

## Overview
The `config_utils.py` script provides a set of utility functions for locating and accessing various configuration directories and files within the LOGIK-PROJEKT application. It centralizes the logic for finding paths to JSON, XML, CFG, and TXT configuration files, and includes a specific function for loading LOGIK-PROJEKT preferences.

## Dependencies
- **Python Standard Library**: `json`, `os` (though `pathlib.Path` is preferred for path manipulation), `pathlib.Path`
- **Local Modules (src.core.utils)**:
    - `src.core.utils.path_utils.get_repository_root_dir`: A utility function to get the absolute path to the project's root directory.

## Functions

#### `find_json_dir_path(subdirectory=None)`
- **Purpose**: Locates the base directory for JSON configuration files, optionally within a specified subdirectory.
- **Logic**:
    1.  Gets the project root using `get_repository_root_dir()`.
    2.  Constructs the base JSON path: `repository_root_dir / "config" / "flame-configuration"`.
    3.  If `subdirectory` is provided, appends it to the path.
    4.  Checks if the constructed `json_path` exists using `json_path.exists()`.
    5.  If it doesn't exist, raises a `FileNotFoundError`.
    6.  Returns the `json_path` (a `pathlib.Path` object).

#### `find_xml_directory(subdirectory=None)`
- **Purpose**: Locates the base directory for XML configuration files, optionally within a specified subdirectory.
- **Logic**:
    1.  Gets the project root.
    2.  Constructs the base XML path: `repository_root_dir / "config" / "parameters" / "xml"`.
    3.  If `subdirectory` is provided, appends it to the path.
    4.  Checks if the constructed `xml_path` exists.
    5.  If it doesn't exist, raises a `FileNotFoundError`.
    6.  Returns the `xml_path`.

#### `find_cfg_directory(subdirectory=None)`
- **Purpose**: Locates the base directory for CFG configuration files, optionally within a specified subdirectory.
- **Logic**:
    1.  Gets the project root.
    2.  Constructs the base CFG path: `repository_root_dir / "config" / "flame-configuration"`.
    3.  If `subdirectory` is provided, appends it to the path.
    4.  Checks if the constructed `cfg_path` exists.
    5.  If it doesn't exist, raises a `FileNotFoundError`.
    6.  Returns the `cfg_path`.

#### `find_txt_directory(subdirectory=None)`
- **Purpose**: Locates the base directory for TXT configuration files, optionally within a specified subdirectory.
- **Logic**:
    1.  Gets the project root.
    2.  Constructs the base TXT path: `repository_root_dir / "config" / "parameters" / "txt"`.
    3.  If `subdirectory` is provided, appends it to the path.
    4.  Checks if the constructed `txt_path` exists.
    5.  If it doesn't exist, raises a `FileNotFoundError`.
    6.  Returns the `txt_path`.

#### `find_parameters_directory(file_type, subdirectory=None)`
- **Purpose**: A dispatcher function that calls the appropriate `find_*_directory` function based on the `file_type` argument.
- **Logic**:
    1.  Converts `file_type` to lowercase.
    2.  Uses `if/elif/else` to call `find_json_dir_path`, `find_xml_directory`, `find_cfg_directory`, or `find_txt_directory` based on the `file_type`.
    3.  If an unsupported `file_type` is provided, raises a `ValueError`.

## Observations
-   **Note**: This module is currently located in `src/core/unused/` and is not actively used in the main application flow.
-   The module centralizes path management for various configuration types, making the application more maintainable and less prone to hardcoded path errors.
-   The use of `pathlib.Path` objects for path manipulation is a modern and robust approach compared to string-based `os.path` functions.
-   Each `find_*_directory` function explicitly checks for directory existence and raises `FileNotFoundError`, providing clear feedback if expected paths are missing.
-   `find_parameters_directory` acts as a convenient facade for accessing different configuration types.
