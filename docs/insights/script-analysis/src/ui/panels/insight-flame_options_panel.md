# Insight: `flame_options_panel.py`

## 1. Widget Type

`FlameOptionsPanel` is a composite `QWidget` that serves as a dedicated panel for configuring Autodesk Flame-related settings. It uses a `QGridLayout` to organize various sub-widgets, including `QComboBox`es and custom button widgets for directory selection.

## 2. Purpose

This panel allows users to define critical parameters for a new Flame project, such as the specific Flame software version to use, and the various directory paths (home, setups, media, catalog) that Flame will utilize. It also includes a selection for the overall LOGIK-PROJEKT configuration.

## 3. Behavior and Functionality

- **Initialization and Layout:** The panel initializes its layout using `QGridLayout`, setting up consistent spacing and column stretching. It creates instances of several custom widgets for user input.
- **Dynamic Population:** Upon initialization, it populates the `FlameSoftwareChoiceWidget` with detected Flame versions and the `ProjektConfigWidget` with available LOGIK-PROJEKT configurations by calling external `get` functions.
- **Directory Selection:** It provides dedicated methods (`_select_flame_home_dir`, etc.) that are connected to the custom button widgets. These methods open `QFileDialog` instances to allow users to graphically select directories.
- **Data Retrieval:** The `get_flame_options()` method collects all the selected values and paths from its child widgets and returns them as a dictionary, ready for use by the main application logic.
- **Data Setting:** The `set_flame_options(options)` method allows for programmatically populating the panel's widgets with data from a dictionary, useful for loading saved project settings or templates.
- **Signal Emission:** It emits a custom `path_changed` signal whenever a directory path or a combobox selection changes, notifying other parts of the application that the project configuration might need to be re-evaluated.

## 4. Key Attributes and Properties

- `self.flame_software_choice_widget`: An instance of `FlameSoftwareChoiceWidget`.
- `self.flame_home_dir_widget`: An instance of `FlameHomeDirWidget`.
- `self.flame_setups_dir_widget`: An instance of `FlameSetupsDirWidget`.
- `self.flame_media_dir_widget`: An instance of `FlameMediaDirWidget`.
- `self.flame_catalog_dir_widget`: An instance of `FlameCatalogDirWidget`.
- `self.logik_projekt_config_widget`: An instance of `ProjektConfigWidget`.
- `self.path_changed`: A custom `Signal` emitted when relevant paths or selections change.

## 5. Signals and Slots

- **Custom Signals:**
  - `path_changed`: Emitted when any of the directory paths or combobox selections within the panel are modified. This signal is crucial for triggering updates in summary panels or other dependent logic.
- **Internal Slots:**
  - `_select_flame_home_dir()`, `_select_flame_setups_dir()`, `_select_flame_media_dir()`, `_select_flame_catalog_dir()`: Slots connected to the `clicked` signals of the respective directory selection buttons.
  - `_emit_path_changed()`: A helper slot connected to the `currentIndexChanged` signals of the comboboxes to emit the `path_changed` signal.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: Imports `ui_config` for consistent layout and spacing parameters (`PANEL_LAYOUT_SPACING`, `PANEL_PADDING`).
- **Custom Widgets (from `src/ui/widgets/combobox` and `src/ui/widgets/button`)**: This panel heavily relies on and composes several custom widgets, demonstrating a modular UI design approach.
- **Core Functions (from `src/core/functions/get/`)**: It directly calls various `get_sysconfig_*_dir` and `get_installed_flame_versions` functions to retrieve default paths and available software versions. It also uses `get_logik_projekt_config_values` to populate the project configuration combobox.
- **`AppLogic` (or main application controller)**: This panel acts as a data source for the main application logic. `AppLogic` would call `get_flame_options()` to retrieve the user's selections and use them for project creation. Conversely, `AppLogic` might call `set_flame_options()` to load default or template-based settings into the panel.
- **`ProjektSummaryWidget`**: The `path_changed` signal from this panel would likely be connected to a slot in `AppLogic` that updates the `ProjektSummaryWidget` to reflect the chosen Flame options.

## 7. UI/UX Notes

This panel provides a clear and organized interface for configuring complex Flame-related settings. The use of dedicated widgets for each input type (comboboxes for selection, buttons for directory picking) enhances usability. The dynamic population of options and the real-time updates (via `path_changed` signal) contribute to a responsive and intuitive user experience. The panel's structure makes it easy for users to understand and manage the various paths and software versions involved in their Flame projects.