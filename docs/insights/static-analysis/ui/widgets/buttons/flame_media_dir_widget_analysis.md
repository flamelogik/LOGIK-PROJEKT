# Static Analysis: `src/ui/widgets/button/flame_media_dir_widget.py`

## Overview
The `FlameMediaDirWidget` class is a custom `QWidget` (from PySide6) designed for selecting an Autodesk Flame Media directory. It consists of a `QLabel` for the "Flame Media Dir:" text and a `QPushButton` that, when clicked, likely opens a directory selection dialog. It provides methods to set and get the displayed directory path.

## Dependencies
- **PySide6.QtWidgets**: `QWidget`, `QLabel`, `QPushButton`, `QHBoxLayout`
- **PySide6.QtCore**: `Qt` (for alignment flags)

## Class: `FlameMediaDirWidget`

### Purpose
To provide a dedicated UI component for users to specify the location of the Autodesk Flame Media directory, which is essential for managing media files within Flame projects.

### Initialization (`__init__`)
- Inherits from `PySide6.QtWidgets.QWidget`.
- Takes `master` (parent widget) and an optional `command` (a callable) as arguments.
- Initializes an `QHBoxLayout` for the widget, setting its contents margins to zero.
- Creates a `QLabel` with the text "Flame Media Dir:".
    - Aligns the label text to the right and vertically center (`Qt.AlignRight | Qt.AlignVCenter`).
    - Adds the label to the layout.
- Creates a `QPushButton` with the initial text "Select Directory".
    - Sets the object name to "flameMediaDirButton" for QSS (Qt Style Sheet) styling.
    - If a `command` is provided during initialization, it connects the button's `clicked` signal to this `command`.
    - Adds the button to the layout.

### Methods

#### `set_path(path)`
- **Purpose**: Sets the text displayed on the `QPushButton` to the provided `path`.
- **Behavior**: Updates the button's text to reflect the selected directory path.

#### `get_path()`
- **Purpose**: Retrieves the current text displayed on the `QPushButton`.
- **Returns**: The string value of the displayed directory path.

## Observations
- This widget is a reusable component for selecting a directory path, where the button itself displays the selected path.
- The `command` parameter allows for flexible integration with a directory selection dialog (e.g., `QFileDialog.getExistingDirectory`).
- The `setObjectName` is used for styling, allowing for custom visual appearance via QSS.
- This widget is a fundamental building block for configuring Flame environment settings.
