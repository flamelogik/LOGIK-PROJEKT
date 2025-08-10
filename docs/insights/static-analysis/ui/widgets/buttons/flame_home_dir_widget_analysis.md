# Static Analysis: `src/ui/widgets/button/flame_home_dir_widget.py`

## Overview
The `FlameHomeDirWidget` class is a custom `QWidget` (from PySide6) designed for selecting an Autodesk Flame Home directory. It consists of a `QLabel` for the "Flame Home Dir:" text and a `QPushButton` that, when clicked, likely opens a directory selection dialog. This widget has a unique feature: it can dynamically incorporate a project name into the displayed and returned path, supporting placeholders like `<project name>`.

## Dependencies
- **PySide6.QtWidgets**: `QWidget`, `QLabel`, `QPushButton`, `QHBoxLayout`
- **PySide6.QtCore**: `Qt` (for alignment flags)

## Class: `FlameHomeDirWidget`

### Purpose
To provide a dedicated UI component for users to specify the base location for Autodesk Flame projects, with the added capability to dynamically construct the full project path by integrating a project name.

### Initialization (`__init__`)
- Inherits from `PySide6.QtWidgets.QWidget`.
- Takes `master` (parent widget) and an optional `command` (a callable) as arguments.
- Initializes an `QHBoxLayout` for the widget, setting its contents margins to zero.
- Creates a `QLabel` with the text "Flame Home Dir:".
    - Aligns the label text to the right and vertically center (`Qt.AlignRight | Qt.AlignVCenter`).
    - Adds the label to the layout.
- Creates a `QPushButton` with the initial text "Select Directory".
    - Sets the object name to "flameHomeDirButton" for QSS (Qt Style Sheet) styling.
    - If a `command` is provided during initialization, it connects the button's `clicked` signal to this `command`.
    - Adds the button to the layout.
- Initializes `_base_path` and `_project_name` as empty strings. These internal variables store the selected base directory and the project name, respectively.

### Methods

#### `set_project_name(name: str)`
- **Purpose**: Sets the project name that will be used to construct the full path.
- **Behavior**: Updates `self._project_name` and then calls `_update_displayed_path()` to refresh the button's text.

#### `set_path(path: str)`
- **Purpose**: Sets the base directory path.
- **Behavior**: Updates `self._base_path` and then calls `_update_displayed_path()` to refresh the button's text.

#### `get_path() -> str`
- **Purpose**: Returns the fully constructed Flame home directory path, incorporating the project name if applicable.
- **Behavior**:
    - If `self._base_path` contains the placeholder "<project name>" and `self._project_name` is not empty, it replaces the placeholder with the actual project name.
    - If the placeholder is present but `_project_name` is empty, it returns the `_base_path` with the placeholder still in place.
    - If the placeholder is not present and `_project_name` is not empty, it appends the `_project_name` to the `_base_path` (e.g., "/path/to/base/project_name").
    - Otherwise, it returns just the `_base_path`.

#### `_update_displayed_path()`
- **Purpose**: Internal method to update the text displayed on the `QPushButton` based on `_base_path` and `_project_name`.
- **Behavior**: Similar logic to `get_path()`, but specifically updates the `button.setText()` to reflect the dynamically constructed path.

## Observations
- This widget is a sophisticated directory selector that supports dynamic path construction, which is highly useful for applications that generate project-specific directory structures.
- The separation of `_base_path` and `_project_name` allows for flexible configuration and updates.
- The `get_path()` method provides the actual path to be used by the application logic, while `_update_displayed_path()` ensures the UI reflects the current state.
- The `command` parameter allows for flexible integration with a directory selection dialog (e.g., `QFileDialog.getExistingDirectory`).
- The `setObjectName` is used for styling, allowing for custom visual appearance via QSS.
