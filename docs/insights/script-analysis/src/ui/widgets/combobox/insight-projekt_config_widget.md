# Insight: `projekt_config_widget.py`

## 1. Widget Type

`ProjektConfigWidget` is a composite `QWidget` that combines a `QLabel` and a `QComboBox`. It is designed for selecting a project configuration from a predefined list.

## 2. Purpose

This widget allows the user to select a comprehensive "Projekt Configuration." Each configuration represents a set of predefined settings and values that will be used to initialize a new project. This centralizes project setup and ensures consistency.

## 3. Behavior and Functionality

This widget is more sophisticated than simple comboboxes, as it manages both the display name and the underlying data for each configuration:

- **Data-Driven Population:** The `set_values(configs)` method populates the `QComboBox` from a list of dictionaries. It extracts the `"PROJEKT Configuration Name"` from each dictionary for display in the combobox, while internally storing the *entire* configuration dictionary in `self.all_configs`.
- **Retrieval of Full Data:** The `get_selected_config_data()` method is crucial. It retrieves the *full dictionary* of the currently selected configuration, not just its display name. This allows other parts of the application to access all the detailed settings associated with the chosen configuration.
- **Value Access (Name):** The `get()` method returns only the display name of the currently selected configuration.
- **Value Setting (Name):** The `set(value)` method allows for programmatic selection of a configuration by its display name.

## 4. Key Attributes and Properties

- `self.all_configs`: A list of dictionaries, storing the complete data for all available project configurations.
- `self.layout`: A `QHBoxLayout` for horizontal arrangement.
- `self.label`: A `QLabel` with the static text "Projekt Config:".
- `self.combobox`: The `QComboBox` that displays the names of the project configurations.

## 5. Signals and Slots

- **Signals:** The underlying `QComboBox` emits `currentTextChanged(const QString &)` when the user selects a new configuration. This signal is vital for triggering updates in other UI elements that depend on the selected configuration.
- **Slots (Public Methods):**
  - `set_values(self, configs)`: Populates the combobox and stores the full configuration data.
  - `get(self)`: Returns the display name of the selected configuration.
  - `get_selected_config_data(self)`: Returns the complete dictionary of the selected configuration.
  - `set(self, value)`: Sets the selection based on the display name.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: Imports `ui_config` for the `COMBOBOX_HEIGHT` constant.
- **External Data Source (e.g., `cfg/site-cfg/logik-projekt-cfg/logik-projekt-templates/`)**: This widget is heavily dependent on an external source (likely JSON files) that defines the various project configurations. A data loading utility (e.g., in `src/core/functions/io/`) would read these configurations and pass them to `set_values()`.
- **Relationship to `AppLogic` and other Panels**: This widget is a central control point. When a user selects a configuration, the `currentTextChanged` signal will be connected to a slot in `AppLogic` or a parent panel. This slot will then call `get_selected_config_data()` to retrieve the full configuration, which will then be used to:
  - Populate other widgets (e.g., `ResolutionWidget`, `FrameRateWidget`, `BitDepthWidget`) with default values from the selected configuration.
  - Update summary panels.
  - Drive the project creation process.

## 7. UI/UX Notes

This widget provides a powerful way to manage complex project settings through simple selection. By separating the display name from the underlying data, it offers a user-friendly interface while allowing the application to work with rich, structured configuration data. The ability to load predefined configurations significantly streamlines the project setup workflow and reduces the chance of errors.