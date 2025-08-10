# Template Summary Data Map

This document analyzes the data displayed in the **Template Summary** widget located on the left-hand panel (`LeftSubPanelTemplateSummary`).

## Overview

This widget provides a live, read-only summary of the data entered by the user in the three main template configuration panels above it: **Info**, **Parameters**, and **Cache**. It gathers all the values from these panels and displays them in a consolidated view, which is then used for exporting the template to a JSON file.

## Related Scripts

* [`src/ui/panels/template_summary_panel.py`](<../src/ui/panels/template_summary_panel.py>)

    * [`src/ui/panels/template_info_panel.py`](<../src/ui/panels/template_info_panel.py>)
    * [`src/ui/panels/template_parameters_panel.py`](<../src/ui/panels/template_parameters_panel.py>)
    * [`src/ui/widgets/display/template_summary_widget.py`](<../src/ui/widgets/display/template_summary_widget.py>)
    * [`src/ui/widgets/button/export_template_widget.py`](<../src/ui/widgets/button/export_template_widget.py>)

| Field Name / Displayed Field / Label | Widget Class | Variable Name / Key | Is Displayed? | Data Source (Panel & Widget) | JSON Key | Notes |
|---|---|---|---|---|---|---|
| `Template Serial #:` | `TemplateSummaryWidget` | `template_serial_number` | Yes | `TemplateSummaryPanel` (`set_template_summary_panel_data`) | `template_serial_number` | From user input. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| `Template Client:` | `TemplateSummaryWidget` | `template_client_name` | Yes | `TemplateSummaryPanel` (`set_template_summary_panel_data`) | `template_client_name` | From user input. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| `Template Campaign:` | `TemplateSummaryWidget` | `template_campaign_name` | Yes | `TemplateSummaryPanel` (`set_template_summary_panel_data`) | `template_campaign_name` | From user input. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| `Template Name:` | `TemplateSummaryWidget` | `template_calculated_name` | Yes | `TemplateSummaryPanel` (`set_template_summary_panel_data`) | `template_calculated_name` | Calculated from `template_serial_number`, `template_client_name`, and `template_campaign_name` (e.g., `SN_CLIENT_CAMPAIGN`). Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| `Template Description:` | `TemplateSummaryWidget` | `template_description` | Yes | `src/ui/panels/template_info_panel.py` (`get_template_info`) | `template_description` | From user input. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| `Template Resolution:` | `TemplateSummaryWidget` | `template_resolution` | Yes | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `Template Resolution:` | From user input. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| `Template Width:` | `TemplateSummaryWidget` | `template_resolution_w` | Yes | `TemplateSummaryPanel` (`set_template_summary_panel_data`) | `template_resolution_w` | Calculated from `template_resolution`. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| `Template Height:` | `TemplateSummaryWidget` | `template_resolution_h` | Yes | `TemplateSummaryPanel` (`set_template_summary_panel_data`) | `template_resolution_h` | Calculated from `template_resolution`. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| `Template Aspect Ratio:` | `TemplateSummaryWidget` | `template_aspect_ratio` | Yes | `TemplateSummaryPanel` (`set_template_summary_panel_data`) | `template_aspect_ratio` | Calculated from `template_resolution`. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| `Template Bit Depth:` | `TemplateSummaryWidget` | `template_bit_depth` | Yes | `TemplateSummaryPanel` (`set_template_summary_panel_data`) | `template_bit_depth` | From user input. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| `Template Framerate:` | `TemplateSummaryWidget` | `template_framerate` | Yes | `TemplateSummaryPanel` (`set_template_summary_panel_data`) | `template_framerate` | From user input. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| `Template Scan Mode:` | `TemplateSummaryWidget` | `template_scan_mode` | Yes | `TemplateSummaryPanel` (`set_template_summary_panel_data`) | `template_scan_mode` | From user input. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| `Template Start Frame:` | `TemplateSummaryWidget` | `template_start_frame` | Yes | `TemplateSummaryPanel` (`set_template_summary_panel_data`) | `template_start_frame` | From user input. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| `Template Init Config:` | `TemplateSummaryWidget` | `template_init_config` | Yes | `TemplateSummaryPanel` (`set_template_summary_panel_data`) | `template_init_config` | From user input. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| (Not Displayed) | N/A | `template_ocio_config` | No | `TemplateSummaryPanel` (`set_template_summary_panel_data`) | `template_ocio_config` | The full OCIO config string. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| (Not Displayed) | N/A | `template_ocio_path` | No | `TemplateSummaryPanel` (`set_template_summary_panel_data`) | `template_ocio_path` | Calculated by joining `/opt/Autodesk/colour_mgmt/configs` with the value of `template_ocio_config` and `config.ocio`. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| `Template OCIO Name:` | `TemplateSummaryWidget` | `template_ocio_name` | Yes | `TemplateSummaryPanel` (`set_template_summary_panel_data`) | `template_ocio_name` | Extracted from `template_ocio_config` via `WidgetOCIOConfig.get_ocio_name()`. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| (Not Displayed) | N/A | `template_cache_integer` | No | `TemplateSummaryPanel` (`set_template_summary_panel_data`) | `template_cache_integer` | The full integer cache string. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| `Template Cache Integer ID:` | `TemplateSummaryWidget` | `template_cache_integer_id` | Yes | `TemplateSummaryPanel` (`set_template_summary_panel_data`) | `template_cache_integer_id` | Calculated from `template_cache_integer`. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| (Not Displayed) | N/A | `template_cache_float` | No | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `template_cache_float` | The full float cache string. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| `Template Cache Float ID:` | `TemplateSummaryWidget` | `template_cache_float_id` | Yes | `src/ui/panels/template_parameters_panel.py` (`get_template_parameters`) | `template_cache_float_id` | Calculated from `template_cache_float`. Data flows to `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`). |
| `Export LOGIK-PROJEKT Template` | `ExportTemplateWidget` | N/A | Yes | User Interaction | N/A | Button to trigger template export. |