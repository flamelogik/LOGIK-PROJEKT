# Static Analysis: `src/ui/widgets/display/template_summary_widget.py`

## Overview
The `TemplateSummaryWidget` class is a custom `QWidget` (from PySide6) designed to display a comprehensive summary of template information. It presents various template attributes in a grid layout, with labels for each field and corresponding `QLabel` widgets to show their values. It is primarily a display-only widget.

## Dependencies
- **PySide6.QtWidgets**: `QWidget`, `QLabel`, `QGridLayout`
- **PySide6.QtCore**: `Qt` (for alignment flags)
- **Local Modules (src.ui)**:
    - `src.ui.ui_config`: Used for layout padding, spacing, and fixed height (`PANEL_PADDING`, `PANEL_LAYOUT_SPACING`).

## Class: `TemplateSummaryWidget`

### Purpose
To provide a clear, organized, and read-only summary of all relevant template information, consolidating data from various input panels for user review.

### Initialization (`__init__`)
- Inherits from `PySide6.QtWidgets.QWidget`.
- Takes `master` (parent widget) as an argument.
- Initializes a `QGridLayout` for the widget.
    - Sets contents margins using `ui_config.PANEL_PADDING`.
    - Sets spacing using `ui_config.PANEL_LAYOUT_SPACING` and a horizontal spacing of 4 pixels.
    - Configures column stretching: Column 0 (labels) takes minimum space, Column 1 (values) takes all remaining space.
- Sets a fixed height for the widget (392 pixels).
- Initializes an empty dictionary `self.fields` to store references to the value `QLabel` widgets, keyed by their data field names.
- Defines a `summary_fields` list, where each tuple contains the display label text and the corresponding data key.
- Iterates through `summary_fields` to create and add `QLabel` widgets to the layout:
    - For each field, a label (`QLabel`) is created with the `label_text` and added to column 0.
    - A value label (`QLabel`) is created (initially empty) and added to column 1.
    - The value label is stored in `self.fields` using its `key`.
- Some fields (e.g., `template_ocio_config`, `template_ocio_path`, `template_cache_integer_id`, `template_cache_float_id`) are commented out, indicating they are hidden in the UI but might be present in the underlying data.

### Methods

#### `set_template_summary_widget_data(data)`
- **Purpose**: Updates the text of the value labels based on the provided `data` dictionary.
- **Behavior**: Iterates through the `self.fields` dictionary. For each `key` and its corresponding `label_widget`, it retrieves the value from the input `data` dictionary using `data.get(key, "")` (providing an empty string as default if the key is missing) and sets the `label_widget`'s text.

#### `get_template_summary_widget_data()`
- **Purpose**: Retrieves the current text displayed in the value labels.
- **Returns**: A dictionary where keys are the data field names and values are the current text displayed in the corresponding `QLabel` widgets.

## Observations
- This widget is a highly structured display component, ideal for presenting a fixed set of information in a readable format.
- The use of `QGridLayout` with specific column stretching ensures a clean, two-column layout.
- The `set_template_summary_widget_data` method provides a convenient way to update all displayed fields at once from a data dictionary.
- The `get_template_summary_widget_data` method, while primarily for display, allows for retrieval of the currently shown data if needed for debugging or other purposes.
- The fixed height and consistent styling (via `ui_config`) contribute to a predictable and polished UI.
- The commented-out fields suggest that the widget is designed to handle more data than it currently displays, allowing for future expansion or selective visibility.
