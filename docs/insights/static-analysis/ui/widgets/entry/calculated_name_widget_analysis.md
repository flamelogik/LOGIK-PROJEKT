# Static Analysis: `src/ui/widgets/entry/calculated_name_widget.py`

## Overview
The `CalculatedNameWidget` class is a custom `QWidget` (from PySide6) designed to display a calculated project name. It comprises a `QLabel` for the "Projekt Name:" text and a `QLineEdit` that is typically read-only, showing the automatically generated name. It provides methods to get and set the displayed name.

## Dependencies
- **PySide6.QtWidgets**: `QWidget`, `QLabel`, `QLineEdit`, `QHBoxLayout`
- **PySide6.QtCore**: `Qt` (for alignment flags)
- **Local Modules (src.ui)**:
    - `src.ui.ui_config`: Used for setting the fixed height of the entry field (`ENTRY_HEIGHT`).

## Class: `CalculatedNameWidget`

### Purpose
To provide a dedicated UI component for displaying a project name that is automatically generated based on other user inputs, ensuring consistency and preventing manual errors.

### Initialization (`__init__`)
- Inherits from `PySide6.QtWidgets.QWidget`.
- Takes `master` (parent widget) as an argument.
- Initializes an `QHBoxLayout` for the widget, setting its contents margins to zero.
- Creates a `QLabel` with the text "Projekt Name:".
    - Aligns the label text to the right and vertically center (`Qt.AlignRight | Qt.AlignVCenter`).
    - Adds the label to the layout.
- Creates a `QLineEdit` for displaying the calculated name.
    - Sets placeholder text: "Projekt Name will be automatically calculated...".
    - Sets a fixed height for the entry field using `ui_config.ENTRY_HEIGHT`.
    - Adds the entry field to the layout.

### Methods

#### `get()`
- **Purpose**: Retrieves the current text displayed in the `QLineEdit`.
- **Returns**: The string value of the calculated project name.

#### `set(value)`
- **Purpose**: Sets the text of the `QLineEdit` to the provided `value`.
- **Behavior**: Temporarily sets the `QLineEdit` to writable (`setReadOnly(False)`), sets the text, and then immediately sets it back to read-only (`setReadOnly(True)`). This allows programmatic updates while preventing direct user editing.

## Observations
- Similar to `AspectRatioWidget`, this is a simple, self-contained UI component for displaying a derived value.
- The use of placeholder text is a good UX practice, informing the user about the field's purpose.
- The `set()` method's handling of the `readOnly` property is consistent with other display-only entry widgets.
- This widget is crucial for showing the user the final, formatted project name before creation, which is often a critical piece of information in project management workflows.
