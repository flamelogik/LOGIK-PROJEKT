# Insight: `start_frame_widget.py`

## 1. Widget Type

`StartFrameWidget` is a composite `QWidget` that combines a `QLabel` and a `QComboBox`. It functions as a dropdown menu for selecting the project's starting frame number.

## 2. Purpose

This widget allows the user to define the initial frame number for the project's timeline. Common choices include "1" (for film/VFX conventions) or "1001" (for broadcast/editorial conventions).

## 3. Behavior and Functionality

- **Dynamic Population:** The list of available start frame options is populated dynamically by an external controller calling the `set_values(values)` method. This allows for flexibility in defining common starting points.
- **Default Selection:** The first item in the populated list is selected by default.
- **Simple Value Access:** The `get()` method returns the currently selected start frame as a string. The `set(value)` method allows for programmatically selecting a start frame.

## 4. Key Attributes and Properties

- `self.layout`: A `QHBoxLayout` for horizontal arrangement.
- `self.label`: A `QLabel` with the static text "Start Frame:".
- `self.combobox`: The `QComboBox` that displays the list of start frame options.

## 5. Signals and Slots

- **Signals:** The underlying `QComboBox` emits the `currentTextChanged(const QString &)` signal when the user selects a new start frame. This signal is important for updating other parts of the application that might depend on this setting.
- **Slots (Public Methods):**
  - `set_values(self, values)`: Populates the dropdown with a list of strings.
  - `get(self)`: Retrieves the selected start frame string.
  - `set(self, value)`: Sets the current selection.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: Imports `ui_config` for the `COMBOBOX_HEIGHT` constant.
- **External Controller/Data Source**: The widget depends on a higher-level controller or configuration to provide the list of valid start frame options. This ensures that only appropriate options are presented to the user.
- **Relationship to Project Configuration**: The selected start frame is a core piece of project metadata that will be used by the project creation logic to correctly configure the Flame project's timeline.

## 7. UI/UX Notes

Using a `QComboBox` for start frame selection ensures that users choose from a predefined set of valid options, preventing errors related to incorrect timeline offsets. It simplifies a technical choice into a clear, user-friendly selection.