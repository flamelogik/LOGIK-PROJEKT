# Static Analysis: `src/core/functions/create/create_flame_launcher_script.py`

## Overview
The `create_flame_launcher_script.py` script defines a function to generate a shell script that launches Autodesk Flame. This generated launcher script is configured with the correct project and environment settings, ensuring a streamlined startup for Flame projects.

## Dependencies
- **Python Standard Library**: `os`, `logging`, `datetime`, `shutil`

## Function: `create_flame_launcher_script(...)`

### Purpose
To create a bash shell script (`flame_launcher_script.sh`) that automates the launching of Autodesk Flame with project-specific configurations. This script is then copied to the Flame project's `setups/scripts/startup/` directory.

### Arguments
- `repository_root_dir` (str): The root directory of the LOGIK-PROJEKT application.
- `logik_projekt_path` (str): The full path to the created PROJEKT directory.
- `current_workstation` (str): The hostname of the workstation.
- `current_os` (str): The operating system of the project.
- `the_projekts_dir` (str): The root directory for all projects.
- `the_projekt_flame_dirs` (str): The root directory for Flame projects.
- `the_adsk_dir` (str): The Autodesk installation directory.
- `the_adsk_dir_linux` (str): The Autodesk install dir for Linux.
- `the_adsk_dir_macos` (str): The Autodesk install dir for macOS.
- `logik_projekt_name` (str): The name of the project.
- `the_projekt_flame_name` (str): The Flame-specific project name.
- `flame_software_sanitized_version` (str): Sanitized software version (e.g., "2026.1").
- `flame_software_choice` (str): The full software version (e.g., "Flame 2026.1").
- `flame_projekt_setups_dir` (str): The absolute path to the Flame project's "setups" directory.

### Logic
1.  **Logging**: Logs an informational message about the creation of the launcher script.
2.  **Path Construction**: Constructs various project-related paths, including the target path for the generated launcher script within the LOGIK-PROJEKT's session preferences directory.
3.  **Directory Creation**: Ensures the parent directory for the target launcher script exists.
4.  **Read Template**: Reads the content of the `flame_launcher_template.sh` file.
5.  **Determine Application Starter**: Based on `flame_software_choice`, determines the correct Autodesk application starter (`startFlame`, `startFlare`, `startFlameAssist`).
6.  **Placeholder Replacement**: Defines a dictionary of placeholders and their corresponding values (e.g., project names, dates, paths, application starter). It then iterates through this dictionary, replacing all occurrences of placeholders in the template content with their actual values.
7.  **Write Launcher Script**: Writes the modified template content to the target launcher script file.
8.  **Set Permissions**: Sets execute permissions (`0o755`) for the generated launcher script.
9.  **Copy to Flame Setups**: 
    - Defines an `additional_target_dir` within the Flame project's `setups/scripts/startup/` directory.
    - Ensures this directory exists.
    - Copies the generated launcher script from its temporary location (`tgt_launcher_script`) to this `additional_target_dir`, preserving metadata (`shutil.copy2`).
    - Sets execute permissions for the copied script.
10. **Logging**: Logs success messages for both modification and copying operations.
11. **Return Value**: Returns the path to the generated launcher script in the session preferences directory.

## Observations
- The script uses string replacement for templating, which is effective for simple shell scripts but can become complex for more intricate configurations.
- It leverages `os.umask(0)` to ensure consistent file permissions, which is important for scripts that need to be executable.
- The use of `shutil.copy2` is good practice for preserving file metadata during copying.
- The script automates a critical step in integrating LOGIK-PROJEKT with Flame by generating a customized launcher.
- The logic for determining the `app_starter` based on `flame_software_choice` demonstrates adaptability to different Flame Family applications.
