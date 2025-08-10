# Static Analysis: `src/core/projekt_manager/projekt_models.py`

## Overview
The `projekt_models.py` module defines the `ProjektParameters` dataclass, which serves as a comprehensive data model for encapsulating all the necessary parameters required to create and manage an Autodesk Flame project within the LOGIK-PROJEKT application.

## Dependencies
- **Python Standard Library**: `dataclasses` (for `dataclass`, `field`), `typing` (for `Optional`)

## Dataclass: `ProjektParameters`

### Purpose
To provide a structured and type-hinted way to store and pass around all the configuration data related to a new or existing Flame project. This centralizes project parameters, making them easier to manage and validate.

### Attributes

#### Environment Data
- `current_user` (str): The username of the current user. Default: `""`
- `current_group` (str): The primary group of the current user. Default: `""`
- `current_workstation` (str): The hostname of the current workstation. Default: `""`
- `current_os` (str): The operating system of the current environment. Default: `""`

#### Flame Software Data
- `flame_software_choice` (str): The user's selected Flame software choice (e.g., "Flame 2026.1"). Default: `""`
- `flame_software_name` (str): The name of the Flame software (e.g., "Flame"). Default: `""`
- `flame_software_version` (str): The version of the Flame software (e.g., "2026.1"). Default: `""`
- `flame_software_sanitized_name` (str): Sanitized version of the software name. Default: `""`
- `flame_software_sanitized_version` (str): Sanitized version number of the software. Default: `""`

#### Flame Projekt Data
- `flame_projekt_name` (str): The full, unique name of the Flame project. Default: `""`
- `flame_projekt_nickname` (str): A shorter, user-friendly nickname for the Flame project. Default: `""`
- `flame_projekt_shotgun_name` (str): The name of the Flame project as it might appear in Shotgun/ShotGrid. Default: `""`
- `flame_projekt_description` (str): A description for the Flame project. Default: `""`
- `flame_projekt_home` (str): The home directory path for the Flame project. Default: `""`
- `flame_projekt_setups_dir` (str): The setups directory path for the Flame project. Default: `""`
- `flame_projekt_media_dir` (str): The media directory path for the Flame project. Default: `""`
- `flame_projekt_catalog_dir` (str): The catalog directory path for the Flame project. Default: `""`
- `flame_projekt_width` (str): The width resolution of the Flame project. Default: `""`
- `flame_projekt_height` (str): The height resolution of the Flame project. Default: `""`
- `flame_projekt_ratio` (str): The aspect ratio of the Flame project. Default: `""`
- `flame_projekt_depth` (str): The bit depth of the Flame project. Default: `""`
- `flame_projekt_rate` (str): The frame rate of the Flame project. Default: `""`
- `flame_projekt_mode` (str): The scan mode of the Flame project. Default: `""`
- `flame_projekt_start` (str): The start frame of the Flame project. Default: `""`
- `flame_projekt_init` (str): The initialization configuration for the Flame project. Default: `""`
- `flame_projekt_ocio` (str): The OCIO configuration for the Flame project. Default: `""`
- `flame_projekt_ocio_path` (str): The full path to the OCIO configuration. Default: `""`
- `flame_projekt_ocio_name` (str): The name of the OCIO configuration. Default: `""`
- `flame_projekt_cachef` (str): The float cache setting for the Flame project. Default: `""`
- `flame_projekt_cachef_id` (str): The ID for the float cache setting. Default: `""`
- `flame_projekt_cachei` (str): The integer cache setting for the Flame project. Default: `""`
- `flame_projekt_cachei_id` (str): The ID for the integer cache setting. Default: `""`

#### LOGIK PROJEKT Data
- `logik_projekt_name` (str): The calculated name for the LOGIK-PROJEKT. Default: `""`
- `logik_projekt_path` (str): The filesystem path for the LOGIK-PROJEKT. Default: `""`
- `logik_projekt_config_name` (str): The name of the LOGIK-PROJEKT configuration used. Default: `""`
- `logik_projekt_config_tree` (str): Path to the filesystem tree configuration. Default: `""`
- `logik_projekt_config_bookmarks` (str): Path to the Flame bookmarks configuration. Default: `""`
- `logik_projekt_config_workspace` (str): Path to the Flame workspace configuration. Default: `""`

#### Workflow Options
- `launch_flame_after_creation` (bool): Flag indicating whether to launch Flame automatically after project creation. Default: `False`

### Observations
- The `ProjektParameters` dataclass is a central data structure that aggregates all necessary information for project creation and management, promoting a single source of truth for project-related data.
- The use of Python's `dataclasses` module provides a concise way to define data-holding classes, automatically generating methods like `__init__`, `__repr__`, etc.
- All attributes are initialized with empty strings or `False` as default values, ensuring that instances can be created without providing all parameters initially.
- The comprehensive set of fields covers various aspects of a Flame project, from basic naming and paths to detailed technical specifications and workflow options.
- This dataclass is likely used to pass a consolidated set of project data between different modules and functions within the application, particularly between the UI and the core logic for project creation.