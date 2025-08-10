# Static Analysis: `src/ui/widgets/combobox/ocio_config_widget.py`

## Overview
The `OcioConfigWidget` class is a custom `QWidget` (from PySide6) designed for selecting an OpenColorIO (OCIO) configuration from a dropdown list. It consists of a `QLabel` for the "OCIO Config:" text and a `QComboBox` for the selection. It provides methods to populate the combobox with display names and associated relative directory paths, get the selected relative path, set the selection based on a relative path, and get the display name of the selected OCIO configuration.

## Dependencies
- **PySide6.QtWidgets**: `QWidget`, `QLabel`, `QComboBox`, `QHBoxLayout`
- **PySide6.QtCore**: `Qt` (for alignment flags)
- **Local Modules (src.ui)**:
    - `src.ui.ui_config`: Used for setting the fixed height of the combobox (`COMBOBOX_HEIGHT`).

## Class: `OcioConfigWidget`

### Purpose
To provide a dedicated UI component for users to select an OCIO configuration, which is essential for color management in visual effects and animation workflows.

### Initialization (`__init__`)
- Inherits from `PySide6.QtWidgets.QWidget`.
- Takes `master` (parent widget) as an argument.
- Initializes an `QHBoxLayout` for the widget, setting its contents margins to zero.
- Creates a `QLabel` with the text "OCIO Config:".
    - Aligns the label text to the right and vertically center (`Qt.AlignRight | Qt.AlignVCenter`).
    - Adds the label to the layout.
- Creates a `QComboBox` for selecting the OCIO configuration.
    - Sets a fixed height for the combobox using `ui_config.COMBOBOX_HEIGHT`.
    - Adds the combobox to the layout.

### Methods

#### `set_values(values: list[tuple[str, str]])`
- **Purpose**: Populates the `QComboBox` with a list of tuples, where each tuple contains a `(relative_dir, ocio_name)`.
- **Behavior**: Clears any existing items in the combobox. Iterates through the `values` list, adding the `relative_dir` as both the display text and the associated user data. If the `values` list is not empty, it sets the current selection to the first item.

#### `get() -> str`
- **Purpose**: Retrieves the data associated with the currently selected item in the `QComboBox`.
- **Returns**: The string value of the relative directory path of the selected OCIO configuration.

#### `set(value: str)`
- **Purpose**: Sets the current selection of the `QComboBox` based on a provided data `value`.
- **Behavior**: Uses `self.combobox.findData(value)` to find the index of the item associated with the given `value`. If found, it sets the combobox's current index to that position.

#### `get_ocio_name() -> str`
- **Purpose**: Retrieves the display text of the currently selected item in the `QComboBox`.
- **Returns**: The string value of the OCIO configuration's display name.

## Observations
- This widget is a specialized combobox that uses the `relative_dir` as both the display text and the internal data, which is a common pattern for path-based selections.
- The `set_values` method expects a specific tuple structure for its input, indicating a clear data contract.
- The `get()` method returns the `currentData()`, which is the `relative_dir` associated with the selected item.
- The `set()` method uses `findData()` for robust selection based on the internal data, rather than relying on the display text.
- The `get_ocio_name()` method provides access to the user-facing display text, which might be different from the internal data.
- The use of `ui_config.COMBOBOX_HEIGHT` ensures consistent sizing across similar combobox widgets.
