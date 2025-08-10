# Static Analysis: `src/ui/widgets/entry/resolution_height_widget.py`

## Overview
The `ResolutionHeightWidget` class is a custom `QWidget` (from PySide6) designed to display the height component of a resolution. It consists of a `QLabel` for the "Height:" text and a read-only `QLineEdit` to show the value. It provides methods to get and set the displayed height.

## Dependencies
- **PySide6.QtWidgets**: `QWidget`, `QLabel`, `QLineEdit`, `QHBoxLayout`
- **PySide6.QtCore**: `Qt` (for alignment flags)
- **Local Modules (src.ui)**:
    - `src.ui.ui_config`: Used for setting the fixed height of the entry field (`ENTRY_HEIGHT`).

## Class: `ResolutionHeightWidget`

### Purpose
To provide a dedicated, read-only UI component for displaying the height, typically as part of a resolution (e.g., 1920x1080), which is often calculated or derived from other inputs within the application.

### Initialization (`__init__`)
- Inherits from `PySide6.QtWidgets.QWidget`.
- Takes `master` (parent widget) as an argument.
- Initializes an `QHBoxLayout` for the widget, setting its contents margins to zero.
- Creates a `QLabel` with the text "Height:".
    - Aligns the label text to the right and vertically center (`Qt.AlignRight | Qt.AlignVCenter`).
    - Adds the label to the layout.
- Creates a `QLineEdit` for displaying the height.
    - Sets a fixed height for the entry field using `ui_config.ENTRY_HEIGHT`.
    - Sets the entry field to read-only by default.
    - Adds the entry field to the layout.

### Methods

#### `get()`
- **Purpose**: Retrieves the current text displayed in the `QLineEdit`.
- **Returns**: The string value of the height.

#### `set(value)`
- **Purpose**: Sets the text of the `QLineEdit` to the provided `value`.
- **Behavior**: Temporarily sets the `QLineEdit` to writable (`setReadOnly(False)`), sets the text, and then immediately sets it back to read-only (`setReadOnly(True)`). This allows programmatic updates while preventing direct user editing.

## Observations
- This widget is a simple, self-contained UI component, encapsulating a label and a read-only text input.
- The use of `ui_config.ENTRY_HEIGHT` ensures consistent sizing across similar entry widgets in the application.
- The `set()` method's temporary change to `readOnly` status is a common pattern for updating read-only fields programmatically.
- This widget is likely used in panels where the resolution height is a derived value rather than a direct user input.
