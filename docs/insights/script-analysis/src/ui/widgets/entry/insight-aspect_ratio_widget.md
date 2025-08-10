# Insight: `aspect_ratio_widget.py`

## 1. Widget Type

`AspectRatioWidget` is a composite `QWidget` that encapsulates a `QLabel` and a `QLineEdit`. It functions as a specialized, read-only display field.

## 2. Purpose

The primary purpose of this widget is to display the calculated pixel aspect ratio derived from the project's resolution settings (width and height).

## 3. Behavior and Functionality

- **Read-Only Display:** The widget is designed for display purposes only. The `QLineEdit` is not user-editable, preventing accidental changes to the calculated value.
- **Programmatic Updates:** The value is updated by calling the public `set(value)` method. This method temporarily removes the read-only flag, sets the new text, and immediately reapplies the read-only flag.
- **Value Retrieval:** The displayed aspect ratio can be retrieved as a string using the `get()` method.

## 4. Key Attributes and Properties

- `self.layout`: A `QHBoxLayout` that arranges the label and line edit horizontally.
- `self.label`: A `QLabel` displaying the static text "Aspect Ratio:".
- `self.entry`: A `QLineEdit` instance used to display the aspect ratio value.

## 5. Signals and Slots

- **Signals:** This widget does not define or emit any custom signals.
- **Slots (Public Methods):**
  - `set(self, value)`: Acts as a public slot to update the text of the `QLineEdit`.
  - `get(self)`: A public method to retrieve the current text from the `QLineEdit`.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: The widget imports `ui_config` to use the `ENTRY_HEIGHT` constant. This ensures its height is consistent with other input widgets in the application, demonstrating a dependency on the project's centralized UI styling.
- **Parent Panel/Controller**: `AspectRatioWidget` is designed to be a passive component. It relies on an external script (likely a parent panel or an application logic controller) to perform the aspect ratio calculation (e.g., by listening to changes in `ResolutionWidthWidget` and `ResolutionHeightWidget`) and then push the result to this widget via its `set()` method.

## 7. UI/UX Notes

From a user's perspective, this widget appears as a standard labeled data field. Its non-editable nature clearly communicates that the value is a calculated result, not a user input. The horizontal layout provides a clean and compact presentation.
