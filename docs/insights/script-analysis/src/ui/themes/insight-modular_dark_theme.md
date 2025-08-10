# Insight: `modular_dark_theme.py`

## 1. Module Type

`ModularDarkTheme` is a Python module that defines a class responsible for generating the application's visual theme using Qt Style Sheets (QSS). It is not a PySide6 widget itself, but a utility for UI styling.

## 2. Purpose

The primary purpose of this module is to provide a consistent, dark-themed visual style for the entire LOGIK-PROJEKT application. It centralizes all QSS definitions, making it easy to manage and modify the application's look and feel.

## 3. Behavior and Functionality

- **QSS Generation:** The core functionality is provided by the `get_stylesheet()` static method, which constructs a comprehensive QSS string based on predefined configurations.
- **Configurable Theme:** It uses an internal `ThemeConfiguration` class to store color, font, and widget-specific styling parameters. This makes the theme highly configurable without directly modifying the QSS string.
- **Dynamic Color Adjustment:** Includes a `_lighten_color` static method to programmatically adjust color brightness, allowing for consistent hover/pressed states for buttons and entries.
- **Modular Design:** The theme is designed to be modular, allowing for easy extension or modification of individual widget styles.

## 4. Key Attributes and Properties

- `ThemeConfiguration` class: A static class that holds dictionaries for `colors`, `fonts`, and `widgets` styling parameters.
- `LogikProjektModularTheme` class:
  - `_lighten_color(hex_color, percent)`: A static method for color manipulation.
  - `get_stylesheet()`: The main static method that returns the complete QSS string.

## 5. Signals and Slots

This module does not define any PySide6 widgets and therefore does not emit or connect to any signals or slots. Its role is purely to provide static styling data.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: Imports `ui_config` to retrieve fixed dimensions for widgets (e.g., `ENTRY_HEIGHT`, `BUTTON_HEIGHT`, `COMBOBOX_HEIGHT`). This ensures that the QSS styling aligns with the layout dimensions defined elsewhere.
- **`src.app.py` (main application entry point)**: The `get_stylesheet()` method is called in `src/app.py` (formerly `main.py`) to apply the theme to the entire `QApplication` instance.
- **UI Components (indirectly)**: All PySide6 widgets used in the application are indirectly affected by this module, as their appearance is dictated by the QSS generated here.

## 7. Other Useful Information

- **Centralized Styling:** Consolidating all styling in one place significantly improves maintainability. Changes to the visual theme can be made in a single location without modifying individual widget files.
- **Consistency:** Ensures a consistent look and feel across the entire application, enhancing user experience and brand identity.
- **Readability:** By using Python variables for colors and other properties, the QSS string becomes more readable and manageable compared to hardcoding hex values directly.
- **Extensibility:** New widget styles can be easily added to the `get_stylesheet()` method, and new color palettes can be integrated via the `ThemeConfiguration`.
- **Separation of Concerns:** This module effectively separates the UI's visual presentation from its functional logic, adhering to good software design principles.