# LOGIK-PROJEKT Data Flow Analysis

This document provides a consolidated overview of the data flow within the LOGIK-PROJEKT application, tracing variables and their transformations across different panels and components.

## Data Flow Summary

### 1. Template Info Panel (`src/ui/panels/template_info_panel.py`)

| Variable Name / Key | Data Source | Data Flow To |
|---|---|---|
| `template_serial_number` | `src/ui/widgets/entry/serial_number_widget.py` (User Input) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_client_name` | `src/ui/widgets/entry/client_name_widget.py` (User Input) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_campaign_name` | `src/ui/widgets/entry/campaign_name_widget.py` (User Input) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_calculated_name` | `src/ui/widgets/entry/calculated_name_widget.py` (Calculated) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_description` | `src/ui/widgets/entry/description_widget.py` (User Input) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |

### 2. Template Parameters Panel (`src/ui/panels/template_parameters_panel.py`)

| Variable Name / Key | Data Source | Data Flow To |
|---|---|---|
| `template_resolution` | `src/ui/widgets/combobox/resolution_widget.py` (User Input) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_resolution_w` | `src/ui/widgets/entry/resolution_width_widget.py` (Calculated) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_resolution_h` | `src/ui/widgets/entry/resolution_height_widget.py` (Calculated) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_aspect_ratio` | `src/ui/widgets/entry/aspect_ratio_widget.py` (Calculated) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_bit_depth` | `src/ui/widgets/combobox/bit_depth_widget.py` (User Input) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_framerate` | `src/ui/widgets/combobox/frame_rate_widget.py` (User Input) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_scan_mode` | `src/ui/widgets/combobox/scan_mode_widget.py` (User Input) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_start_frame` | `src/ui/widgets/combobox/start_frame_widget.py` (User Input) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_init_config` | `src/ui/widgets/combobox/init_config_widget.py` (User Input) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_ocio_config` | `src/ui/widgets/combobox/ocio_config_widget.py` (User Input) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_ocio_path` | `src/ui/panels/template_parameters_panel.py` (Calculated) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_ocio_name` | `src/ui/panels/template_parameters_panel.py` (Calculated) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_cache_integer` | `src/ui/widgets/combobox/cache_integer_widget.py` (User Input) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_cache_integer_id` | `src/ui/panels/template_parameters_panel.py` (Calculated) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_cache_float` | `src/ui/widgets/combobox/cache_float_widget.py` (User Input) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |
| `template_cache_float_id` | `src/ui/panels/template_parameters_panel.py` (Calculated) | `src/ui/panels/template_summary_panel.py` (`set_summary_data`), `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`) |

### 3. Template Summary Panel (`src/ui/panels/template_summary_panel.py`)

| Variable Name / Key | Data Source | Data Flow To |
|---|---|---|
| `template_serial_number` | `src/ui/panels/template_info_panel.py` (`get_template_info`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_client_name` | `src/ui/panels/template_info_panel.py` (`get_template_info`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_campaign_name` | `src/ui/panels/template_info_panel.py` (`get_template_info`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_calculated_name` | `src/ui/panels/template_info_panel.py` (`get_template_info`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_description` | `src/ui/panels/template_info_panel.py` (`get_template_info`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_resolution` | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_resolution_w` | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_resolution_h` | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_aspect_ratio` | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_bit_depth` | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_framerate` | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_scan_mode` | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_start_frame` | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_init_config` | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_ocio_config` | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_ocio_path` | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_ocio_name` | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_cache_integer` | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_cache_integer_id` | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_cache_float` | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |
| `template_cache_float_id` | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`) |

### 4. Projekt Template Panel (`src/ui/panels/projekt_template_panel.py`)

| Variable Name / Key | Data Source | Data Flow To |
|---|---|---|
| `projekt_serial_number` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_client_name` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_campaign_name` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_calculated_name` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_description` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_resolution` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_resolution_w` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_resolution_h` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_aspect_ratio` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_bit_depth` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_framerate` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_scan_mode` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_start_frame` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_init_config` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_ocio_config` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_ocio_path` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_ocio_name` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_cache_integer` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_cache_integer_id` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_cache_float` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `projekt_cache_float_id` | `src/core/app_logic.py` (`import_logik_projekt_template`) | `src/core/app_logic.py` (`get_projekt_summary_data`) |

### 5. Flame Options Panel (`src/ui/panels/flame_options_panel.py`)

| Variable Name / Key | Data Source | Data Flow To |
|---|---|---|
| `flame_software_choice` | `src/ui/widgets/combobox/flame_software_choice_widget.py` (User Input) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `flame_home_directory` | `src/ui/widgets/button/flame_home_dir_widget.py` (User Input) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `flame_setups_directory` | `src/ui/widgets/button/flame_setups_dir_widget.py` (User Input) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `flame_media_directory` | `src/ui/widgets/button/flame_media_dir_widget.py` (User Input) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `flame_catalog_directory` | `src/ui/widgets/button/flame_catalog_dir_widget.py` (User Input) | `src/core/app_logic.py` (`get_projekt_summary_data`) |
| `logik_projekt_config_name` | `src/ui/widgets/combobox/projekt_config_widget.py` (User Input) | `src/core/app_logic.py` (`get_projekt_summary_data`) |

### 6. Projekt Summary Panel (`src/ui/panels/projekt_summary_panel.py`)

| Variable Name / Key | Data Source | Data Flow To |
|---|---|---|
| `current_user` | `src/core/utils/system_info_utils.py` (`get_current_user`) | N/A (End of Flow) |
| `current_group` | `src/core/utils/system_info_utils.py` (`get_primary_group`) | N/A (End of Flow) |
| `current_workstation` | `src/core/utils/system_info_utils.py` (`get_short_hostname`) | N/A (End of Flow) |
| `current_os` | System Environment (Python `platform` module) | N/A (End of Flow) |
| `flame_software_choice` | `src/ui/panels/flame_options_panel.py` (`get_flame_options`) | N/A (End of Flow) |
| `flame_software_name` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_software_version` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_software_sanitized_name` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_software_sanitized_version` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_name` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_nickname` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_shotgun_name` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_description` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_home` | `src/ui/panels/flame_options_panel.py` (`get_flame_options`) | N/A (End of Flow) |
| `flame_projekt_setups_dir` | `src/ui/panels/flame_options_panel.py` (User Input / Default from `sysconfig.cfg`) | N/A (End of Flow) |
| `flame_projekt_media_dir` | `src/ui/panels/flame_options_panel.py` (User Input / Default from `sysconfig.cfg`) | N/A (End of Flow) |
| `flame_projekt_catalog_dir` | `src/ui/panels/flame_options_panel.py` (User Input / Default from `sysconfig.cfg`) | N/A (End of Flow) |
| `flame_projekt_width` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_height` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_ratio` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_depth` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_rate` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_mode` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_start` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_init` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_ocio` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_ocio_path` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_ocio_name` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_cachef` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_cachef_id` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_cachei` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `flame_projekt_cachei_id` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `logik_projekt_name` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `logik_projekt_path` | `src/core/app_logic.py` (`get_projekt_summary_data`) | N/A (End of Flow) |
| `logik_projekt_config_name` | `src/ui/panels/flame_options_panel.py` (`get_flame_options`) | N/A (End of Flow) |
| `logik_projekt_config_tree` | `src/ui/panels/flame_options_panel.py` (User Input) | N/A (End of Flow) |
| `logik_projekt_config_bookmarks` | `src/ui/panels/flame_options_panel.py` (User Input) | N/A (End of Flow) |
| `logik_projekt_config_workspace` | `src/ui/panels/flame_options_panel.py` (User Input) | N/A (End of Flow) |