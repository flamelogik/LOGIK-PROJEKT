# Insight: `flame_home_dir_widget.py`

## 1. Widget Type

`FlameHomeDirWidget` is a composite `QWidget` that includes a `QLabel` and a `QPushButton`. It is a specialized button for selecting a base directory path, with dynamic path construction capabilities.

## 2. Purpose

This widget allows the user to define the base directory for the Autodesk Flame project's "home" directory. This is a crucial setting as it determines the root location where the new Flame project's files and subdirectories will reside. It also supports dynamic path generation based on the project name.

## 3. Behavior and Functionality

- **Directory Selection Trigger:** Clicking the button emits a `clicked` signal, intended to open a directory selection dialog.
- **Dynamic Path Display:** The button's text displays a dynamically constructed path. This path can include a placeholder `<project name>` which is replaced by the actual project name as it is entered by the user in another widget.
- **Path Management:** The widget internally stores a `_base_path` (the selected directory) and a `_project_name`. The `_update_displayed_path()` method combines these to show the user the final path.
- **Path Access:** The `get_path()` method returns the fully resolved path, including the project name if available. The `set_path(path)` and `set_project_name(name)` methods allow external components to update the base path and project name, respectively.

## 4. Key Attributes and Properties

- `self.layout`: A `QHBoxLayout` for horizontal arrangement.
- `self.label`: A `QLabel` with the static text "Flame Home Dir:".
- `self.button`: The `QPushButton` instance, which displays the dynamically constructed path.
- `self._base_path`: Stores the selected base directory (e.g., `/mnt/projects/`).
- `self._project_name`: Stores the project name (e.g., "MyNewProjekt").

## 5. Signals and Slots

- **Signals:** The `self.button` (a `QPushButton`) emits the standard `clicked()` signal when pressed.
- **Slots (Public Methods):**
  - The `__init__` method takes an optional `command` argument, which is connected to the button's `clicked` signal (typically for opening a `QFileDialog`).
  - `set_project_name(self, name)`: Updates the internal project name and refreshes the displayed path.
  - `set_path(self, path)`: Updates the internal base path and refreshes the displayed path.
  - `get_path(self)`: Returns the fully resolved project home directory path.

## 6. Dependencies and Relationships

- **`QFileDialog` (external to this widget)**: The `command` connected to this button will typically invoke a `QFileDialog` to allow the user to select the base directory.
- **`CalculatedNameWidget` (or similar project name input)**: This widget has a strong relationship with the project name input. A controller will connect the `textChanged` signal of the project name input widget to this widget's `set_project_name()` method, ensuring the displayed path updates in real-time.
- **Application Logic/Configuration**: The resolved path from `get_path()` is a critical input for the project creation process, defining the physical location of the new Flame project.

## 7. UI/UX Notes

This widget provides a sophisticated yet user-friendly way to define project locations. The dynamic path display, including the project name, gives the user immediate feedback on where their project will be created. This helps prevent errors and ensures that the project structure aligns with expectations. The use of a placeholder (`<project name>`) makes the path template clear and adaptable.