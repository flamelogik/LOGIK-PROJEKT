# Projekt Summary Data Map

This document tracks the origin of variables used in the LOGIK-PROJEKT application, specifically focusing on the **Projekt Summary** widget (`RightSubPanelProjektSummary`).

## Overview

The Projekt Summary widget consolidates and displays information from various parts of the application, including user inputs, imported template data, and system environment variables. It serves as a final overview of the project configuration before creation.

## Related Scripts

* [`src/ui/panels/projekt_summary_panel.py`](<../src/ui/panels/projekt_summary_panel.py>)

    * [`src/ui/panels/projekt_template_panel.py`](<../src/ui/panels/projekt_template_panel.py>)
    * [`src/ui/panels/flame_options_panel.py`](<../src/ui/panels/flame_options_panel.py>)
    * [`src/ui/widgets/display/projekt_summary_widget.py`](<../src/ui/widgets/display/projekt_summary_widget.py>)


| Field Name / Displayed Field / Label | Widget Class | Variable Name / Key | Is Displayed? | Data Source (Panel & Widget) | JSON Key | Notes |
|---|---|---|---|---|---|---|
| **Environment** | N/A | | Yes | | N/A | |
| `Current User:` | N/A | `current_user` | Yes | `src/core/utils/system_info_utils.py` (`get_current_user`) | N/A | The user running the application. |
| `Current Group:` | N/A | `current_group` | Yes | `src/core/utils/system_info_utils.py` (`get_primary_group`) | N/A | The primary group of the user. |
| `Current Workstation:` | N/A | `current_workstation` | Yes | `src/core/utils/system_info_utils.py` (`get_short_hostname`) | N/A | The short hostname of the machine. |
| `Current OS` | N/A | `current_os` | Yes | Python's `platform` module | N/A | Detected via Python's `platform` module. |
| **Flame Software** | N/A | | Yes | | N/A | |
| `Flame Software` | `src/ui/widgets/combobox/flame_software_choice_widget.py` | `flame_software` | No | User selection from the Flame version dropdown. | N/A | User selection from the Flame version dropdown. |
| `Flame Software Name` | N/A | `flame_software_name` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A | Parsed from the `flame_software` selection. |
| `Flame Software Version` | N/A | `flame_software_version` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A | Parsed from the `flame_software` selection. |
| `Flame Software Sanitized Name` | N/A | `flame_software_sanitized_name` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A | A cleaned-up version of the software name for internal use, derived from `flame_software`. |
| `Flame Software Sanitized Version` | N/A | `flame_software_sanitized_version` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A | A cleaned-up version of the software version, derived from `flame_software`. |
| **Flame Projekt** | N/A | | Yes | | N/A | |
| `Flame Projekt Name` | N/A | `flame_projekt_name` | Yes | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A | Generated from `flame_projekt_nickname` and `flame_software_sanitized_version` (e.g., `NICKNAME_VERSION`). |
| `Flame Projekt Nickname` | N/A | `flame_projekt_nickname` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template Name` | From the imported JSON template file. |
| `Flame Projekt Shotgun Name` | N/A | `flame_projekt_shotgun_name` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template Name` | From the imported JSON template file. Typically the same as `flame_projekt_nickname`. |
| `Flame Projekt Description` | N/A | `flame_projekt_description` | Yes | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template Description` | From the imported JSON template file. |
| `Flame Projekt Home` | `src/ui/widgets/button/flame_home_dir_widget.py` | `flame_projekt_home` | Yes | User-selected path from the "Flame Home Directory" button. | N/A | User-selected path from the "Flame Home Directory" button. |
| `Flame Projekt Setups Dir` | `src/ui/widgets/button/flame_setups_dir_widget.py` | `flame_projekt_setups_dir` | Yes | User-selected path from the "Flame Setups Directory" button or default from `sysconfig.cfg`. | N/A | User-selected path or default from `sysconfig.cfg`. |
| `Flame Projekt Media Dir` | `src/ui/widgets/button/flame_media_dir_widget.py` | `flame_projekt_media_dir` | Yes | User-selected path from the "Flame Media Directory" button or default from `sysconfig.cfg`. | N/A | User-selected path or default from `sysconfig.cfg`. |
| `Flame Projekt Catalog Dir` | `src/ui/widgets/button/flame_catalog_dir_widget.py` | `flame_projekt_catalog_dir` | Yes | User-selected path from the "Flame Catalog Directory" button or default from `sysconfig.cfg`. | N/A | User-selected path or default from `sysconfig.cfg`. |
| `Flame Projekt Width` | N/A | `flame_projekt_width` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template Width` | From the imported JSON template file. |
| `Flame Projekt Height` | N/A | `flame_projekt_height` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template Height` | From the imported JSON template file. |
| `Flame Projekt Ratio` | N/A | `flame_projekt_ratio` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template Aspect Ratio` | From the imported JSON template file. |
| `Flame Projekt Depth` | N/A | `flame_projekt_depth` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template Bit Depth` | From the imported JSON template file. |
| `Flame Projekt Rate` | N/A | `flame_projekt_rate` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template Framerate` | From the imported JSON template file. |
| `Flame Projekt Mode` | N/A | `flame_projekt_mode` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template Scan Mode` | From the imported JSON template file (scan mode). |
| `Flame Projekt Start` | N/A | `flame_projekt_start` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template Start Frame` | From the imported JSON template file. |
| `Flame Projekt Init` | N/A | `flame_projekt_init` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template Init Config` | From the imported JSON template file (init config). |
| `Flame Projekt Ocio` | N/A | `flame_projekt_ocio` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template OCIO Name` | General OCIO settings from the imported JSON. Corresponds to `projekt_ocio_name`. |
| `Flame Projekt Ocio Path` | N/A | `flame_projekt_ocio_path` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template OCIO Path` | Path to the OCIO configuration file, often found in `sysconfig.cfg`. Corresponds to `projekt_ocio_path`. |
| `Flame Projekt Ocio Name` | N/A | `flame_projekt_ocio_name` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template OCIO Name` | The OCIO policy name from the imported JSON. Corresponds to `projekt_ocio_name`. |
| `Flame Projekt Cache F` | N/A | `flame_projekt_cachef` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template Cache Float` | Float cache setting from the imported JSON. Corresponds to `projekt_cache_float`. |
| `Flame Projekt Cache F ID` | N/A | `flame_projekt_cachef_id` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template Cache Float ID` | Float cache ID from the imported JSON. Corresponds to `projekt_cache_float_id`. |
| `Flame Projekt Cache I` | N/A | `flame_projekt_cachei` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template Cache Integer` | Integer cache setting from the imported JSON. Corresponds to `projekt_cache_integer`. |
| `Flame Projekt Cache I ID` | N/A | `flame_projekt_cachei_id` | No | `src/core/app_logic.py` (`get_projekt_summary_data`) | `Template Cache Integer ID` | Integer cache ID from the imported JSON. Corresponds to `projekt_cache_integer_id`. |
| **LOGIK PROJEKT** | N/A | | Yes | | N/A | |
| `LOGIK-PROJEKT Name` | N/A | `logik_projekt_name` | Yes | Calculated | N/A | Typically the same as `flame_projekt_nickname`. |
| `LOGIK-PROJEKT Path` | N/A | `logik_projekt_path` | Yes | Calculated | N/A | Constructed as "/PROJEKTS/`logik_projekt_name`". |
| `LOGIK-PROJEKT Config` | N/A | `logik_projekt_config_name` | No | `src/ui/widgets/combobox/projekt_config_widget.py` (User Input) | N/A | The name of the generated project configuration file. |
| `LOGIK-PROJEKT Config Tree` | N/A | `logik_projekt_config_tree` | No | `src/ui/widgets/combobox/projekt_config_widget.py` (User Input) | N/A | Sourced from `logik_projekt_config_data` (e.g., `PROJEKT Filesystem Tree`). |
| `LOGIK-PROJEKT Config Bookmarks` | N/A | `logik_projekt_config_bookmarks` | No | `src/ui/widgets/combobox/projekt_config_widget.py` (User Input) | N/A | Sourced from `logik_projekt_config_data` (e.g., `PROJEKT Flame Bookmarks`). |
| `LOGIK-PROJEKT Config Workspace` | N/A | `logik_projekt_config_workspace` | No | `src/ui/widgets/combobox/projekt_config_widget.py` (User Input) | N/A | Sourced from `logik_projekt_config_data` (e.g., `PROJEKT Flame Workspace`). |
<!-- | `LOGIK-PROJEKT Config Prefs Dir` | N/A | `logik_projekt_prefs_dir` | Yes | Static Path  | N/A | "config/site-preferences/logik-projekt-preferences" |
| `LOGIK-PROJEKT Flame Bookmarks Dir` | N/A | `logik_projekt_flame_bookmarks_dir` | Yes | Calculated | N/A | os.path.join(logik_projekt_prefs_dir, "bookmark-prefs", "flame-bookmarks-prefs") |
| `LOGIK-PROJEKT Flame Bookmarks File` | N/A | `logik_projekt_flame_bookmarks_file` | Yes | Calculated | N/A | f"{logik_projekt_flame_bookmarks_dir}/{logik_projekt_config_name}-flame_bookmarks.json" |
| `LOGIK-PROJEKT Filesystem Prefs Dir` | N/A | `logik_projekt_filesystem_prefs_dir` | Yes | Calculated | N/A | os.path.join(logik_projekt_prefs_dir, "directory-prefs", "filesystem-prefs") |
| `LOGIK-PROJEKT Filesystem Prefs File` | N/A | `logik_projekt_filesystem_prefs_file` | Yes | Calculated | N/A | f"{logik_projekt_filesystem_prefs_dir}/{logik_projekt_config_name}-filesystem_directories.json" |
| `LOGIK-PROJEKT Workspace Prefs Dir` | N/A | `logik_projekt_workspace_prefs_dir` | Yes | Calculated | N/A | os.path.join(logik_projekt_prefs_dir, "workspace-prefs", "flame-workspace-prefs") |
| `LOGIK-PROJEKT Workspace Prefs File` | N/A | `logik_projekt_workspace_prefs_file` | Yes | Calculated | N/A | f"{logik_projekt_workspace_prefs_dir}/{logik_projekt_config_name}-flame_workspace.json" |
| `LOGIK-PROJEKT Config Dir` | N/A | `logik_projekt_config_dir` | Yes | Static Path  | N/A | "config/flame-configuration" |
| `LOGIK-PROJEKT Flame Archive Template Dir` | N/A | `logik_projekt_flame_archive_template_dir` | Yes | Static Path | N/A | os.path.join(logik_projekt_config_dir, "flame-archive-templates") |
| `LOGIK-PROJEKT Flame Archive Template File` | N/A | `logik_projekt_flame_archive_template_file` | Yes | Calculated | N/A | f"{logik_projekt_flame_archive_template_dir}/flame_archive_template.sh" |
| `LOGIK-PROJEKT JSON Template Dir` | N/A | `logik_projekt_json_template_dir` | Yes | Static Path | N/A | os.path.join(logik_projekt_config_dir, "json-templates") |
| `LOGIK-PROJEKT JSON Template File` | N/A | `logik_projekt_json_template_file` | Yes | Calculated | N/A | f"{logik_projekt_json_template_dir}/json-template.json" |
| `LOGIK-PROJEKT Rsync Template Dir` | N/A | `logik_projekt_rsync_template_dir` | Yes | Static Path | N/A | os.path.join(logik_projekt_config_dir, "rsync-templates") |
| `LOGIK-PROJEKT Rsync Template File` | N/A | `logik_projekt_rsync_template_file` | Yes | Calculated | N/A | f"{logik_projekt_rsync_template_dir}/rsync-template.sh" |
| `LOGIK-PROJEKT XML Template Dir` | N/A | `logik_projekt_xml_template_dir` | Yes | Static Path | N/A | os.path.join(logik_projekt_config_dir, "xml-templates") |
| `LOGIK-PROJEKT XML Template File` | N/A | `logik_projekt_xml_template_file` | Yes | Calculated | N/A | f"{logik_projekt_xml_template_dir}/fxml-template.xml" | -->
