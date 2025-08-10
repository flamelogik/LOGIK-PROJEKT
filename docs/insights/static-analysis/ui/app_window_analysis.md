# Static Analysis: `src/ui/app_window.py`

## Overview
The `AppWindow` class is the main GUI window for the LOGIK-PROJEKT application. It orchestrates the layout of various UI panels, manages user interactions, and handles the communication between the UI and the core application logic. It also implements a multi-threading pattern to keep the UI responsive during long-running operations.

## Dependencies
- **PySide6.QtCore**: `QThread`, `QObject`, `Signal`, `Slot`
- **PySide6.QtWidgets**: `QWidget`, `QVBoxLayout`, `QHBoxLayout`, `QFileDialog`, `QMessageBox`
- **Python Standard Library**: `logging`
- **Local Modules (src.ui)**:
    - `src.ui.ui_config`
    - `src.ui.panels.template_info_panel.TemplateInfoPanel`
    - `src.ui.panels.template_parameters_panel.TemplateParametersPanel`
    - `src.ui.panels.template_summary_panel.TemplateSummaryPanel`
    - `src.ui.panels.projekt_template_panel.ProjektTemplatePanel`
    - `src.ui.panels.flame_options_panel.FlameOptionsPanel`
    - `src.ui.panels.projekt_summary_panel.ProjektSummaryPanel`
- **Local Modules (src.core)**:
    - `src.core.app_logic.AppLogic`
    - `src.core.projekt_manager.projekt_creator.create_projekt`
    - `src.core.template_manager.template_models.TemplateInfo`
    - `src.core.template_manager.template_models.TemplateParameters`
    - `src.core.utils.ocio_utils`
    - `src.core.utils.threaded_logging_utils.SignalHandler`
    - `src.core.utils.validation_utils`

## Class: `Worker` (Nested within `AppWindow` context)

### Overview
`Worker` is a `QObject` designed to run long-duration tasks in a separate thread, preventing the main GUI from freezing. It communicates with `AppWindow` via signals.

### Signals
- `finished`: Emitted when a task is completed.
- `error(str)`: Emitted if an error occurs during a task, carrying an error message.
- `template_imported(dict, dict)`: Emitted after a template is successfully imported, carrying `template_info` and `template_parameters`.
- `template_exported(str)`: Emitted after a template is successfully exported, carrying a success message.

### Methods

#### `create_projekt(self, projekt_summary_data)` (Slot)
- **Purpose**: Executes the project creation logic in a separate thread.
- **Arguments**: `projekt_summary_data` (dict) - data required for project creation.
- **Behavior**: Calls `create_projekt` function. Emits `finished` on completion or `error` if an exception occurs.

#### `export_template_json(self, template_info_data, template_params_data)` (Slot)
- **Purpose**: Exports template data to a JSON file in a separate thread.
- **Arguments**: `template_info_data` (dict), `template_params_data` (dict).
- **Behavior**: Calls `self.app_logic.export_logik_projekt_template`. Emits `template_exported` on success or `error` on failure.

#### `import_template_json(self, file_path)` (Slot)
- **Purpose**: Imports template data from a JSON file in a separate thread.
- **Arguments**: `file_path` (str) - path to the JSON file.
- **Behavior**: Calls `self.app_logic.import_logik_projekt_template`. Emits `template_imported` on success or `error` on failure.

## Class: `AppWindow`

### Overview
`AppWindow` is the central widget of the application, responsible for its overall layout, panel management, and coordinating interactions between UI elements and backend logic. It sets up the `QThread` and `Worker` for asynchronous operations.

### Signals
- `create_projekt_requested(dict)`: Emitted when the user requests project creation.
- `export_template_requested(dict, dict)`: Emitted when the user requests template export.
- `import_template_requested(str)`: Emitted when the user requests template import.

### Initialization (`__init__`)
- Inherits from `PySide6.QtWidgets.QWidget`.
- Takes `master` (parent widget) as an argument.
- Initializes `AppLogic` instance (`self.app_logic`).
- Sets up the main `QHBoxLayout` with left and right `QVBoxLayout` containers.
- Instantiates all UI panels (`TemplateInfoPanel`, `TemplateParametersPanel`, `TemplateSummaryPanel`, `ProjektTemplatePanel`, `FlameOptionsPanel`, `ProjektSummaryPanel`), sets their properties and fixed heights, and adds them to the appropriate layouts.
- Sets up thread-safe logging by connecting `LogEmitter` to `projekt_summary_panel.shell_output_text`.
- Calls `_update_all_summaries()` to initialize summary displays.
- Connects UI button clicks to internal methods (`_export_template_json`, `_import_template_json`, `_create_projekt`).
- Connects panel signals (`path_changed`, `calculated_name_updated`, `parameters_updated`) to `_update_all_summaries`.
- Initializes `QThread` and `Worker` instances, moves the worker to the new thread, and connects worker signals (`finished`, `error`, `template_imported`, `template_exported`) to `AppWindow` slots.
- Connects `AppWindow`'s request signals to `Worker`'s slots.
- Starts the `QThread`.

### Methods

#### `on_worker_finished(self)` (Slot)
- **Purpose**: Handles the completion of a worker thread task.
- **Behavior**: Logs a message indicating the worker thread has finished.

#### `on_worker_error(self, error_message)` (Slot)
- **Purpose**: Handles errors reported by the worker thread.
- **Arguments**: `error_message` (str) - the error description.
- **Behavior**: Logs the error and displays a critical `QMessageBox` to the user.

#### `on_template_exported(self, export_message)` (Slot)
- **Purpose**: Handles the successful completion of a template export.
- **Arguments**: `export_message` (str) - success message from the export operation.
- **Behavior**: Displays an information `QMessageBox` to the user.

#### `on_template_imported(self, template_info, template_parameters)` (Slot)
- **Purpose**: Handles the successful completion of a template import.
- **Arguments**: `template_info` (dict), `template_parameters` (dict) - imported template data.
- **Behavior**: Updates `template_info_panel` and `template_parameters_panel` with the imported data, then calls `_update_all_summaries()`.

#### `_update_all_summaries(self)`
- **Purpose**: Gathers data from input panels, updates summary panels, and sets the project name in `flame_options_panel`.
- **Behavior**: 
    - Retrieves data from `template_info_panel` and `template_parameters_panel`.
    - Combines and sets this data in `template_summary_panel`.
    - Retrieves `flame_options` from `flame_options_panel`.
    - Calls `self.app_logic.get_projekt_summary_data` to get comprehensive project summary.
    - Sets the full Flame project name in `flame_options_panel`.
    - Sets the project summary data in `projekt_summary_panel`.
    - Updates `projekt_template_panel` with relevant template info.

#### `_export_template_json(self)`
- **Purpose**: Initiates the template export process.
- **Behavior**: 
    - Gathers data from `template_info_panel` and `template_parameters_panel`.
    - Performs validation checks using `validation_utils.validate_client_campaign_names` and `validation_utils.validate_init_config`.
    - Displays warning/critical `QMessageBox` based on validation results.
    - If validation passes, emits `export_template_requested` signal to the worker thread.

#### `_import_template_json(self)`
- **Purpose**: Initiates the template import process.
- **Behavior**: Opens a `QFileDialog` to let the user select a JSON template file. If a file is selected, emits `import_template_requested` signal to the worker thread.

#### `_create_projekt(self)`
- **Purpose**: Initiates the project creation process.
- **Behavior**: 
    - Calls `self.projekt_summary_panel.run_validation()`.
    - If validation passes, prompts the user with a `QMessageBox` whether to launch Flame after creation.
    - Gathers all necessary data (template info, parameters, Flame options) and combines them into `projekt_summary_data`.
    - Adds `launch_flame_after_creation` flag to `projekt_summary_data`.
    - Emits `create_projekt_requested` signal to the worker thread.
    - If validation fails, logs a warning.

## Observations
- `AppWindow` is a complex orchestrator, managing multiple UI panels and coordinating with backend logic through `AppLogic`.
- The use of `QThread` and `Worker` is critical for maintaining UI responsiveness during potentially long-running operations like project creation or template import/export.
- Extensive use of signals and slots facilitates decoupled communication between UI components and the worker thread.
- The `_update_all_summaries` method is a central point for synchronizing data across various display panels.
- Validation is integrated directly into the UI interaction methods (`_export_template_json`, `_create_projekt`), providing immediate feedback to the user.