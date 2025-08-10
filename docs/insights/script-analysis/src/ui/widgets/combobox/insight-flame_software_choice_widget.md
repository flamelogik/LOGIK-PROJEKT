# Insight: `flame_software_choice_widget.py`

## 1. Widget Type

`FlameSoftwareChoiceWidget` is a composite `QWidget` that includes a `QLabel` and a `QComboBox`. It serves as a dropdown menu for selecting a version of Autodesk Flame.

## 2. Purpose

This widget's primary function is to allow the user to select which installed version of Autodesk Flame they want to use for the new project. This is a critical choice that dictates which set of command-line tools and paths the application will use.

## 3. Behavior and Functionality

- **Dynamic Population:** The list of software versions is not hardcoded. It is populated dynamically by an external process that scans the system for Flame installations. The `set_values(values)` method takes a list of version strings found by this scan.
- **Data Association:** The widget uses `self.combobox.addItem(value, value)`, storing the version string (e.g., "2025.1") as both the visible text and the associated item data. This provides a consistent way to retrieve the selection.
- **Value Access:** The `get()` method returns the `currentData()`, which is the full version string of the selected item. The `set(value)` method allows for programmatically selecting a version from the list.

## 4. Key Attributes and Properties

- `self.layout`: A `QHBoxLayout` for horizontal arrangement.
- `self.label`: A `QLabel` with the static text "Software Version:".
- `self.combobox`: The `QComboBox` that displays the list of detected Flame versions.

## 5. Signals and Slots

- **Signals:** The underlying `QComboBox` emits `currentTextChanged(const QString &)` when the user selects a new version. This signal is fundamental to the application's reactive nature.
- **Slots (Public Methods):**
  - `set_values(self, values)`: Populates the dropdown with a list of version strings.
  - `get(self)`: Retrieves the selected version string.
  - `set(self, value)`: Sets the current selection based on a version string.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: Imports `ui_config` for the `COMBOBOX_HEIGHT` constant.
- **`src.core.utils.flame_software_utils` (or similar)**: This widget is critically dependent on an external utility script that performs the system scan to find installed Flame versions. The main application logic (`app_logic.py`) would call this utility and then use the results to populate this widget.
- **Relationship to Project Creation Logic**: The value selected in this widget directly influences the entire project creation process. The application logic listens for changes to this widget and uses the selected version to determine:
  - The correct path to the `wiretap_create_project` executable.
  - The default paths for project metadata and media.
  - Any version-specific settings that need to be applied.

## 7. UI/UX Notes

By dynamically scanning the system and populating the dropdown, the widget ensures that the user can only select a valid, installed version of Flame. This is a robust design that prevents errors and makes the application automatically adapt to the user's specific environment without requiring manual configuration.