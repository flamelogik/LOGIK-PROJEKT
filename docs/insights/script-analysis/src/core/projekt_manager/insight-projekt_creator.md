# Insight: `projekt_creator.py`

## 1. Module Type

`projekt_creator.py` is a Python module responsible for orchestrating the creation of Autodesk Flame projects and their associated file structures within the LOGIK-PROJEKT ecosystem.

## 2. Purpose

The primary purpose of this module is to automate the complex process of setting up a new Flame project. This includes creating filesystem directories, generating configuration files, establishing symbolic links, copying presets and scripts, and preparing various project management and backup utilities.

## 3. Behavior and Functionality

- **`ProjektCreator` Class:**
  - Encapsulates the entire project creation workflow.
  - **`create_projekt(self, config: ProjektParameters)` method:**
    - Takes a `ProjektParameters` object as input, which contains all the necessary configuration data for the new project.
    - Executes a series of sequential steps to build the project:
      1.  **Logging:** Initiates logging for the project creation process.
      2.  **Export Session Variables:** Exports project configuration data to session-specific variable files.
      3.  **Export Session ADSK JSON:** Exports project configuration data to an Autodesk-specific JSON format.
      4.  **Create Filesystem Directories:** Establishes the core filesystem directory structure for the LOGIK-PROJEKT.
      5.  **Generate Flame Project XML:** Creates an XML file based on a template, used for Flame project creation.
      6.  **Create Flame Project via Wiretap:** Uses the generated XML to create the actual Flame project via Wiretap (Flame's API).
      7.  **Create Flame Project Setup Directories:** Sets up specific directories within the Flame project structure.
      8.  **Create Symbolic Links:** Establishes symbolic links between the LOGIK-PROJEKT filesystem and the Flame project setups directory.
      9.  **Copy Site Presets:** Copies predefined Flame presets into the new project.
      10. **Copy Flame Python Scripts:** Copies custom Python scripts for Flame into the project.
      11. **Copy Flame Bookmarks:** Copies Flame bookmarks, linking filesystem directories to Flame project folders.
            12. **Create Archive Script:** Generates a script for archiving the Flame project.
      13. **Create Backup Script:** Generates a backup script for the project, typically using `rsync`.
      14. **Create Backup Crontab Script:** Creates a script to schedule automated backups using `cron`.
      15. **Create Flame Startup Script:** Generates a script to start the Flame application with specific project settings.
      16. **Create Flame Launcher Script:** Creates a general launcher script for the Flame project.
      17. **Create Project Launcher Alias:** Sets up a system alias for easy launching of the project.
      18. **Create PostgreSQL Database:** Initializes a PostgreSQL database for the project.
      19. **Launch Flame (Optional):** If configured, attempts to launch Flame after project creation, capturing its output.
      20. **Copy Current Session Files:** Copies relevant session files to the new project directory.

- **`create_projekt(projekt_summary_data: dict)` function:**
  - A convenience function that acts as the main entry point for project creation.
  - Takes a dictionary `projekt_summary_data` (which is expected to contain all project configuration details).
  - Instantiates `ProjektParameters` from the dictionary and then calls the `ProjektCreator.create_projekt` method.

## 4. Key Classes and Functions

- **`class ProjektCreator`:**
  - Purpose: Manages the end-to-end process of creating a new Autodesk Flame project and its associated LOGIK-PROJEKT structure.
  - Methods:
    - `create_projekt(self, config: ProjektParameters) -> None`:
      - Purpose: Executes the detailed steps for project creation.
      - Arguments: `config` (an instance of `ProjektParameters` containing project details).
      - Returns: None.
- **`create_projekt(projekt_summary_data: dict) -> None`:**
  - Purpose: Public interface for initiating project creation.
  - Arguments: `projekt_summary_data` (a dictionary of project configuration data).
  - Returns: None.

## 5. Signals and Slots

This module is a core logic module and does not directly interact with PySide6 signals or slots. Its operations are primarily sequential and command-line/filesystem based.

## 6. Dependencies and Relationships

- **Internal Dependencies (from `src.core.utils`):**
  - `path_utils`: Used for creating directories and getting the project root.
  - `system_info_utils`: Used for `get_short_hostname` (though not directly in the `create_projekt` method shown, it's imported and likely used in related functions).
- **Internal Dependencies (from `src.core.projekt_manager`):**
  - `projekt_models.ProjektParameters`: Crucial for defining the structure of project configuration data.
- **Internal Dependencies (from `src.core.functions`):**
  - A large number of specific functions are imported and called, each responsible for a distinct step in the project creation process (e.g., `export_session_variables`, `create_projekt_filesystem_dirs`, `create_flame_wiretap_node`, `copy_flame_presets`, `create_projekt_backup_script`, etc.). This indicates a highly modular design where `projekt_creator.py` acts as an orchestrator.
- **External Dependencies:**
  - `os`, `logging`, `subprocess`: Standard Python libraries for file system operations, logging, and running external commands (like launching Flame).
- **Autodesk Flame:** This module is fundamentally tied to Autodesk Flame, as it creates Flame projects, interacts with Flame's Wiretap API, and sets up Flame-specific configurations.

## 7. Other Useful Information

- **Orchestration Layer:** `projekt_creator.py` serves as a high-level orchestration layer, coordinating calls to many smaller, specialized functions. This makes the overall process manageable and allows for easier debugging and modification of individual steps.
- **Automation:** This module is central to the automation capabilities of LOGIK-PROJEKT, significantly reducing the manual effort and potential for errors in setting up new Flame projects.
- **Error Handling:** Includes logging for various stages and `try-except` blocks for critical operations like launching Flame, providing feedback on success or failure.
- **Modularity:** The extensive use of imported functions for each step promotes modularity, allowing individual creation tasks to be developed, tested, and maintained independently.
