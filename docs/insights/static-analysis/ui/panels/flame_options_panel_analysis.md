# Static Analysis: `src/ui/panels/flame_options_panel.py`

## Overview
The `FlameOptionsPanel` class is a custom `QWidget` (from PySide6) that provides a user interface for configuring Autodesk Flame software options and directory paths. It allows users to select the Flame software version and specify various Flame-related directories.

## Dependencies
- **PySide6.QtWidgets**: `QWidget`, `QGridLayout`, `QFileDialog`
- **PySide6.QtCore**: `Signal`, `Slot`
- **Local Modules (src.ui)**:
    - `src.ui.ui_config`: For layout and spacing constants.
    - `src.ui.widgets.combobox.flame_software_choice_widget.FlameSoftwareChoiceWidget`
    - `src.ui.widgets.button.flame_home_dir_widget.FlameHomeDirWidget`
    - `src.ui.widgets.button.flame_setups_dir_widget.FlameSetupsDirWidget`
    - `src.ui.widgets.button.flame_media_dir_widget.FlameMediaDirWidget`
    - `src.ui.widgets.button.flame_catalog_dir_widget.FlameCatalogDirWidget`
    - `src.ui.widgets.combobox.projekt_config_widget.ProjektConfigWidget`
- **Local Modules (src.core.functions.get)**:
    - `src.core.functions.get.get_sysconfig_flame_home_dir.get_sysconfig_flame_home_dir`
    - `src.core.functions.get.get_sysconfig_flame_setups_dir.get_sysconfig_flame_setups_dir`
    - `src.core.functions.get.get_sysconfig_flame_media_dir.get_sysconfig_flame_media_dir`
    - `src.core.functions.get.get_sysconfig_flame_catalog_dir.get_sysconfig_flame_catalog_dir`
    - `src.core.functions.get.get_flame_software_versions.get_flame_software_versions`
    - `src.core.functions.get.get_logik_projekt_config_values.get_logik_projekt_config_values`

## Class: `FlameOptionsPanel`

### Purpose
To provide a dedicated panel within the application for users to configure Flame-specific settings, including software version and critical directory paths, and to retrieve these settings for project creation.

### Signals
- `path_changed`: Emitted when any of the directory paths or combobox selections are changed by the user.

### Initialization (`__init__`)
- Inherits from `PySide6.QtWidgets.QWidget`.
- Takes `master` (parent widget) and an optional `default_params` dictionary as arguments.
- Calls `_setup_layout()` to configure the panel's grid layout.
- Calls `_create_widgets()` to instantiate and add all UI components.
- Calls `_populate_widgets()` to fill comboboxes with initial data.

### Methods

#### `_setup_layout(self)`
- **Purpose**: Configures the `QGridLayout` for the panel.
- **Behavior**: Sets spacing and contents margins using `ui_config` constants. Sets column 0 (labels) to a minimum width of 160 pixels and column 1 (widgets) to stretch and take remaining space.

#### `_create_widgets(self)`
- **Purpose**: Instantiates and arranges all child widgets within the panel.
- **Behavior**: Creates instances of `FlameSoftwareChoiceWidget`, `FlameHomeDirWidget`, `FlameSetupsDirWidget`, `FlameMediaDirWidget`, `FlameCatalogDirWidget`, and `ProjektConfigWidget`. Adds their labels and main widgets to the `QGridLayout`. Connects the `currentIndexChanged` signal of the comboboxes to `_emit_path_changed`.

#### `_emit_path_changed(self)`
- **Purpose**: Emits the custom `path_changed` signal.
- **Behavior**: This slot is connected to changes in combobox selections, ensuring that external components (e.g., the main application window) are notified when Flame options are modified.

#### `_populate_widgets(self)`
- **Purpose**: Populates the comboboxes with data retrieved from backend functions.
- **Behavior**: Calls `get_flame_software_versions()` to get Flame versions and `get_logik_projekt_config_values()` to get project configuration values, then uses these to populate the respective comboboxes. Sets the default selected project configuration if `default_params` contains it.

#### `_select_flame_home_dir(self)`
- **Purpose**: Slot for the "Select Flame Home Directory" button.
- **Behavior**: Opens a `QFileDialog` to allow the user to select a directory. If a directory is selected, it updates the `FlameHomeDirWidget` and emits `path_changed`.

#### `_select_flame_setups_dir(self)`
- **Purpose**: Slot for the "Select Flame Setups Directory" button.
- **Behavior**: Opens a `QFileDialog` to allow the user to select a directory. If a directory is selected, it updates the `FlameSetupsDirWidget` and emits `path_changed`.

#### `_select_flame_media_dir(self)`
- **Purpose**: Slot for the "Select Flame Media Directory" button.
- **Behavior**: Opens a `QFileDialog` to allow the user to select a directory. If a directory is selected, it updates the `FlameMediaDirWidget` and emits `path_changed`.

#### `_select_flame_catalog_dir(self)`
- **Purpose**: Slot for the "Select Flame Catalog Directory" button.
- **Behavior**: Opens a `QFileDialog` to allow the user to select a directory. If a directory is selected, it updates the `FlameCatalogDirWidget` and emits `path_changed`.

#### `get_flame_options(self) -> dict`
- **Purpose**: Gathers all current Flame-related options from the panel's widgets.
- **Returns**: A dictionary containing the selected Flame software choice, and the paths for home, setups, media, catalog directories, and the selected LOGIK-PROJEKT configuration data.

#### `set_flame_options(self, options: dict)`
- **Purpose**: Sets the Flame-related options in the panel's widgets based on a provided dictionary.
- **Arguments**:
    - `options` (dict): A dictionary containing Flame option values.
- **Behavior**: Updates each widget with its corresponding value from the `options` dictionary. Includes a fallback for `logik_projekt_config` to handle old string-based configurations if necessary.

#### `set_project_name(self, project_name: str)`
- **Purpose**: Sets the project name in the `FlameHomeDirWidget`.
- **Arguments**:
    - `project_name` (str): The name of the project.

## Observations
- This panel effectively consolidates all Flame-related configuration inputs into a single, organized UI section.
- It leverages specialized custom widgets for each input type (comboboxes, directory selectors), promoting reusability and modularity.
- The use of `QFileDialog` for directory selection provides a standard and user-friendly way to browse the filesystem.
- The `path_changed` signal is a good example of how custom signals can be used to communicate changes from a child widget to its parent or other interested components.
- The `get_flame_options` and `set_flame_options` methods provide a convenient interface for external components to interact with the panel's data.
- The panel integrates with backend functions (`get_sysconfig_*`, `get_flame_software_versions`, `get_logik_projekt_config_values`) to populate its widgets with initial or default values.