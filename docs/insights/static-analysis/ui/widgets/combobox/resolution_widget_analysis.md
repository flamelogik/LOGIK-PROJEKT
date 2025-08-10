# Static Analysis: `src/ui/widgets/combobox/resolution_widget.py`

## Overview
The `ResolutionWidget` class is a custom `QWidget` (from PySide6) designed for selecting a resolution from a dropdown list. It consists of a `QLabel` for the "Resolution:" text and a `QComboBox` for the selection. It provides methods to populate the combobox with resolution names, get the selected resolution name, get the full data for the selected resolution, and set the selection based on a resolution name.

## Dependencies
- **PySide6.QtWidgets**: `QWidget`, `QLabel`, `QComboBox`, `QHBoxLayout`
- **PySide6.QtCore**: `Qt` (for alignment flags)
- **Local Modules (src.ui)**:
    - `src.ui.ui_config`: Used for setting the fixed height of the combobox (`COMBOBOX_HEIGHT`).

## Class: `ResolutionWidget`

### Purpose
To provide a dedicated UI component for users to select a video resolution, which is a fundamental parameter in media projects.

### Initialization (`__init__`)
- Inherits from `PySide6.QtWidgets.QWidget`.
- Takes `master` (parent widget) as an argument.
- Initializes an empty list `self.resolutions` to store the full resolution data.
- Initializes an `QHBoxLayout` for the widget, setting its contents margins to zero.
- Creates a `QLabel` with the text "Resolution:".
    - Aligns the label text to the right and vertically center (`Qt.AlignRight | Qt.AlignVCenter`).
    - Adds the label to the layout.
- Creates a `QComboBox` for selecting the resolution.
    - Sets a fixed height for the combobox using `ui_config.COMBOBOX_HEIGHT`.
    - Adds the combobox to the layout.

### Methods

#### `set_values(values: list[dict])`
- **Purpose**: Populates the `QComboBox` with a list of resolution dictionaries.
- **Behavior**: Stores the full `values` list in `self.resolutions`. Clears any existing items in the combobox. If `self.resolutions` is not empty, it extracts `"resolution_name"` from each dictionary to populate the combobox display and sets the current selection to the first item.

#### `get()`
- **Purpose**: Retrieves the currently selected text (resolution name) from the `QComboBox`.
- **Returns**: The string value of the selected resolution name.

#### `get_selected_resolution_data() -> dict | None`
- **Purpose**: Retrieves the full dictionary data for the currently selected resolution.
- **Behavior**: Gets the `currentIndex` of the combobox. If the index is valid, it returns the corresponding dictionary from `self.resolutions`. Otherwise, it returns `None`.

#### `set(value)`
- **Purpose**: Sets the current selection of the `QComboBox` based on a provided resolution name `value`.
- **Behavior**: If `self.resolutions` is empty, it does nothing. Otherwise, it iterates through `self.resolutions` to find a dictionary whose `"resolution_name"` matches the `value`. If a match is found, it sets the combobox's current index to that position.

## Observations
- This widget is a specialized combobox that stores both the display name and the full data dictionary for each resolution, allowing for easy retrieval of detailed information.
- The `set_values` method expects a list of dictionaries with a `"resolution_name"` key, indicating a clear data contract.
- The `get_selected_resolution_data()` method is particularly useful for retrieving associated properties (like width, height, aspect ratio) when a resolution is selected.
- The `set()` method provides a way to programmatically set the selected resolution by its name.
- The use of `ui_config.COMBOBOX_HEIGHT` ensures consistent sizing across similar combobox widgets.
