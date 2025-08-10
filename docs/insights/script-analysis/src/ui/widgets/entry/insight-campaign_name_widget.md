# Insight: `campaign_name_widget.py`

## 1. Widget Type

`CampaignNameWidget` is a composite `QWidget` that combines a `QLabel` and a `QLineEdit`. It functions as a standard, user-editable text input field.

## 2. Purpose

This widget's primary purpose is to capture the user's input for the "Campaign Name," which is a key component of the overall project identifier.

## 3. Behavior and Functionality

- **User Input:** Unlike read-only widgets, this one is fully editable by the user.
- **Data Access:** The entered text can be retrieved via the `get()` method and programmatically set using the `set(value)` method.
- **Placeholder Text:** It displays "Enter Campaign Name..." to guide the user on what information to provide.

## 4. Key Attributes and Properties

- `self.layout`: A `QHBoxLayout` that arranges the label and entry field horizontally.
- `self.label`: A `QLabel` with the static text "Campaign Name:".
- `self.entry`: The `QLineEdit` instance where the user types the campaign name.

## 5. Signals and Slots

- **Signals:** While the `CampaignNameWidget` class itself does not define custom signals, its `self.entry` (`QLineEdit`) child emits standard Qt signals, most importantly `textChanged(const QString &)`. This signal is crucial for enabling real-time updates in other parts of the application.
- **Slots (Public Methods):**
  - `get(self)`: A public method to retrieve the current text.
  - `set(self, value)`: A public method to populate the entry field.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: Imports `ui_config` to set a fixed `ENTRY_HEIGHT`, ensuring visual consistency with other widgets.
- **Relationship to `CalculatedNameWidget`**: This is a critical relationship. A controller or parent panel will connect the `textChanged` signal of this widget's `QLineEdit` to a slot that updates the `CalculatedNameWidget`. This creates a reactive UI where the final project name changes dynamically as the user types the campaign name.
- **Parent Controller/Panel**: The widget relies on a higher-level component to read its value (using `get()`) when constructing the final project name or saving the project data.

## 7. UI/UX Notes

This is a straightforward and conventional UI input element. The placeholder text provides a clear affordance for user interaction. Its direct and immediate impact on the `CalculatedNameWidget` provides excellent feedback to the user, showing them how their input contributes to the final output.
