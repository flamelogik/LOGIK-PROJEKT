# `src/app.py`: Core Application Entry Point and Orchestration

## 1. Purpose and Role

`src/app.py` serves as the primary entry point for the LOGIK-PROJEKT application. Its fundamental role is to:
*   Initialize the PySide6 application environment.
*   Establish the main application window (`QMainWindow`).
*   Instantiate and integrate the `AppWindow` (the central UI component) and its constituent panels.
*   Configure application-wide settings such as logging and stylesheets.
*   Initiate and manage the Qt event loop, ensuring application responsiveness.

It acts as the orchestrator, bringing together the UI layer (`src/ui/`) and the core business logic (`src/core/`) without directly implementing complex business rules.

## 2. Architectural Overview

`app.py` adheres to a clean separation of concerns, primarily focusing on application bootstrapping and UI composition. It instantiates `QApplication` and `QMainWindow`, then delegates the complex UI layout and interaction management to `src.ui.app_window.AppWindow`.

The application employs a multi-threaded approach for long-running operations (e.g., template import/export, project creation) to maintain UI responsiveness. This is managed via `QThread` and a `QObject`-based `Worker` class within `AppWindow`, with `app.py` merely initiating the `QMainWindow` and `AppWindow` instances.

## 3. Key Components and Their Responsibilities

*   **`main()` function**:
    *   **Logging Setup**: Configures a root `logging` instance with both console and file handlers. Session-specific log files are generated with a timestamp and organized by date (`logs/session-logs/YYYY/MM/DD/`).
    *   **`QApplication`**: The core PySide6 application object, responsible for event handling and application-wide resources.
    *   **Stylesheet Application**: Applies the global UI theme via `src.ui.themes.modular_dark_theme.LogikProjektModularTheme.get_stylesheet()`.
    *   **`QMainWindow`**: The top-level application window. `app.py` sets its title and calculates its initial geometry to center it on the primary screen, leveraging `src.ui.ui_config` for dimensions.
    *   **`AppWindow` (from `src.ui.app_window.py`)**: This is the central widget of `QMainWindow`. `app.py` instantiates it, passing the `QMainWindow` as its parent. `AppWindow` is responsible for:
        *   Composing the main UI layout (left and right containers).
        *   Instantiating and arranging all individual UI panels (e.g., `TemplateInfoPanel`, `TemplateParametersPanel`, `FlameOptionsPanel`, `ProjektTemplatePanel`, `TemplateSummaryPanel`, `ProjektSummaryPanel`).
        *   Managing signal-slot connections between UI elements and the `AppLogic` layer.
        *   Implementing the `QThread`/`Worker` pattern for asynchronous operations.
        *   Handling user interactions for template import/export and project creation, delegating to the `Worker` and `AppLogic`.
    *   **Event Loop**: Calls `app.exec_()` to start the Qt event loop, which processes events and keeps the application running until termination.

## 4. Data Flow and State Management

`app.py` itself does not directly manage application state beyond UI window properties. State management is primarily handled within `AppWindow` and its child panels, which then interact with the `AppLogic` layer.

*   **UI Panels as Data Sources**: Individual panels (e.g., `TemplateInfoPanel`, `TemplateParametersPanel`, `FlameOptionsPanel`) encapsulate their respective data inputs.
*   **`_update_all_summaries()` (in `AppWindow`)**: This method is critical for synchronizing UI state. It retrieves data from input panels, combines it, and passes it to `AppLogic.get_projekt_summary_data()` to generate the comprehensive project summary displayed in `ProjektSummaryPanel`.
*   **`AppLogic` as Business Logic Facade**: `src.core.app_logic.AppLogic` acts as a facade, providing methods for `AppWindow` to interact with the underlying template management (`TemplateHandler`) and project creation (`ProjektCreator`) components. Data is passed between `AppWindow` and `AppLogic` primarily as dictionaries or dataclass instances (`TemplateInfo`, `TemplateParameters`).

## 5. Concurrency and Responsiveness

The application employs a dedicated `QThread` and `Worker` object (defined within `src/ui/app_window.py`) to execute potentially long-running operations (e.g., file I/O, complex calculations) off the main GUI thread. This prevents the UI from freezing and ensures a smooth user experience. `app.py`'s role is limited to initiating the `AppWindow` which then sets up this threading model.

## 6. Extensibility and Maintainability

The design promotes extensibility and maintainability through:
*   **Modular UI Panels**: Each panel is a self-contained `QWidget`, making it easy to add, remove, or modify UI sections without impacting others.
*   **Separation of Concerns**: Clear distinction between UI presentation (`src/ui/`) and business logic (`src/core/`).
*   **Facade Pattern (`AppLogic`)**: Simplifies the interface between the UI and the core functionalities, reducing direct dependencies on lower-level modules.
*   **Signal-Slot Mechanism**: Qt's signal-slot system provides a robust and decoupled way for components to communicate.
*   **Configuration-driven UI (`ui_config.py`)**: Centralizes UI dimensions and layout parameters, simplifying global UI adjustments.

## 7. Logging and Error Handling

*   **Centralized Logging**: `app.py` initializes a robust logging system that outputs to both console and a timestamped file. This is crucial for debugging and monitoring application behavior in production.
*   **Thread-Safe Logging**: `AppWindow` integrates `src.core.utils.threaded_logging_utils.LogEmitter` and `SignalHandler` to ensure that log messages from worker threads are safely relayed to the main UI thread (specifically, to the `ProjektSummaryPanel`'s shell output display).
*   **GUI-based Error Reporting**: Critical errors caught in worker threads or UI interactions are presented to the user via `QMessageBox` for immediate feedback.

## 8. Dependencies

`app.py` directly imports and relies on:
*   `sys`, `logging`, `os`, `datetime` (Python standard library)
*   `PySide6.QtWidgets` (for GUI components)
*   `src.ui.app_window.AppWindow` (the main UI widget)
*   `src.ui.themes.modular_dark_theme.LogikProjektModularTheme` (for styling)
*   `src.ui.ui_config` (for UI dimensions and layout constants)

Indirectly, through `AppWindow` and `AppLogic`, it depends on a wide array of modules within `src/core/` and `src/ui/panels/`.

## 9. `src` Directory Structure and Annotations

The `src` directory is the heart of the LOGIK-PROJEKT application, housing all the Python source code. It's organized into logical subdirectories to promote modularity, maintainability, and a clear separation of concerns.

```
src/
├── __init__.py                                       # Python package initializer for 'src'
├── app.py                                            # Main application entry point and orchestrator
├── core/                                             # Contains the core business logic and data models
│   ├── __init__.py                                   # Python package initializer for 'core'
│   ├── app_logic.py                                  # Facade for core application logic, interacts with UI
│   ├── functions/                                    # Collection of utility functions grouped by purpose
│   │   ├── __init__.py                               # Python package initializer for 'functions'
│   │   ├── copy/                                     # Functions for copying files and configurations
│   │   │   ├── __init__.py
│   │   │   ├── copy_current_session_files.py
│   │   │   ├── copy_flame_bookmarks.py
│   │   │   ├── copy_flame_presets.py
│   │   │   └── copy_flame_python_scripts.py
│   │   ├── create/                                   # Functions for creating various project-related assets
│   │   │   ├── __init__.py
│   │   │   ├── create_flame_archive_script.py
│   │   │   ├── create_flame_launcher_script.py
│   │   │   ├── create_flame_setup_dirs.py
│   │   │   ├── create_flame_startup_script.py
│   │   │   ├── create_flame_symbolic_links.py
│   │   │   ├── create_flame_wiretap_node.py
│   │   │   ├── create_projekt_backup_script.py
│   │   │   ├── create_projekt_filesystem_dirs.py
│   │   │   ├── create_projekt_launcher_alias.py
│   │   │   └── create_projekt_pgsql_db.py
│   │   ├── get/                                      # Functions for retrieving data and configurations
│   │   │   ├── __init__.py
│   │   │   ├── get_application_paths.py
│   │   │   ├── get_bit_depth_values.py
│   │   │   ├── get_cache_float_values.py
│   │   │   ├── get_cache_integers_values.py
│   │   │   ├── get_default_template_values.py
│   │   │   ├── get_flame_bookmarks_path.py
│   │   │   ├── get_flame_software_versions.py
│   │   │   ├── get_frame_rate_values.py
│   │   │   ├── get_init_config_values.py
│   │   │   ├── get_json_data.py
│   │   │   ├── get_logik_projekt_config_values.py
│   │   │   ├── get_ocio_config_values.py
│   │   │   ├── get_projekt_summary_data.py
│   │   │   ├── get_resolution_values.py
│   │   │   ├── get_scan_mode_values.py
│   │   │   ├── get_start_frame_values.py
│   │   │   ├── get_sysconfig_flame_catalog_dir.py
│   │   │   ├── get_sysconfig_flame_home_dir.py
│   │   │   ├── get_sysconfig_flame_media_dir.py
│   │   │   └── get_sysconfig_flame_setups_dir.py
│   │   └── io/                                       # Functions for input/output operations (e.g., template handling)
│   │       ├── __init__.py
│   │       ├── export_logik_projekt_template.py
│   │       ├── export_session_adsk_json.py
│   │       ├── export_session_variables.py
│   │       ├── export_session_xml.py
│   │       └── import_logik_projekt_template.py
│   ├── projekt_manager/                              # Modules related to project creation and management
│   │   ├── __init__.py
│   │   ├── projekt_creator.py                        # Handles the actual creation of Flame projects and file structures
│   │   └── projekt_models.py                         # Data models for project parameters
│   ├── template_manager/                             # Modules for handling project templates
│   │   ├── __init__.py
│   │   ├── template_handler.py                       # Manages template import/export logic
│   │   ├── template_models.py                        # Data models for template information and parameters
│   │   └── template_serializers.py                   # Handles serialization/deserialization of templates
│   ├── unused/                                       # Contains modules that are currently not in use but might be in the future
│   │   ├── __init__.py
│   │   ├── config_utils.py
│   │   ├── logik_projekt_dark_theme.py
│   │   ├── script_utils.py
│   │   └── string_utils.py
│   └── utils/                                        # General utility functions used across the core logic
│       ├── __init__.py
│       ├── backup_utils.py
│       ├── calculated_name_utils.py
│       ├── flame_software_utils.py                   # Utilities for interacting with Flame software
│       ├── logik_projekt_utils.py
│       ├── ocio_utils.py                             # Utilities for OpenColorIO (OCIO) configurations
│       ├── path_utils.py                             # Path manipulation utilities
│       ├── system_info_utils.py                      # System information retrieval utilities
│       ├── threaded_logging_utils.py                 # Utilities for thread-safe logging
│       └── validation_utils.py                       # Utilities for data validation
├── ui/                                               # Contains all User Interface related components
│   ├── __init__.py                                   # Python package initializer for 'ui'
│   ├── app_window.py                                 # Defines the main application window layout and panel integration
│   ├── panels/                                       # Individual UI panels that make up the main window
│   │   ├── __init__.py
│   │   ├── flame_options_panel.py                    # Panel for Flame-specific settings
│   │   ├── projekt_summary_panel.py                  # Panel displaying a summary of the project to be created
│   │   ├── projekt_template_panel.py                 # Panel for importing existing project templates
│   │   ├── template_info_panel.py                    # Panel for basic template information input
│   │   ├── template_parameters_panel.py              # Panel for technical template parameters input
│   │   └── template_summary_panel.py                 # Panel displaying a summary of the template being built
│   ├── themes/                                       # UI themes and styling
│   │   ├── __init__.py
│   │   ├── logik_projekt_spectrum_color.py           # Color definitions for the theme
│   │   └── modular_dark_theme.py                     # Defines the application's dark theme
│   ├── ui_config.py                                  # Centralized UI configuration constants (dimensions, margins, etc.)
│   └── widgets/                                      # Reusable UI widgets (buttons, comboboxes, entry fields)
│       ├── __init__.py
│       ├── button/                                   # Custom button widgets
│       │   ├── __init__.py
│       │   ├── create_projekt_widget.py
│       │   ├── export_template_widget.py
│       │   ├── flame_catalog_dir_widget.py
│       │   ├── flame_home_dir_widget.py
│       │   ├── flame_media_dir_widget.py
│       │   ├── flame_setups_dir_widget.py
│       │   └── import_template_widget.py
│       ├── combobox/                                 # Custom combobox widgets
│       │   ├── __init__.py
│       │   ├── bit_depth_widget.py
│       │   ├── cache_float_widget.py
│       │   ├── cache_integer_widget.py
│       │   ├── flame_software_choice_widget.py
│       │   ├── frame_rate_widget.py
│       │   ├── init_config_widget.py
│       │   ├── ocio_config_widget.py
│       │   ├── projekt_config_widget.py
│       │   ├── resolution_widget.py
│       │   ├── scan_mode_widget.py
│       │   └── start_frame_widget.py
│       ├── display/                                  # Widgets for displaying information (read-only)
│       │   ├── __init__.py
│       │   ├── projekt_summary_widget.py
│       │   ├── projekt_template_widget.py
│       │   └── template_summary_widget.py
│       └── entry/                                    # Custom text entry widgets
│           ├── __init__.py
│           ├── aspect_ratio_widget.py
│           ├── calculated_name_widget.py
│           ├── campaign_name_widget.py
│           ├── client_name_widget.py
│           ├── description_widget.py
│           ├── resolution_height_widget.py
│           ├── resolution_width_widget.py
│           └── serial_number_widget.py
└── utils/                                            # General utilities not directly tied to core logic or UI
    ├── __init__.py
    └── common/                                       # Common utility functions
        ├── __init__.py
        └── create/                                   # Functions for creating common assets/structures
            ├── __init__.py
            ├── create_banners.py
            ├── create_customized_filesystem_template.py
            ├── create_logs.py
            ├── create_separators.py
            ├── create_timestamp.py
            ├── directory_structure_analysis.py
            ├── directory_structure_to_bookmarks.py
            ├── directory_structure_to_json.py
```
