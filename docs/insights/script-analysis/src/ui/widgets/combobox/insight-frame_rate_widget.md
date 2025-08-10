# Insight: `frame_rate_widget.py`

## 1. Widget Type

`FrameRateWidget` is a composite `QWidget` that consists of a `QLabel` and a `QComboBox`. It serves as a standard dropdown selection menu.

## 2. Purpose

This widget allows the user to select the frame rate for the project (e.g., "23.976", "24", "25", "29.97"). This is a fundamental setting that defines the project's timebase.

## 3. Behavior and Functionality

- **Dynamic Population:** The list of available frame rates is not hardcoded within the widget. It is populated by an external controller calling the `set_values(values)` method, which takes a list of strings.
- **Default Selection:** Upon population, the widget automatically selects the first item in the list as the default.
- **Simple Value Access:** The `get()` method returns the currently selected frame rate as a string. The `set(value)` method allows for programmatically selecting a frame rate from the list.

## 4. Key Attributes and Properties

- `self.layout`: A `QHBoxLayout` for horizontal arrangement.
- `self.label`: A `QLabel` with the static text "Framerate:".
- `self.combobox`: The `QComboBox` that displays the list of frame rate options.

## 5. Signals and Slots

- **Signals:** The underlying `QComboBox` emits the `currentTextChanged(const QString &)` signal when the user selects a new frame rate.
- **Slots (Public Methods):**
  - `set_values(self, values)`: Populates the dropdown with a list of strings.
  - `get(self)`: Retrieves the selected frame rate string.
  - `set(self, value)`: Sets the current selection.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: Imports `ui_config` for the `COMBOBOX_HEIGHT` constant to ensure visual consistency.
- **External Controller/Data Source**: The widget depends on a higher-level controller (e.g., `app_logic.py`) or a configuration file to provide the list of valid frame rates. This makes the application adaptable to different production standards.
- **Relationship to Project Configuration**: The selected frame rate is a core piece of project metadata. The application logic listens for changes to this widget to update the main project data model and summary panels.

## 7. UI/UX Notes

Using a `QComboBox` for frame rate selection is an excellent design choice as it prevents users from entering invalid or non-standard frame rates. It ensures data integrity for a critical project setting. The dynamic population allows the list of available rates to be tailored to specific studio or project requirements without modifying the widget's code.