# Insight: `resolution_height_widget.py`

## 1. Widget Type

`ResolutionHeightWidget` is a composite `QWidget` that contains a `QLabel` and a read-only `QLineEdit`.

## 2. Purpose

This widget's specific purpose is to display the vertical resolution (height) of the project. This value is typically derived from a selection made elsewhere, such as a dropdown menu of resolution presets.

## 3. Behavior and Functionality

- **Read-Only Display:** The `QLineEdit` is not user-editable. This prevents the user from entering a custom height that might not be a standard or supported resolution.
- **Programmatic Updates:** The value is set by an external controller calling the public `set(value)` method.
- **Value Retrieval:** The displayed height can be retrieved as a string using the `get()` method.

## 4. Key Attributes and Properties

- `self.layout`: A `QHBoxLayout` for horizontal alignment of the label and line edit.
- `self.label`: A `QLabel` with the static text "Height:".
- `self.entry`: A `QLineEdit` used to display the resolution height.

## 5. Signals and Slots

- **Signals:** This widget does not define or emit any custom signals. However, a change to its value (via the `set` method) is a trigger for external logic.
- **Slots (Public Methods):**
  - `set(self, value)`: A public method that acts as a slot to update the displayed text.
  - `get(self)`: A public method to retrieve the current value.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: It imports `ui_config` to use the `ENTRY_HEIGHT` constant, ensuring a consistent UI appearance.
- **Relationship to `AspectRatioWidget`**: This is a critical relationship. An external controller monitors changes to this widget and the `ResolutionWidthWidget`. When either value changes, the controller recalculates the aspect ratio and updates the `AspectRatioWidget` accordingly.
- **Relationship to Resolution Preset Selector**: The value displayed in this widget is almost certainly set in response to a user's selection in a different widget (e.g., a `QComboBox` of presets like "1920x1080", "3840x2160"). The controller extracts the height from the selected preset and uses the `set()` method to display it here.

## 7. UI/UX Notes

By making this field read-only, the UI enforces the use of standardized resolutions, preventing user error. It acts as a clear, passive display of a choice made elsewhere, reinforcing the user's selection without allowing for invalid modifications.