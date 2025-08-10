# Insight: `resolution_width_widget.py`

## 1. Widget Type

`ResolutionWidthWidget` is a composite `QWidget` that bundles a `QLabel` and a read-only `QLineEdit`.

## 2. Purpose

This widget is designed to display the horizontal resolution (width) of the project. Like the height widget, this value is derived from a selection made elsewhere in the UI, not direct user input.

## 3. Behavior and Functionality

- **Read-Only Display:** The `QLineEdit` is not editable by the user, ensuring that the displayed width corresponds to a standard, selected resolution.
- **Programmatic Updates:** The value is updated by an external controller via the public `set(value)` method.
- **Value Retrieval:** The displayed width can be accessed as a string using the `get()` method.

## 4. Key Attributes and Properties

- `self.layout`: A `QHBoxLayout` for arranging the label and line edit side-by-side.
- `self.label`: A `QLabel` with the static text "Width:".
- `self.entry`: A `QLineEdit` that displays the resolution width value.

## 5. Signals and Slots

- **Signals:** The widget itself does not define custom signals.
- **Slots (Public Methods):**
  - `set(self, value)`: A public method to update the displayed text.
  - `get(self)`: A public method to retrieve the current value.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: Imports `ui_config` to use the `ENTRY_HEIGHT` constant, maintaining visual consistency.
- **Relationship to `AspectRatioWidget`**: This widget is a critical input for the aspect ratio calculation. An external controller monitors this widget and `ResolutionHeightWidget`. When the value in either changes, the controller recalculates the aspect ratio and updates the `AspectRatioWidget`.
- **Relationship to Resolution Preset Selector**: The value displayed here is set in response to a user's selection in another widget, typically a `QComboBox` containing resolution presets. The controller extracts the width from the selected preset and uses the `set()` method to display it in this widget.

## 7. UI/UX Notes

Similar to the height widget, making this field read-only is a deliberate design choice to enforce standard resolutions and prevent user error. It provides clear, passive feedback of a choice made in another part of the UI.