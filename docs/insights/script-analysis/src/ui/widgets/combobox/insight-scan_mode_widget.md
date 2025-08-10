# Insight: `scan_mode_widget.py`

## 1. Widget Type

`ScanModeWidget` is a composite `QWidget` that combines a `QLabel` and a `QComboBox`. It functions as a dropdown selection for video scan modes.

## 2. Purpose

This widget allows the user to select the scan mode for the project (e.g., "Progressive", "Interlaced"). This setting is crucial for how video frames are displayed and processed, especially in broadcast and film workflows.

## 3. Behavior and Functionality

- **Dynamic Population:** The list of available scan modes is populated dynamically by an external controller calling the `set_values(values)` method. This allows for flexibility in defining supported scan modes.
- **Default Selection:** The first item in the populated list is selected by default.
- **Simple Value Access:** The `get()` method returns the currently selected scan mode as a string. The `set(value)` method allows for programmatically selecting a scan mode.

## 4. Key Attributes and Properties

- `self.layout`: A `QHBoxLayout` for horizontal arrangement.
- `self.label`: A `QLabel` with the static text "Scan Mode:".
- `self.combobox`: The `QComboBox` that displays the list of scan mode options.

## 5. Signals and Slots

- **Signals:** The underlying `QComboBox` emits the `currentTextChanged(const QString &)` signal when the user selects a new scan mode. This signal is important for updating other parts of the application that might depend on this setting.
- **Slots (Public Methods):**
  - `set_values(self, values)`: Populates the dropdown with a list of strings.
  - `get(self)`: Retrieves the selected scan mode string.
  - `set(self, value)`: Sets the current selection.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: Imports `ui_config` for the `COMBOBOX_HEIGHT` constant.
- **External Controller/Data Source**: The widget depends on a higher-level controller or configuration to provide the list of valid scan modes. This ensures that only appropriate options are presented to the user.
- **Relationship to Project Configuration**: The selected scan mode is a core piece of project metadata that will be used by the project creation logic to correctly configure the Flame project.

## 7. UI/UX Notes

Using a `QComboBox` for scan mode selection ensures that users choose from a predefined set of valid options, preventing errors related to incorrect video formats. It simplifies a technical choice into a clear, user-friendly selection.