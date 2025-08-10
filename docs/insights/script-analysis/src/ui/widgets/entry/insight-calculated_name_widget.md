# Insight: `calculated_name_widget.py`

## 1. Widget Type

`CalculatedNameWidget` is a composite `QWidget` containing a `QLabel` for the title ("Projekt Name:") and a `QLineEdit` to display the name. It serves as a read-only information field.

## 2. Purpose

The widget's sole purpose is to display the final, calculated project name. This name is automatically generated based on other user inputs from different widgets.

## 3. Behavior and Functionality

- **Read-Only Display:** The `QLineEdit` is not directly editable by the user. It displays placeholder text initially to inform the user that the value is automatically generated.
- **Dynamic Updates:** The displayed name is set programmatically by an external controller calling the public `set(value)` method.
- **Value Access:** The current value of the widget can be retrieved as a string using the `get()` method.

## 4. Key Attributes and Properties

- `self.layout`: A `QHBoxLayout` that arranges the label and the line edit horizontally.
- `self.label`: A `QLabel` with the static text "Projekt Name:".
- `self.entry`: A `QLineEdit` that shows the placeholder text and later the calculated project name.

## 5. Signals and Slots

- **Signals:** This widget does not emit any custom signals.
- **Slots (Public Methods):**
  - `set(self, value)`: A public method that functions as a slot to update the displayed project name.
  - `get(self)`: A public method to retrieve the currently displayed name.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: It imports the `ui_config` module to use the `ENTRY_HEIGHT` constant, ensuring its visual height is consistent with other entry widgets across the application.
- **External Controller/Logic**: This widget is a passive view component. It is controlled by a higher-level script (e.g., `app_logic.py` or a parent panel). This controller is responsible for:
  1. Gathering inputs from other widgets (like `ClientNameWidget`, `CampaignNameWidget`, `SerialNumberWidget`).
  2. Concatenating or processing these inputs to form the final project name.
  3. Calling the `set()` method of this widget to display the result.

## 7. UI/UX Notes

The use of placeholder text ("Projekt Name will be automatically calculated...") is a crucial UX feature. It clearly communicates to the user that this field is not for direct input and that its value is dependent on other fields. This prevents user confusion and ensures the naming convention is enforced.
