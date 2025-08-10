# Insight: `resolution_widget.py`

## 1. Widget Type

`ResolutionWidget` is a composite `QWidget` that encapsulates a `QLabel` and a `QComboBox`. It is designed for selecting a project resolution from a predefined list of options.

## 2. Purpose

This widget allows the user to select a standard resolution (e.g., "1920x1080", "3840x2160") for the new project. This selection is crucial as it determines the pixel dimensions and often the aspect ratio of the project.

## 3. Behavior and Functionality

This widget is designed to manage complex resolution data while presenting a simple choice to the user:

- **Data-Driven Population:** The `set_values(values)` method populates the `QComboBox` from a list of dictionaries. Each dictionary represents a resolution and is expected to contain a `"resolution_name"` key (for display) and likely `"width"`, `"height"`, and `"aspect_ratio"` keys (for internal data).
- **Internal Data Storage:** The widget stores the full list of resolution dictionaries in `self.resolutions`.
- **Retrieval of Full Data:** The `get_selected_resolution_data()` method is a key feature. It returns the *entire dictionary* of the currently selected resolution, allowing other parts of the application to easily access its width, height, and aspect ratio.
- **Value Access (Name):** The `get()` method returns only the display name of the currently selected resolution.
- **Value Setting (Name):** The `set(value)` method allows for programmatic selection of a resolution by its display name.

## 4. Key Attributes and Properties

- `self.resolutions`: A list of dictionaries, where each dictionary contains the full data for a resolution preset.
- `self.layout`: A `QHBoxLayout` for horizontal arrangement.
- `self.label`: A `QLabel` with the static text "Resolution:".
- `self.combobox`: The `QComboBox` that displays the names of the resolution presets.

## 5. Signals and Slots

- **Signals:** The underlying `QComboBox` emits `currentTextChanged(const QString &)` when the user selects a new resolution. This signal is critical for triggering updates in related widgets.
- **Slots (Public Methods):**
  - `set_values(self, values)`: Populates the combobox and stores the full resolution data.
  - `get(self)`: Returns the display name of the selected resolution.
  - `get_selected_resolution_data(self)`: Returns the complete dictionary of the selected resolution.
  - `set(self, value)`: Sets the selection based on the display name.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: Imports `ui_config` for the `COMBOBOX_HEIGHT` constant.
- **External Data Source**: This widget relies on an external source (e.g., a configuration file or a data model) to provide the list of valid resolution presets. A data loading utility would read these presets and pass them to `set_values()`.
- **Relationship to `ResolutionWidthWidget`, `ResolutionHeightWidget`, and `AspectRatioWidget`**: This widget is the primary driver for these three display-only widgets. When a user selects a resolution, the `currentTextChanged` signal will be connected to a slot in a parent panel or `AppLogic`. This slot will then call `get_selected_resolution_data()` and use the returned width, height, and aspect ratio to update the respective display widgets.

## 7. UI/UX Notes

Using a `QComboBox` for resolution selection simplifies a potentially complex choice for the user. By providing predefined options, it prevents invalid inputs and ensures consistency. The ability to retrieve the full resolution data (width, height, aspect ratio) from a single selection streamlines the data flow to other parts of the UI and the project creation logic.