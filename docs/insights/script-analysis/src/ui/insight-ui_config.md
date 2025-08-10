# Insight: `ui_config.py`

## 1. Module Type

`ui_config.py` is a Python module that serves as a centralized configuration file for the user interface of the LOGIK-PROJEKT application. It does not define any PySide6 widgets or classes, but rather provides a collection of constants.

## 2. Purpose

The primary purpose of this module is to define and centralize all key dimensions, paddings, spacing, and other layout-related values for the application's GUI. This ensures a consistent look and feel across all UI components and simplifies future adjustments or redesigns.

## 3. Behavior and Functionality

- **Static Configuration:** The module contains a series of global constants (e.g., `WINDOW_WIDTH`, `ENTRY_HEIGHT`, `PANEL_PADDING`). These values are loaded once when the module is imported and remain constant throughout the application's runtime.
- **Read-Only Access:** The values defined in this module are intended to be read-only. Other UI components import this module and use these constants to set their dimensions and layout properties.
- **Centralized Management:** By having all UI-related numerical configurations in one place, developers can easily modify the application's layout and sizing without having to search through multiple widget or panel files.

## 4. Key Attributes and Properties

- **Window Settings:**
  - `WINDOW_WIDTH`, `WINDOW_HEIGHT`: Defines the main application window dimensions.
- **Panel Settings:**
  - `LEFT_CONTAINER_WIDTH`, `RIGHT_CONTAINER_WIDTH`: Defines the width of the main layout containers.
  - `TEMPLATE_INFO_PANEL_HEIGHT`, `TEMPLATE_PARAMETERS_PANEL_HEIGHT`, etc.: Defines fixed heights for various UI panels.
- **Widget Settings:**
  - `WIDGET_HEIGHT`, `ENTRY_HEIGHT`, `COMBOBOX_HEIGHT`, `BUTTON_HEIGHT`: Defines standard heights for common input widgets.
- **Layout Settings:**
  - `MAIN_LAYOUT_MARGINS`: Defines margins for the top-level layout.
  - `PANEL_LAYOUT_SPACING`: Defines spacing between widgets within panels.
  - `PANEL_PADDING`: Defines padding around the content of panels.

## 5. Signals and Slots

This module does not define any PySide6 widgets or classes, and therefore, it does not emit or connect to any signals or slots. Its role is purely to provide static configuration data.

## 6. Dependencies and Relationships

- **`src.ui.app_window.py`**: The main `AppWindow` imports and uses these constants to set the dimensions of the main window and its primary containers.
- **All UI Panels (e.g., `TemplateInfoPanel`, `FlameOptionsPanel`)**: Almost all custom UI panels import `ui_config` to set their layout spacing, margins, and the fixed heights of their child widgets (entries, comboboxes, buttons).
- **UI Widgets (e.g., `aspect_ratio_widget.py`, `bit_depth_widget.py`)**: Individual custom widgets import `ui_config` to ensure their heights and other dimensions conform to the application's standard.
- **`src.ui.themes.modular_dark_theme.py`**: The theme module uses `ui_config` constants to define widget heights in its QSS, ensuring that the visual styling matches the layout dimensions.

## 7. Other Useful Information

- **Consistency and Maintainability:** This module is fundamental for maintaining a consistent and professional UI. Any changes to the application's visual spacing or sizing can be made in this single file, significantly reducing the effort and potential for errors compared to modifying values scattered across many files.
- **Readability:** By giving meaningful names to numerical constants, the code in other UI modules becomes more readable and understandable.
- **Rapid Prototyping/Theming:** It facilitates rapid prototyping and theming by allowing quick adjustments to the overall UI scale and appearance without touching the underlying widget logic.