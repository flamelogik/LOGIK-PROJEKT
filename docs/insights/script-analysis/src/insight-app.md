# Insight: `app.py`

## 1. Module Type

`app.py` is the main entry point for the LOGIK-PROJEKT application. It is an application script that initializes and runs the PySide6 GUI.

## 2. Purpose

The primary purpose of this module is to set up the application environment, configure logging, initialize the PySide6 application, apply the visual theme, create and display the main application window, and start the event loop. It serves as the bootstrap for the entire GUI application.

## 3. Behavior and Functionality

- **`main()` function:**
  - This is the core function executed when the script is run.
  - **Logging Configuration:**
    - Configures the root Python logger for console output with `DEBUG` level and a specific format.
    - Generates a timestamped session log file path within `logs/session-logs/YYYY/MM/DD/`.
    - Creates the necessary log directories if they don't exist.
    - Adds a `FileHandler` to the root logger to write all log messages to the session log file.
  - **PySide6 Application Initialization:**
    - Creates a `QApplication` instance, which is the central object for any PySide6 application.
  - **Theme Application:**
    - Applies a custom stylesheet obtained from `LogikProjektModularTheme.get_stylesheet()` to the entire application.
  - **Main Window Setup:**
    - Creates a `QMainWindow` instance, which serves as the top-level window for the application.
    - Sets the window title to "LOGIK-PROJEKT 2026.1".
    - **Window Positioning:** Calculates the center position of the screen and sets the main window's geometry (position and size) based on `ui_config.WINDOW_WIDTH` and `ui_config.WINDOW_HEIGHT`. If screen information is unavailable, it defaults to a fixed position.
  - **Central Widget:**
    - Creates an instance of `AppWindow` (the main application widget) and sets it as the central widget of the `QMainWindow`.
  - **Display and Event Loop:**
    - Calls `main_window.show()` to make the window visible.
    - Enters the PySide6 event loop using `app.exec()`, which keeps the application running and responsive to user interactions until it's closed.
  - **Exit:** Calls `sys.exit()` with the application's exit code when the event loop finishes.

## 4. Key Functions

- **`main() -> None`:**
  - Purpose: The primary function that orchestrates the application's startup, including logging, GUI initialization, and display.
  - Arguments: None.
  - Returns: None.

## 5. Signals and Slots

This module primarily sets up the PySide6 application and its main window. While it doesn't define custom signals or slots, it relies heavily on the PySide6 framework's signal/slot mechanism for GUI interaction.

- It initializes `QApplication`, which manages the event loop and signal/slot connections.
- It sets up `AppWindow`, which is expected to contain and manage various UI widgets that will use signals and slots for their functionality.

## 6. Dependencies and Relationships

- **Standard Python Libraries:** `sys`, `logging`, `os`, `datetime`.
- **External Libraries:** `PySide6.QtWidgets` (specifically `QApplication`, `QMainWindow`).
- **Internal Dependencies:**
  - `src.ui.app_window.AppWindow`: The main widget that forms the content of the application's window.
  - `src.ui.themes.modular_dark_theme.LogikProjektModularTheme`: Provides the stylesheet for the application's visual theme.
  - `src.ui.ui_config`: Contains configuration constants for UI elements, such as window dimensions.
- **Relationship to the Entire Application:** This module is the root of the application's execution. It brings together the UI components, styling, and logging infrastructure to present a functional GUI to the user.

## 7. Other Useful Information

- **Application Entry Point:** This is the file that should be executed to start the LOGIK-PROJEKT GUI application.
- **Centralized Setup:** All fundamental application-wide configurations (logging, theme, window properties) are handled here, ensuring consistency.
- **Logging:** The robust logging setup ensures that all application events and potential errors are recorded, which is crucial for debugging and monitoring.
- **Modularity:** By importing `AppWindow`, `LogikProjektModularTheme`, and `ui_config`, this module demonstrates a modular design where different aspects of the application are separated into distinct files and modules.