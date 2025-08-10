# Projekt Template Data Map

This document analyzes the data displayed in the **Projekt Template** panel (`ProjektTemplatePanel`).

## Overview

This panel displays a summary of the project template that has been imported. It is a read-only view that reflects the data from the `current_template.json` file, which is loaded when a template is imported.

## Related Scripts

* [`src/ui/panels/projekt_template_panel.py`](<../src/ui/panels/projekt_template_panel.py>)

    * [`src/ui/widgets/display/projekt_template_widget.py`](<../src/ui/widgets/display/projekt_template_widget.py>)

| Field Name / Displayed Field / Label | Widget Class | Variable Name / Key | Is Displayed? | Data Source (Panel & Widget) | JSON Key | Notes |
|---|---|---|---|---|---|---|
| `Import LOGIK-PROJEKT Template` | `ImportTemplateWidget` | N/A | Yes | User Interaction | N/A | Button to trigger template import. |
| (Not Displayed) | `ProjektTemplateWidget` | `projekt_serial_number` | No | Imported JSON Template File | `Template Serial Number:` | Mapped from JSON key during import. Corresponds to `template_serial_number` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| (Not Displayed) | `ProjektTemplateWidget` | `projekt_client_name` | No | Imported JSON Template File | `Template Client Name:` | Mapped from JSON key during import. Corresponds to `template_client_name` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| (Not Displayed) | `ProjektTemplateWidget` | `projekt_campaign_name` | No | Imported JSON Template File | `Template Campaign Name:` | Mapped from JSON key during import. Corresponds to `template_campaign_name` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| `Projekt Name:` | `ProjektTemplateWidget` | `projekt_calculated_name` | Yes | Imported JSON Template File | `Template Name:` | Mapped from JSON key during import. Corresponds to `template_calculated_name` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| `Projekt Description:` | `ProjektTemplateWidget` | `projekt_description` | Yes | Imported JSON Template File | `Template Description:` | Mapped from JSON key during import. Corresponds to `template_description` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| (Not Displayed) | `ProjektTemplateWidget` | `projekt_resolution` | No | Imported JSON Template File | `Template Resolution:` | Mapped from JSON key during import. Raw value from JSON; parsed into `projekt_resolution_w`, `projekt_resolution_h`, and `projekt_aspect_ratio` for display. Corresponds to `template_resolution` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| `Projekt Width:` | `ProjektTemplateWidget` | `projekt_resolution_w` | Yes | Imported JSON Template File | `Template Width:` | Mapped from JSON key during import. Corresponds to `template_resolution_w` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| `Projekt Height:` | `ProjektTemplateWidget` | `projekt_resolution_h` | Yes | Imported JSON Template File | `Template Height:` | Mapped from JSON key during import. Corresponds to `template_resolution_h` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| `Projekt Aspect Ratio:` | `ProjektTemplateWidget` | `projekt_aspect_ratio` | Yes | Imported JSON Template File | `Template Aspect Ratio:` | Mapped from JSON key during import. Corresponds to `template_aspect_ratio` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| `Projekt Bit Depth:` | `ProjektTemplateWidget` | `projekt_bit_depth` | Yes | Imported JSON Template File | `Template Bit Depth:` | Mapped from JSON key during import. Corresponds to `template_bit_depth` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| `Projekt Framerate:` | `ProjektTemplateWidget` | `projekt_framerate` | Yes | Imported JSON Template File | `Template Framerate:` | Mapped from JSON key during import. Corresponds to `template_framerate` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| `Projekt Scan Mode:` | `ProjektTemplateWidget` | `projekt_scan_mode` | Yes | Imported JSON Template File | `Template Scan Mode:` | Mapped from JSON key during import. Corresponds to `template_scan_mode` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| `Projekt Start Frame:` | `ProjektTemplateWidget` | `projekt_start_frame` | Yes | Imported JSON Template File | `Template Start Frame:` | Mapped from JSON key during import. Corresponds to `template_start_frame` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| `Projekt Init Config:` | `ProjektTemplateWidget` | `projekt_init_config` | Yes | Imported JSON Template File | `Template Init Config:` | Mapped from JSON key during import. Corresponds to `template_init_config` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| (Not Displayed) | `ProjektTemplateWidget` | `projekt_ocio_config` | No | Imported JSON Template File | `Template OCIO Config:` | Mapped from JSON key during import. Raw value from JSON; `projekt_ocio_name` is extracted for display. Corresponds to `template_ocio_config` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| (Not Displayed) | `ProjektTemplateWidget` | `projekt_ocio_path` | No | Imported JSON Template File | `Template OCIO Path:` | Mapped from JSON key during import. Corresponds to `template_ocio_path` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| `Projekt OCIO Name:` | `ProjektTemplateWidget` | `projekt_ocio_name` | Yes | Imported JSON Template File | `Template OCIO Name:` | Mapped from JSON key during import. Corresponds to `template_ocio_name` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| (Not Displayed) | `ProjektTemplateWidget` | `projekt_cache_integer` | No | Imported JSON Template File | `Template Cache Integer:` | Mapped from JSON key during import. Raw value from JSON; `projekt_cache_integer_id` is extracted for display. Corresponds to `template_cache_integer` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| `Projekt Cache Integer ID:` | `ProjektTemplateWidget` | `projekt_cache_integer_id` | Yes | Imported JSON Template File | `Template Cache Integer ID:` | Mapped from JSON key during import. Corresponds to `template_cache_integer_id` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| (Not Displayed) | `ProjektTemplateWidget` | `projekt_cache_float` | No | Imported JSON Template File | `Template Cache Float:` | Mapped from JSON key during import. Raw value from JSON; `projekt_cache_float_id` is extracted for display. Corresponds to `template_cache_float` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
| `Projekt Cache Float ID:` | `ProjektTemplateWidget` | `projekt_cache_float_id` | Yes | Imported JSON Template File | `Template Cache Float ID:` | Mapped from JSON key during import. Corresponds to `template_cache_float_id` from `template_summary_data_map.md`. Data flows to `projekt_summary_data_map.md`. |
