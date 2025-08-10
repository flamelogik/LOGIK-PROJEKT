# Template Parameters Data Map

This document analyzes the data fields in the **Template Parameters** panel (`TemplateParametersPanel`).

## Overview

This panel is responsible for gathering the technical parameters for a new LOGIK-PROJEKT template. It features various combobox and entry fields for the user to select and fill in.

## Related Scripts

* [`src/ui/panels/template_parameters_panel.py`](<../src/ui/panels/template_parameters_panel.py>)

    * [`src/ui/widgets/combobox/resolution_widget.py`](<../src/ui/widgets/combobox/resolution_widget.py>)
    * [`src/ui/widgets/entry/resolution_width_widget.py`](<../src/ui/widgets/entry/resolution_width_widget.py>)
    * [`src/ui/widgets/entry/resolution_height_widget.py`](<../src/ui/widgets/entry/resolution_height_widget.py>)
    * [`src/ui/widgets/entry/aspect_ratio_widget.py`](<../src/ui/widgets/entry/aspect_ratio_widget.py>)
    * [`src/ui/widgets/combobox/bit_depth_widget.py`](<../src/ui/widgets/combobox/bit_depth_widget.py>)
    * [`src/ui/widgets/combobox/frame_rate_widget.py`](<../src/ui/widgets/combobox/frame_rate_widget.py>)
    * [`src/ui/widgets/combobox/scan_mode_widget.py`](<../src/ui/widgets/combobox/scan_mode_widget.py>)
    * [`src/ui/widgets/combobox/start_frame_widget.py`](<../src/ui/widgets/combobox/start_frame_widget.py>)
    * [`src/ui/widgets/combobox/init_config_widget.py`](<../src/ui/widgets/combobox/init_config_widget.py>)
    * [`src/ui/widgets/combobox/ocio_config_widget.py`](<../src/ui/widgets/combobox/ocio_config_widget.py>)
    * [`src/ui/widgets/combobox/cache_integer_widget.py`](<../src/ui/widgets/combobox/cache_integer_widget.py>)
    * [`src/ui/widgets/combobox/cache_float_widget.py`](<../src/ui/widgets/combobox/cache_float_widget.py>)




## Data Map

| Field Name / Displayed Field / Label | Widget Class | Variable Name / Key | Is Displayed? | Data Source (Panel & Widget) | JSON Key | Notes |
|---|---|---|---|---|---|---|
| `Resolution:` | `ResolutionWidget` | `template_resolution` | Yes | User Input | `Template Resolution:` | Dropdown selection. Data flows to `src/ui/panels/template_summary_panel.py` (`set_template_summary_panel_data`) and `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`). |
| `Resolution Width:` | `ResolutionWidthWidget` | `template_resolution_w` | Yes | Calculated | `resolution_w` | Read-only field, calculated based on `Resolution` selection. Data flows to `src/ui/panels/template_summary_panel.py` (`set_template_summary_panel_data`) and `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`). |
| `Resolution Height:` | `ResolutionHeightWidget` | `template_resolution_h` | Yes | Calculated | `resolution_h` | Read-only field, calculated based on `Resolution` selection. Data flows to `src/ui/panels/template_summary_panel.py` (`set_template_summary_panel_data`) and `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`). |
| `Aspect Ratio:` | `AspectRatioWidget` | `template_aspect_ratio` | Yes | Calculated | `aspect_ratio` | Read-only field, calculated based on `Resolution` selection. Data flows to `src/ui/panels/template_summary_panel.py` (`set_template_summary_panel_data`) and `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`). |
| `Bit Depth:` | `BitDepthWidget` | `template_bit_depth` | Yes | User Input | `bit_depth` | Dropdown selection. Data flows to `src/ui/panels/template_summary_panel.py` (`set_template_summary_panel_data`) and `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`). |
| `Frame Rate:` | `FrameRateWidget` | `template_framerate` | Yes | User Input | `framerate` | Dropdown selection. Data flows to `src/ui/panels/template_summary_panel.py` (`set_template_summary_panel_data`) and `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`). |
| `Scan Mode:` | `ScanModeWidget` | `template_scan_mode` | Yes | User Input | `scan_mode` | Dropdown selection. Data flows to `src/ui/panels/template_summary_panel.py` (`set_template_summary_panel_data`) and `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`). |
| `Start Frame:` | `StartFrameWidget` | `template_start_frame` | Yes | User Input | `start_frame` | Dropdown selection. Data flows to `src/ui/panels/template_summary_panel.py` (`set_template_summary_panel_data`) and `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`). |
| `Init Config:` | `InitConfigWidget` | `template_init_config` | Yes | User Input | `init_config` | Dropdown selection. Data flows to `src/ui/panels/template_summary_panel.py` (`set_template_summary_panel_data`) and `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`). |
| `OCIO Config:` | `OcioConfigWidget` | `template_ocio_config` | Yes | User Input | `ocio_config` | Dropdown selection. Data flows to `src/ui/panels/template_summary_panel.py` (`set_template_summary_panel_data`) and `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`). |
| `OCIO Path:` | N/A | `template_ocio_path` | No | Calculated | `ocio_path` | Calculated based on `OCIO Config` selection. Data flows to `src/ui/panels/template_summary_panel.py` (`set_template_summary_panel_data`) and `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`). |
| `OCIO Name:` | N/A | `template_ocio_name` | No | Calculated | `ocio_name` | Calculated based on `OCIO Path` selection. Data flows to `src/ui/panels/template_summary_panel.py` (`set_template_summary_panel_data`) and `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`). |
| `Cache Integer:` | `CacheIntegerWidget` | `template_cache_integer` | Yes | User Input | `cache_integer` | Dropdown selection. Data flows to `src/ui/panels/template_summary_panel.py` (`set_template_summary_panel_data`) and `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`). |
| `Cache Integer ID:` | N/A | `template_cache_integer_id` | No | Calculated | `cache_integer_id` | Calculated based on `Cache Integer` selection. Data flows to `src/ui/panels/template_summary_panel.py` (`set_template_summary_panel_data`) and `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`). |
| `Cache Float:` | `CacheFloatWidget` | `template_cache_float` | Yes | User Input | `cache_float` | Dropdown selection. Data flows to `src/ui/panels/template_summary_panel.py` (`set_template_summary_panel_data`) and `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`). |
| `Cache Float ID:` | N/A | `template_cache_float_id` | No | Calculated | `cache_float_id` | Calculated based on `Cache Float` selection. Data flows to `src/ui/panels/template_summary_panel.py` (`set_template_summary_panel_data`) and `src/core/app_logic.py` (`get_projekt_summary_data`, `export_logik_projekt_template`, `import_logik_projekt_template`). |