# Data Map and Process Flow Analysis for LOGIK-PROJEKT

This document provides an analysis and validation of the data flow and process implementation as described in the following data map files:
1.  [`data_map-template_info.md`](data_map-template_info.md)
2.  [`data_map-template_parameters.md`](data_map-template_parameters.md)
3.  [`data_map-template_summary.md`](data_map-template_summary.md)
4.  [`data_map-projekt_template.md`](data_map-projekt_template.md)
5.  [`data_map-flame_options.md`](data_map-flame_options.md)
6.  [`data_map-projekt_summary.md`](data_map-projekt_summary.md)

## Overall Process Flow

The LOGIK-PROJEKT application's data flow can be broadly categorized into two main phases:

1.  **Template Creation and Export:** User input is gathered to define a Flame project template. This data is consolidated and then exported into a JSON file.
2.  **Project Configuration and Summary:** An existing template (imported from a JSON file) is combined with real-time user selections (Flame software options) and system environment variables to form a comprehensive project configuration. This configuration is then summarized for user review before project creation.

## Detailed Analysis of Each Data Map

### 1. `template_info_data_map.md`
*   **Purpose:** Gathers basic identifying information for a new LOGIK-PROJEKT template.
*   **Data Flow:** Direct user inputs for `template_serial_number`, `template_client_name`, `template_campaign_name`, and `template_description`. The `template_calculated_name` is a calculated field, derived by combining the `Serial Number`, `Client Name`, and `Campaign Name` fields, separated by underscores (e.g., `SN_CLIENT_CAMPAIGN`).
*   **Validation:** The data capture and calculation logic are clear and appropriate for generating a unique template identifier.

### 2. `template_parameters_data_map.md`
*   **Purpose:** Defines the technical specifications for the Flame project template.
*   **Data Flow:** Direct user inputs (combobox selections) for `template_resolution`, `template_bit_depth`, `template_framerate`, `template_scan_mode`, `template_start_frame`, `template_init_config`, `template_ocio_config`, `template_cache_integer`, and `template_cache_float`.
    *   Calculated fields: `template_resolution_w`, `template_resolution_h`, and `template_aspect_ratio` are automatically populated based on the `template_resolution` selection.
    *   `template_ocio_path` is calculated from `template_ocio_config` by joining with `/opt/Autodesk/colour_mgmt/configs` and `config.ocio`.
    *   `template_ocio_name` is extracted from `template_ocio_config` via `WidgetOCIOConfig.get_ocio_name()`.
    *   `template_cache_integer_id` is extracted from `template_cache_integer` via `WidgetCacheInteger.template_get_code()`.
    *   `template_cache_float_id` is extracted from `template_cache_float` via `WidgetCacheFloat.template_get_code()`.
*   **Validation:** The data capture and derivation of calculated fields are logical and consistent with typical application behavior for technical specifications.

### 3. `template_summary_data_map.md`
*   **Purpose:** Provides a live, read-only summary of the data entered in the Info and Parameters panels, serving as the source for exporting the template to a JSON file.
*   **Data Flow:** Primarily consolidates data from `template_info_data_map.md` and `template_parameters_data_map.md`. Most fields are direct passthroughs, while calculated fields (e.g., `template_resolution_w`, `template_ocio_path`) maintain their derivation logic from the Parameters Panel.
*   **Validation:** This map correctly aggregates data for template export. The `JSON Key` column now accurately reflects how these variables map to the exported JSON template file, resolving previous discrepancies.

### 4. `projekt_template_data_map.md`
*   **Purpose:** Displays a summary of an *imported* project template, reflecting data from a `current_template.json` file.
*   **Data Flow:** All data originates from an "Imported JSON Template File." Fields like `projekt_serial_number`, `projekt_client_name`, `projekt_calculated_name`, etc., are directly mapped from their corresponding JSON keys.
    *   "Not Displayed" fields (e.g., `projekt_resolution`, `projekt_ocio_config`) represent raw imported values that are then parsed or transformed into more granular displayed fields (e.g., `projekt_resolution_w`, `projekt_resolution_h`).
*   **Validation:** This map confirms the successful import of template data. The use of `projekt_` prefix for imported data, distinct from the `template_` prefix used during creation, is a good convention. The explicit storage of derived values (like width, height, and aspect ratio) in the JSON, rather than just the resolution string, enhances robustness.

### 5. `flame_options_data_map.md`
*   **Purpose:** Gathers user-specified Flame-related settings, including software version and key project directory paths.
*   **Data Flow:** Direct user inputs for `flame_software_choice`, `flame_home_directory`, `flame_setups_directory`, `flame_media_directory`, `flame_catalog_directory`, and `logik_projekt_config`.
*   **Validation:** This map clearly defines the runtime configuration inputs. No internal calculations are performed here, as expected.

### 6. `projekt_summary_data_map.md`
*   **Purpose:** Consolidates and displays information from various parts of the application (user inputs, imported template data, system environment variables) to provide a final overview before project creation.
*   **Data Flow:**
    *   **Environment Data:** Sourced from system environment variables (e.g., `current_user`, `current_os`).
    *   **Flame Software Data:** `flame_software` is sourced from `flame_options_data_map.md`. Derived fields like `flame_software_name` and `flame_software_sanitized_version` are calculated from `flame_software`.
    *   **Flame Projekt Data (from Imported Template):** Fields like `flame_projekt_nickname`, `flame_projekt_description`, `flame_projekt_width`, etc., are sourced from `projekt_template_data_map.md`. `flame_projekt_name` is calculated from `flame_projekt_nickname` and `flame_software_sanitized_version`.
    *   **Flame Projekt Data (from Flame Options Panel):** Directory paths like `flame_projekt_home`, `flame_projekt_setups_dir` are sourced from `flame_options_data_map.md`.
    *   **LOGIK PROJEKT Data:** `logik_projekt_name` is typically the same as `flame_projekt_nickname`. `logik_projekt_path` is constructed as "/PROJEKTS/`logik_projekt_name`". `logik_projekt_config_name` is sourced from `flame_options_data_map.md`, and `logik_projekt_config_tree` is calculated from `logik_projekt_config_name`.
*   **Validation:** This map successfully integrates all disparate data sources, performing necessary calculations and transformations to present a comprehensive and coherent project configuration.

## Conclusion

The process and data flow described across these six data map files are logically sound and correctly implemented. The system demonstrates a clear and robust progression from initial template definition and export to the final consolidation of project configuration data for creation. The recent updates to the data maps have significantly improved their clarity, consistency, and completeness, particularly regarding JSON key mappings, calculation logic, and cross-referencing. This detailed documentation provides a strong foundation for understanding and maintaining the application's data architecture.
