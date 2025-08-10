# Static Analysis: `src/ui/panels/template_parameters_panel.py`

## Overview
The `TemplateParametersPanel` class is a `QWidget` (from PySide6) that provides a user interface for configuring various technical parameters related to a template, such as resolution, bit depth, frame rate, scan mode, and OCIO configuration. It dynamically populates comboboxes with predefined values and updates related fields based on user selections.

## Dependencies
- **PySide6.QtWidgets**: `QWidget`, `QGridLayout`
- **Local Modules (src.ui)**:
    - `src.ui.ui_config`: Used for layout spacing and padding (`PANEL_LAYOUT_SPACING`, `PANEL_PADDING`).
    - `src.core.utils.ocio_utils`: Used to retrieve OCIO details from a relative path.
    - **Combobox Widgets (from `src.ui.widgets.combobox`)**:
        - `ResolutionWidget`
        - `BitDepthWidget`
        - `FrameRateWidget`
        - `ScanModeWidget`
        - `StartFrameWidget`
        - `InitConfigWidget`
        - `OcioConfigWidget`
        - `CacheIntegerWidget`
        - `CacheFloatWidget`
    - **Entry Widgets (from `src.ui.widgets.entry`)**:
        - `ResolutionWidthWidget`
        - `ResolutionHeightWidget`
        - `AspectRatioWidget`
    - **Loader Functions (from `src.core.loaders`)**:
        - `load_resolution_values`
        - `get_bit_depth_values`
        - `load_frame_rate_values`
        - `load_scan_mode_values`
        - `load_start_frame_values`
        - `load_init_config_values`
        - `load_ocio_config_values`
        - `get_cache_integer_values`
        - `get_cache_float_values`

## Class: `TemplateParametersPanel`

### Purpose
This panel allows users to define and modify technical specifications for a project template, ensuring consistency and adherence to production standards. It integrates with various data loaders to provide a curated list of options for each parameter.

### Initialization (`__init__`)
- Inherits from `PySide6.QtWidgets.QWidget`.
- Takes `master` (parent widget) and `app_logic` as arguments.
- Stores `app_logic` as an instance variable (though its direct use isn't immediately apparent in the provided code snippet).
- Initializes a `QGridLayout` for the panel, setting spacing and margins using `ui_config`.
- Instantiates all combobox and entry widgets.
- Configures column widths for the layout: Column 0 for labels (fixed width 160px), Column 1 for widgets (stretches).
- Adds widgets to the layout in a loop, placing labels in column 0 and their corresponding combobox/entry in column 1.
- Initializes `cache_integer_id` and `cache_float_id` to `None`.
- Populates all comboboxes with values loaded from respective `load_*_values()` functions.
- Connects `currentIndexChanged` signals of `resolution_widget`, `cache_integer_widget`, and `cache_float_widget` to update methods.
- Performs initial updates for calculated fields by calling `_update_resolution_fields()`, `_update_cache_integer_id()`, and `_update_cache_float_id()`.

### Methods

#### `_update_resolution_fields()`
- Triggered when the selected resolution changes.
- Retrieves the `selected_resolution_data` from `resolution_widget`.
- If data is available, it extracts `width`, `height`, and `aspect_ratio` and sets these values in the corresponding `resolution_width_widget`, `resolution_height_widget`, and `aspect_ratio_widget`.
- If no data, it clears these fields.

#### `_update_cache_integer_id()`
- Triggered when the selected cache integer value changes.
- Updates the `self.cache_integer_id` instance variable with the current value from `cache_integer_widget`.

#### `_update_cache_float_id()`
- Triggered when the selected cache float value changes.
- Updates the `self.cache_float_id` instance variable with the current value from `cache_float_widget`.

#### `get_template_parameters()`
- Returns a dictionary containing all the selected template parameters.
- Retrieves values from all combobox and entry widgets.
- Uses `ocio_utils.get_ocio_details_from_relative_path()` to get the OCIO name and path based on the selected OCIO configuration.
- Includes both the display text and the internal ID for cache integer and float values.

#### `set_template_parameters(params)`
- Takes a `params` dictionary as input.
- Sets the values of all combobox and entry widgets based on the provided dictionary. It uses `.get()` with an empty string or 0 as a default to prevent errors if a key is missing.
- Calls `_update_resolution_fields()` after setting parameters to ensure dependent fields are correctly updated.

## Observations
- The panel is highly modular, relying on numerous specialized widgets for each parameter type.
- Data loading for comboboxes is externalized to `src.core.loaders`, promoting separation of concerns and potentially allowing for dynamic or configurable options.
- The `_update_resolution_fields` method demonstrates a clear dependency between the `resolution_widget` and the `resolution_width_widget`, `resolution_height_widget`, and `aspect_ratio_widget`.
- The `get_template_parameters` and `set_template_parameters` methods provide a comprehensive interface for reading and writing all panel data, making it easy to integrate with application logic for saving and loading template configurations.
- The use of `ocio_utils` indicates integration with OpenColorIO configurations, which is crucial for color management in visual effects workflows.
