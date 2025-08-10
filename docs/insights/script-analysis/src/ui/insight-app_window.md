# Insight: `app_window.py`

## 1. Widget Type

`AppWindow` is a composite `QWidget` that serves as the main graphical user interface (GUI) window for the LOGIK-PROJEKT application. It acts as the central orchestrator, composing various UI panels and managing their interactions with the application's core logic.

## 2. Purpose

The primary purpose of `AppWindow` is to provide a user-friendly interface for configuring, creating, importing, and exporting project data. It integrates all the individual UI components into a cohesive application flow, handles user actions, and displays feedback.

## 3. Behavior and Functionality

- **Layout Management:** It uses a `QHBoxLayout` to divide the main window into left and right containers, each holding a vertical stack of panels. This provides a clear and organized layout for different sections of the application.
- **Panel Composition:** It instantiates and arranges all the major UI panels:
  - `TemplateInfoPanel` (left)
  - `TemplateParametersPanel` (left)
  - `TemplateSummaryPanel` (left)
  - `ProjektTemplatePanel` (right)
  - `FlameOptionsPanel` (right)
  - `ProjektSummaryPanel` (right)
- **Data Flow Orchestration:** It gathers data from input panels (e.g., `TemplateInfoPanel`, `TemplateParametersPanel`, `FlameOptionsPanel`), combines them, and passes them to summary panels (`TemplateSummaryPanel`, `ProjektSummaryPanel`, `ProjektTemplatePanel`) to ensure real-time updates and consistency across the UI.
- **Action Triggers:** It connects the `clicked` signals of the main action buttons (Export Template, Import Template, Create Projekt) to internal methods that then emit custom signals to a separate `Worker` thread for execution.
- **Threading for Responsiveness:** It utilizes a `QThread` and a `Worker` `QObject` to perform long-running operations (like project creation, template import/export) in a separate thread. This prevents the GUI from freezing and keeps the application responsive.
- **Error Handling and User Feedback:** It connects signals from the `Worker` thread to display success messages (`QMessageBox.information`) or critical errors (`QMessageBox.critical`) to the user.
- **Thread-Safe Logging:** It integrates a custom `LogEmitter` and `SignalHandler` to ensure that logging messages from any thread are safely displayed in the `ProjektSummaryPanel`'s `QTextEdit`.

## 4. Key Attributes and Properties

- `self.app_logic`: An instance of `AppLogic`, providing access to the application's core business logic.
- `self.main_layout`, `self.left_layout`, `self.right_layout`: Layout managers for organizing widgets.
- `self.template_info_panel`, `self.template_parameters_panel`, `self.template_summary_panel`, `self.projekt_template_panel`, `self.flame_options_panel`, `self.projekt_summary_panel`: Instances of the various UI panels.
- `self.thread`: A `QThread` instance to run background tasks.
- `self.worker`: An instance of the `Worker` `QObject`, which contains the actual long-running methods.
- `self.log_emitter`, `self.log_handler`: Objects for managing thread-safe logging to the UI.

## 5. Signals and Slots

- **Custom Signals (emitted by `AppWindow`):**
  - `create_projekt_requested(dict)`: Emitted when the "Create Projekt" button is clicked, carrying the project summary data.
  - `export_template_requested(dict, dict)`: Emitted when the "Export Template" button is clicked, carrying template info and parameters.
  - `import_template_requested(str)`: Emitted when the "Import Template" button is clicked, carrying the file path.
- **Custom Signals (emitted by `Worker` and connected to `AppWindow`):**
  - `finished()`: Emitted when a worker task completes.
  - `error(str)`: Emitted when an error occurs in a worker task.
  - `template_imported(dict, dict)`: Emitted after a template is successfully imported, carrying the loaded data.
  - `template_exported(str)`: Emitted after a template is successfully exported, carrying a success message.
- **Internal Slots (in `AppWindow`):**
  - `on_worker_finished()`: Handles the completion of worker tasks.
  - `on_worker_error(error_message)`: Displays error messages from the worker.
  - `on_template_exported(export_message)`: Displays success message after template export.
  - `on_template_imported(template_info, template_parameters)`: Populates panels with imported template data and updates summaries.
  - `_update_all_summaries()`: Gathers data from input panels, updates summary panels, and sets the project name for the Flame options panel.
  - `_export_template_json()`: Initiates the template export process, including validation and emitting `export_template_requested`.
  - `_import_template_json()`: Opens a file dialog for template import and emits `import_template_requested`.
  - `_create_projekt()`: Initiates the project creation process, including validation and emitting `create_projekt_requested`.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: Imports `ui_config` for defining fixed dimensions and layout margins, ensuring consistent UI sizing.
- **All Panels (from `src/ui/panels`)**: `AppWindow` acts as the parent and coordinator for all the individual UI panels, managing their creation, placement, and data exchange.
- **`src.core.app_logic`**: `AppWindow` holds an instance of `AppLogic` and delegates all business logic operations (like getting default values, importing/exporting templates, getting project summary data) to it.
- **`src.core.projekt_manager.projekt_creator`**: The `Worker` directly calls `create_projekt` to perform the actual project creation.
- **`src.core.template_manager.template_models`**: Used to structure data passed between `AppWindow` and `AppLogic` for template operations.
- **`src.core.utils.validation_utils`**: Used for pre-action validation (e.g., before exporting a template or creating a project).
- **`src.core.utils.threaded_logging_utils`**: Essential for displaying log messages from background threads safely in the UI.
- **PySide6 Core Modules (`QThread`, `QObject`, `Signal`, `Slot`, `QFileDialog`, `QMessageBox`)**: Relies heavily on these fundamental PySide6 components for threading, inter-object communication, file system interaction, and user feedback.

## 7. UI/UX Notes

`AppWindow` is designed to provide a seamless and responsive user experience. By offloading long-running tasks to a separate thread, it prevents the UI from becoming unresponsive. The clear separation of panels, real-time updates of summary information, and explicit action buttons contribute to an intuitive workflow. The integration of validation and informative message boxes guides the user through the process and provides immediate feedback on the success or failure of operations.