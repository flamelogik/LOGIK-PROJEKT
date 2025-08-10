# Static Analysis: `src/core/functions/get/get_projekt_summary_data.py`

## Overview
The `get_projekt_summary_data.py` script defines a function that compiles various pieces of information related to a project into a single, comprehensive dictionary. This includes environment details, Flame software data, and LOGIK-PROJEKT configurations, derived from user inputs and system queries.

## Dependencies
- **Local Modules (src.core.template_manager)**:
    - `src.core.template_manager.template_models.TemplateInfo`
    - `src.core.template_manager.template_models.TemplateParameters`
- **Local Modules (src.core.utils)**:
    - `src.core.utils.system_info_utils.get_current_user`
    - `src.core.utils.system_info_utils.get_primary_group`
    - `src.core.utils.system_info_utils.get_short_hostname`
    - `src.core.utils.flame_software_utils.get_installed_flame_versions`
    - `src.core.utils.flame_software_utils.sanitize_flame_version_name`
    - `src.core.utils.flame_software_utils.sanitize_flame_version_number`
    - `src.core.utils.ocio_utils`

## Function: `get_projekt_summary_data(template_info: TemplateInfo, template_parameters: TemplateParameters, flame_options_data: dict) -> dict`

### Purpose
To consolidate all relevant data for a new project, including user inputs, system information, and Flame-specific configurations, into a single dictionary that can be used for project creation and display.

### Arguments
- `template_info` (TemplateInfo): An object containing general template information (e.g., serial number, client, campaign, calculated name, description).
- `template_parameters` (TemplateParameters): An object containing technical template parameters (e.g., resolution, bit depth, frame rate, OCIO config, cache settings).
- `flame_options_data` (dict): A dictionary containing Flame-specific configuration options (e.g., software choice, home, setups, media, catalog directories).

### Logic
1.  **Environment Data**: Retrieves current user, primary group, workstation hostname, and sets the OS to "linux" (placeholder for actual detection).
2.  **Flame Software Data**: 
    - Extracts `flame_software_choice` from `flame_options_data`.
    - Parses `flame_software_choice` to extract `flame_software_name` (e.g., "flame") and `flame_software_version` (e.g., "2026.1").
    - Sanitizes the software name and version using `sanitize_flame_version_name` and `sanitize_flame_version_number`.
3.  **Flame Projekt Data**: 
    - Constructs `flame_projekt_name` (e.g., `calculated_name_2026_1_workstation_name`).
    - Sets `flame_projekt_nickname` and `flame_projekt_shotgun_name` to `template_info.template_calculated_name`.
    - Sets `flame_projekt_description` to `template_info.template_description`.
    - Resolves Flame directory paths (`flame_projekt_home`, `flame_projekt_setups_dir`, `flame_projekt_media_dir`, `flame_projekt_catalog_dir`) based on `flame_options_data` and specific rules (e.g., replacing `<project home>` with the actual home directory).
    - Extracts various Flame project parameters (width, height, ratio, depth, rate, mode, start, init, ocio, cache) directly from `template_parameters`.
    - Retrieves OCIO details (name and path) using `ocio_utils.get_ocio_details_from_relative_path`.
4.  **LOGIK PROJEKT Data**: 
    - Sets `logik_projekt_name` to `template_info.template_calculated_name`.
    - Constructs `logik_projekt_path` (e.g., `/PROJEKTS/calculated_name`).
    - Extracts `logik_projekt_config_name`, `logik_projekt_config_tree`, `logik_projekt_config_bookmarks`, and `logik_projekt_config_workspace` from `flame_options_data.get("logik_projekt_config", {})`.
5.  **Return Summary**: Returns a dictionary containing all the compiled data, with clearly defined keys for each piece of information.

### Returns
- `dict`: A comprehensive dictionary containing all generated and collected project summary data.

## Observations
- This function is a central data aggregation point, combining information from various sources (user input, system, Flame configuration) into a single, structured output.
- It demonstrates complex string formatting and path resolution logic to generate Flame-specific project names and directory paths.
- The function relies heavily on helper utilities (`system_info_utils`, `flame_software_utils`, `ocio_utils`) to abstract away system-specific details.
- The use of `TemplateInfo` and `TemplateParameters` dataclasses ensures type safety and clear data structures for input parameters.
- The output dictionary is designed to be consumed by other parts of the application, such as the `ProjektSummaryPanel` for display and the `ProjektCreator` for actual project setup.