# Insight: `create_flame_launcher_script.py`

## 1. Module Type

`create_flame_launcher_script.py` is a Python utility module. It is designed to generate a shell script that launches Autodesk Flame (or related applications like Flare or Flame Assist) with specific project and environment settings.

## 2. Purpose

The primary purpose of this module is to create a customized launcher script for a newly created Flame project. This script ensures that when a user launches Flame for a particular project, it automatically opens with the correct project, software version, and environment variables, streamlining the workflow and preventing configuration errors.

## 3. Behavior and Functionality

- **Target Script Generation:** It generates a shell script named `current_session-flame_launcher.sh` within the `pref/session-preferences/` directory of the LOGIK-PROJEKT application.
- **Directory Creation:** It ensures that the target directory for the launcher script exists, creating it if necessary.
- **Template Reading and Replacement:** It reads a base template (`flame_launcher_template.sh`) and performs extensive string replacements using various project-specific data provided as arguments (e.g., project names, workstation, software version, paths).
- **Application Starter Logic:** It includes logic to determine the correct Flame application starter command (`startFlame`, `startFlare`, `startFlameAssist`) based on the `flame_software_choice` argument.
- **Permissions:** It sets executable permissions (`0o755`) on the generated shell script, making it ready for direct execution.
- **Logging:** It uses the `logging` module to provide informative messages about the script creation process, including success messages and the path of the generated file.

## 4. Key Functions

- `create_flame_launcher_script(...)`:
  - Purpose: Generates the customized Flame launcher shell script.
  - Arguments: Takes numerous string arguments representing various project and environment details (e.g., `repository_root_dir`, `logik_projekt_path`, `flame_software_choice`, `the_projekt_flame_name`).
  - Behavior: Reads a template, replaces placeholders with provided data, writes the new executable script, and logs the process.

## 5. Signals and Slots

This module is a pure utility module and does not interact with PySide6. Therefore, it does not define or use any signals or slots.

## 6. Dependencies and Relationships

- **Standard Python Libraries:** `os`, `logging`, `datetime`, `shutil`.
- **External Template:** It relies on an external template file located at `cfg/site-cfg/flame-cfg/flame-templates/flame-launcher-templates/flame_launcher_template.sh`.
- **`projekt_summary_data` (indirectly):** The numerous arguments passed to `create_flame_launcher_script` are typically derived from the `projekt_summary_data` dictionary, which is assembled by the main application logic (`AppLogic`) from various UI inputs and system information.
- **Relationship to Project Creation Workflow:** This script is a crucial step in the overall project creation process (e.g., called by `projekt_creator.py`). It ensures that the newly created Flame project can be easily launched with its specific configuration.
- **External Flame Binaries:** The generated script will execute Flame binaries (e.g., `startFlame`), implying a dependency on a correctly installed Autodesk Flame environment.

## 7. Other Useful Information

- **Workflow Automation:** This script significantly automates the process of launching Flame for a specific project, eliminating the need for manual configuration and reducing potential user errors.
- **Customization:** The template-based approach allows for easy customization of the launcher script's behavior and environment variables without modifying the Python code.
- **Consistency:** Ensures that all projects launched through LOGIK-PROJEKT adhere to a consistent launch methodology.
- **Debugging:** The generated script can be inspected to understand how Flame is being launched, which is useful for debugging environment-related issues.