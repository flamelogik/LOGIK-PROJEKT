# Static Analysis: `src/ui/widgets/entry/campaign_name_widget.py`

## Overview
The `CampaignNameWidget` class is a custom `QWidget` (from PySide6) designed for user input of a campaign name. It consists of a `QLabel` for the "Campaign Name:" text and a `QLineEdit` for text entry. It provides methods to get and set the displayed campaign name.

## Dependencies
- **PySide6.QtWidgets**: `QWidget`, `QLabel`, `QLineEdit`, `QHBoxLayout`
- **PySide6.QtCore**: `Qt` (for alignment flags)
- **Local Modules (src.ui)**:
    - `src.ui.ui_config`: Used for setting the fixed height of the entry field (`ENTRY_HEIGHT`).

## Class: `CampaignNameWidget`

### Purpose
To provide a dedicated UI component for users to input the campaign name, which is likely a key piece of information for organizing projects within the application.

### Initialization (`__init__`)
- Inherits from `PySide6.QtWidgets.QWidget`.
- Takes `master` (parent widget) as an argument.
- Initializes an `QHBoxLayout` for the widget, setting its contents margins to zero.
- Creates a `QLabel` with the text "Campaign Name:".
    - Aligns the label text to the right and vertically center (`Qt.AlignRight | Qt.AlignVCenter`).
    - Adds the label to the layout.
- Creates a `QLineEdit` for entering the campaign name.
    - Sets placeholder text: "Enter Campaign Name...".
    - Sets a fixed height for the entry field using `ui_config.ENTRY_HEIGHT`.
    - Adds the entry field to the layout.

### Methods

#### `get()`
- **Purpose**: Retrieves the current text entered in the `QLineEdit`.
- **Returns**: The string value of the campaign name.

#### `set(value)`
- **Purpose**: Sets the text of the `QLineEdit` to the provided `value`.
- **Behavior**: Directly sets the text of the `QLineEdit`. Unlike some other widgets, this one is intended for user input, so it does not toggle read-only status.

## Observations
- This widget is a straightforward input component, combining a label and a text entry field.
- The use of placeholder text guides the user on the expected input.
- The fixed height from `ui_config.ENTRY_HEIGHT` ensures visual consistency with other entry widgets.
- This widget is a fundamental building block for collecting project metadata.
