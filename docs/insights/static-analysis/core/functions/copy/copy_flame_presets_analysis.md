# Static Analysis: `src/core/functions/copy/copy_flame_presets.py`

## Overview
The `copy_flame_presets.py` script defines a function to copy site-level Flame presets and configurations to newly created project directories. It utilizes `rsync` for efficient directory synchronization.

## Dependencies
- **Python Standard Library**: `os`, `shutil`, `logging`, `sys`, `pathlib`
- **Local Modules (src.core.functions.get)**:
    - `src.core.functions.get.get_application_paths.GetApplicationPaths`
- **Local Modules (src.core.utils)**:
    - `src.core.utils.path_utils.get_repository_root_dir`

## Function: `copy_flame_presets(logik_projekt_path: str, flame_projekt_setups_dir: str)`

### Purpose
To copy Flame presets from predefined source locations to the appropriate project-specific and shared Flame directories.

### Arguments
- `logik_projekt_path` (str): The absolute path to the LOGIK-PROJEKT directory.
- `flame_projekt_setups_dir` (str): The absolute path to the Flame project's "setups" directory.

### Logic
1.  **Get Project Root**: Determines the project's root directory using `get_repository_root_dir()`.
2.  **Copy Flame Presets to Project Setups**:
    - Defines `flame_presets_source` using `GetApplicationPaths.FLAME_PRESETS_DIR` (e.g., `cfg/site-cfg/flame-cfg/flame-presets`).
    - Sets `flame_presets_destination` to `flame_projekt_setups_dir`.
    - If `flame_presets_source` exists and is a directory, it executes an `rsync` command (`rsync -avh --ignore-existing`) to copy its contents to the destination. Logs the execution and result.
3.  **Copy Shared Presets to Autodesk Shared Directory**:
    - Defines `shared_presets_source` using `GetApplicationPaths.SHARED_PRESETS_DIR`.
    - Sets `shared_presets_destination` to `GetApplicationPaths.AUTODESK_SHARED_DIR` (e.g., `/opt/Autodesk/shared/`).
    - If `shared_presets_source` exists and is a directory, it executes an `rsync` command to copy its contents to the destination.
    - **Important Note**: A warning is logged indicating that copying to `/opt/Autodesk/shared/` might require root privileges, as `os.system` is used for `rsync`.
    - Logs the execution and result.

### Error Handling
- Catches `FileNotFoundError` if the project root is not found.
- Catches general `Exception` for any other unexpected errors during the preset copy process.
- Logs informational messages for successful operations and warnings for missing source directories or potential privilege issues.

## Observations
- The script uses `os.system()` to execute `rsync` commands. While functional, using Python's `subprocess` module would offer more control, better error handling, and improved security by avoiding shell injection risks.
- The `get_repository_root_dir` function is a common pattern for locating project resources.
- The script handles two distinct copying operations: one for project-specific Flame presets and another for shared Autodesk presets.
- The explicit warning about root privileges for `/opt/Autodesk/shared/` is crucial for user awareness.
