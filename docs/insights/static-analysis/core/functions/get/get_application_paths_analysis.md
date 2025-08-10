# Static Analysis: `src/core/functions/get/get_application_paths.py`

## Overview
The `GetApplicationPaths` class serves as a centralized repository for defining various file and directory paths used throughout the LOGIK-PROJEKT application. It provides a single source of truth for locating configuration files, templates, and other application resources.

## Dependencies
- **Python Standard Library**: `os`

## Class: `GetApplicationPaths`

### Purpose
To encapsulate and provide easy access to all hardcoded or relative paths for application resources, promoting consistency and simplifying path management across the project.

### Attributes
All attributes are class-level constants, representing paths to directories or files. They are defined using string concatenation or `os.path.join` for platform compatibility.

- `CFG_DIR`: Base path for configuration files.
- `SITE_CFG_DIR`: Base path for site-specific configuration files.
- `FLAME_CFG_DIR`: Base path for Flame-specific configuration files.
- `FLAME_VALUE_LISTS_DIR`: Base path for Flame value lists.
- `FLAME_TEMPLATES_DIR`: Base path for Flame templates.
- `PREF_DIR`: Base path for preference files.
- `SITE_PREFS_DIR`: Base path for site-specific preference files.
- `AUTODESK_SHARED_DIR`: Path to the Autodesk shared directory (e.g., `/opt/Autodesk/shared/`).
- `BIT_DEPTH_LIST_VALUES`: Path to the JSON file defining bit depth options.
- `CACHE_FLOAT_LIST_VALUES`: Path to the JSON file defining float cache format options.
- `CACHE_INTEGER_LIST_VALUES`: Path to the JSON file defining integer cache format options.
- `DEFAULT_TEMPLATE_VALUES`: Path to the JSON file containing default template parameters.
- `FLAME_PRESETS_DIR`: Path to the directory containing Flame presets.
- `FLAME_PYTHON_SCRIPTS_DIR`: Path to the directory containing Flame Python scripts.
- `FRAME_RATE_LIST_VALUES`: Path to the JSON file defining frame rate options.
- `INIT_CONFIG_DIR`: Path to the directory containing init configuration files.
- `LOGIK_PROJEKT_SITE_PREFS`: Path to the main LOGIK-PROJEKT site preferences JSON file.
- `RESOLUTION_PATH`: Base path for resolution-related files.
- `RESOLUTION_LOAD_ORDER_FILE`: Path to the JSON file defining the resolution load order.
- `SCAN_MODE_LIST_VALUES`: Path to the JSON file defining scan mode options.
- `SESSION_LOGS_DIR`: Path to the directory for session-specific log files.
- `SESSION_PREFERENCES_DIR`: Path to the directory for session-specific preference files.
- `SHARED_PRESETS_DIR`: Path to the directory containing shared presets.
- `START_FRAME_LIST_VALUES`: Path to the JSON file defining start frame options.
- `SYSCONFIG_CFG`: Path to the `sysconfig.cfg` file, relative to `FLAME_VALUE_LISTS_DIR` (e.g., `cfg/site-cfg/flame-cfg/flame-value-lists/sysconfig/sysconfig.cfg`).
- `WIRETAP_XML_TEMPLATE`: Path to the XML template file used for Wiretap project creation, relative to `FLAME_TEMPLATES_DIR` (e.g., `cfg/site-cfg/flame-cfg/flame-templates/wiretap-templates/wiretap_IFFFS_project_EXAMPLE.xml`).

## Observations
- This class acts as a central configuration point for all file system paths, making the application more maintainable. If a directory structure changes, only this file needs to be updated.
- The use of string concatenation for many paths, while functional, can be less robust than `os.path.join` for cross-platform compatibility. `os.path.join` is used where explicitly noted.
- The class does not contain any methods; it is purely a data container for constants.
- The paths are relative to the project root where applicable, promoting portability of the LOGIK-PROJEKT application itself.
