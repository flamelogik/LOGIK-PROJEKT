# Insight: `template_parameters_panel.py`

## 1. Widget Type

`TemplateParametersPanel` is a composite `QWidget` that functions as a comprehensive input panel for various project parameters. It uses a `QGridLayout` to organize a multitude of custom combobox and entry widgets.

## 2. Purpose

This panel allows users to configure detailed technical parameters for a project template, including resolution, bit depth, frame rate, scan mode, start frame, initial configuration, OCIO settings, and cache formats. It centralizes all these critical settings in one place.

## 3. Behavior and Functionality

- **Widget Composition:** It instantiates and arranges numerous custom widgets for selecting or displaying project parameters, such as `ResolutionWidget`, `BitDepthWidget`, `FrameRateWidget`, `OcioConfigWidget`, and their associated display widgets (`ResolutionWidthWidget`, `ResolutionHeightWidget`, `AspectRatioWidget`).
- **Dynamic Widget Population:** Upon initialization, it populates all its combobox widgets by calling various `get_*_values()` functions from `src/core/functions/get/`, ensuring that the user is presented with valid and up-to-date options.
- **Inter-Widget Communication:** It connects signals from certain widgets (e.g., `resolution_widget.combobox.currentIndexChanged`) to internal slots (`_update_resolution_fields`) to ensure that related display widgets (width, height, aspect ratio) are automatically updated when a resolution preset is selected.
- **Data Retrieval:** The `get_template_parameters()` method collects all the selected values from its child widgets and returns them as a comprehensive dictionary, including derived values like OCIO name and path, and cache integer/float IDs.
- **Data Setting:** The `set_template_parameters(params)` method allows for programmatically populating the panel's widgets with data from a dictionary, useful for loading saved template settings.
- **Signal Emission:** It emits a custom `parameters_updated` signal whenever any of its relevant child widgets' values change, notifying other parts of the application that the project parameters might need to be re-evaluated.

## 4. Key Attributes and Properties

- `self.resolution_widget`: An instance of `ResolutionWidget`.
- `self.bit_depth_widget`: An instance of `BitDepthWidget`.
- `self.frame_rate_widget`: An instance of `FrameRateWidget`.
- `self.scan_mode_widget`: An instance of `ScanModeWidget`.
- `self.start_frame_widget`: An instance of `StartFrameWidget`.
- `self.init_config_widget`: An instance of `InitConfigWidget`.
- `self.ocio_config_widget`: An instance of `OcioConfigWidget`.
- `self.cache_integer_widget`: An instance of `CacheIntegerWidget`.
- `self.cache_float_widget`: An instance of `CacheFloatWidget`.
- `self.resolution_width_widget`: An instance of `ResolutionWidthWidget`.
- `self.resolution_height_widget`: An instance of `ResolutionHeightWidget`.
- `self.aspect_ratio_widget`: An instance of `AspectRatioWidget`.
- `self.parameters_updated`: A custom `Signal` emitted when parameters change.

## 5. Signals and Slots

- **Custom Signals:**
  - `parameters_updated`: Emitted whenever a relevant parameter (e.g., resolution, frame rate, bit depth) changes. This signal is crucial for keeping summary panels and other dependent logic synchronized.
- **Internal Slots:**
  - `_update_resolution_fields()`: Connected to `resolution_widget.combobox.currentIndexChanged`. Updates the width, height, and aspect ratio display widgets based on the selected resolution preset.
  - `_update_cache_integer_id()`: Connected to `cache_integer_widget.combobox.currentIndexChanged`. Updates the internal `cache_integer_id`.
  - `_update_cache_float_id()`: Connected to `cache_float_widget.combobox.currentIndexChanged`. Updates the internal `cache_float_id`.
  - `_emit_parameters_updated()`: A helper slot connected to various child widget signals to emit the panel's `parameters_updated` signal.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: Imports `ui_config` for consistent layout and spacing parameters (`PANEL_LAYOUT_SPACING`, `PANEL_PADDING`).
- **Custom Widgets (from `src/ui/widgets/combobox` and `src/ui/widgets/entry`)**: This panel is a major composer of these custom widgets, demonstrating a highly modular UI architecture.
- **Core Functions (from `src/core/functions/get/`)**: It directly calls numerous `get_*_values()` functions to retrieve data for populating its comboboxes, separating data retrieval from UI presentation.
- **`src.core.utils.ocio_utils`**: Uses `ocio_utils.get_ocio_details_from_relative_path` to extract OCIO name and path from the selected OCIO configuration.
- **`AppLogic` (or main application controller)**: This panel is a primary source of detailed project parameters. `AppLogic` would call `get_template_parameters()` to retrieve the user's selections. Conversely, `AppLogic` might call `set_template_parameters()` to load default or template-based settings into the panel.
- **`ProjektSummaryPanel` and `TemplateSummaryPanel`**: The `parameters_updated` signal from this panel would likely be connected to a slot in `AppLogic` that updates these summary panels to reflect the chosen technical parameters.

## 7. UI/UX Notes

This panel provides a robust and user-friendly interface for configuring complex technical project parameters. The use of specialized widgets for each setting, combined with dynamic population and inter-widget updates, ensures data integrity and a smooth user experience. The ability to load and save these settings via `set_template_parameters()` and `get_template_parameters()` further enhances usability and workflow efficiency, especially for standardized project setups.