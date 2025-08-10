# Insight: `create_projekt_backup_script.py`

## 1. Module Type

`create_projekt_backup_script.py` is a Python utility module. It is designed to generate shell scripts for automating project backups and crontab entries for scheduling these backups.

## 2. Purpose

The primary purpose of this module is to facilitate the automated backup of LOGIK-PROJEKT directories. It creates two main files:
1.  A shell script that performs the actual project backup using `rsync`.
2.  A shell script that helps in adding the backup script to the system's crontab for scheduled execution.
It also generates an `exclusion_list.txt` for `rsync`.

## 3. Behavior and Functionality

- **Directory Creation:** It creates necessary directories for storing the generated backup scripts within the LOGIK-PROJEKT structure (e.g., `logik_projekt_path/backup/backup-scripts/`).
- **`os.umask(0)`:** Sets the umask to 0 to ensure newly created files and directories have broad read/write permissions.
- **Template Reading and Replacement:** It reads content from predefined template files (`backup_template` and `archive_script_to_crontab_template.sh`). It then performs string replacements on these templates using project-specific data (e.g., project names, workstation name, paths) provided in the `projekt_summary_data` dictionary.
- **Script Generation:** It writes the modified template content to new `.sh` files, creating the executable backup script and the crontab setup script.
- **Permissions:** It sets executable permissions (`0o755`) on the generated shell scripts, making them ready for execution.
- **Exclusion List Copy:** It copies a generic `exclusion_list.txt` template and renames it to be project-specific, placing it in the same `output_dir`.
- **Logging:** It uses the `logging` module to provide informative messages about the script creation process, including success messages and the paths of the generated files.

## 4. Key Functions

- `create_projekt_backup_script(projekt_summary_data: dict, backup_template_path: str, backup_script_dir: str)`:
  - Purpose: Generates the main project backup shell script, its associated `exclusion_list.txt`, and the crontab entry script.
  - Arguments: `projekt_summary_data` (project details), `backup_template_path` (path to the backup script template), `backup_script_dir` (destination for the generated script).
  - Behavior: Reads templates, performs string replacements, writes new executable scripts, copies exclusion list, and logs the process.

## 5. Signals and Slots

This module is a pure utility module and does not interact with PySide6. Therefore, it does not define or use any signals or slots.

## 6. Dependencies and Relationships

- **Standard Python Libraries:** `os`, `logging`, `datetime`, `shutil`.
- **External Templates:** It relies on external template files located in `cfg/site-cfg/logik-projekt-cfg/logik-projekt-templates/rsync-backup-templates/`.
- **`projekt_summary_data`:** This module is heavily dependent on the `projekt_summary_data` dictionary, which is typically assembled by the main application logic (`AppLogic`) from various UI inputs and system information.
- **Relationship to Project Creation Workflow:** This script is called as part of the overall project creation process (e.g., by `projekt_creator.py`) to set up automated backups for the newly created project.
- **External `rsync` Utility:** The generated backup script is designed to use the `rsync` command-line utility, implying a dependency on Unix-like operating systems.
- **External `crontab` Utility:** The generated crontab script is designed to interact with the system's `crontab` utility, implying a dependency on Unix-like operating systems.

## 7. Other Useful Information

- **Automated Data Protection:** This script is crucial for implementing automated backup strategies, which are essential for data recovery and business continuity.
- **Customization:** The use of templates and string replacement allows for flexible customization of backup parameters and schedules.
- **System Integration:** The ability to generate crontab entries enables seamless integration with system-level scheduling, facilitating hands-off automated backups.
- **Security Considerations:** As it generates and sets executable permissions on shell scripts, proper validation of input data (though not directly handled within this module) is crucial to prevent command injection vulnerabilities. The `exclusion_list.txt` is important for controlling what gets backed up, preventing unnecessary data transfer or sensitive file exposure.