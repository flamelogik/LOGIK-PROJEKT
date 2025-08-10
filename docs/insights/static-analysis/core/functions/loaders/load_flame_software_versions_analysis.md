# Static Analysis: `src/core/functions/get/get_flame_software_versions.py`

## Overview
The `get_flame_software_versions.py` script defines a simple function to retrieve a list of installed Autodesk Flame family software versions. It acts as a wrapper around a utility function that performs the actual system query.

## Dependencies
- **Local Modules (src.core.utils)**:
    - `src.core.utils.flame_software_utils.get_installed_flame_versions`: A utility function that queries the system for installed Flame, Flare, and Flame Assist versions.

## Function: `get_flame_software_versions() -> list[str]`

### Purpose
To provide a standardized way to obtain a list of available Autodesk Flame family software versions installed on the system. This list is typically used to populate UI selection options.

### Arguments
None.

### Logic
- Directly calls `get_installed_flame_versions()` from the `flame_software_utils` module.
- The actual logic for discovering installed versions (e.g., by checking common installation paths or system registries) resides within `get_installed_flame_versions()`.

### Returns
- `list[str]`: A list of strings, where each string represents an installed Flame family software version (e.g., `["Flame 2025", "Flare 2025", "Flame Assist 2025"]`). The format of the strings is determined by `get_installed_flame_versions()`.

## Observations
- This function serves as a clean interface to the underlying system query logic for Flame software versions.
- It promotes modularity by delegating the complex task of version discovery to a specialized utility function (`get_installed_flame_versions`).
- The function is concise and focused on a single task, making it highly reusable and testable.
- Its primary use case is likely populating a dropdown or list in the application's user interface, allowing users to select their target Flame version.
