# Insight: `template_summary_widget.py`

## 1. Widget Type

`TemplateSummaryWidget` is a composite `QWidget` that uses a `QGridLayout` to display a read-only summary of various template configuration details. It is composed of multiple `QLabel` instances.

## 2. Purpose

This widget provides a detailed, read-only overview of the parameters that define a project template. It allows users to review the settings that will be applied when a template is imported or exported, ensuring transparency and accuracy.

## 3. Behavior and Functionality

- **Read-Only Display:** All fields are `QLabel`s, making them non-editable. This ensures that the displayed template information is for review only and cannot be accidentally altered.
- **Data Population:** The `set_template_summary_widget_data(data)` method is used to populate the widget. It expects a dictionary where keys correspond to the `summary_fields` defined internally, and values are the data to be displayed. This allows for dynamic updates when a template is loaded.
- **Structured Layout:** A `QGridLayout` organizes the labels and their corresponding values in a clear, tabular format. Column stretching ensures proper alignment and space distribution.
- **Fixed Height:** The widget has a fixed height for consistent UI layout.

## 4. Key Attributes and Properties

- `self.layout`: A `QGridLayout` instance managing the arrangement of child widgets.
- `self.fields`: A dictionary that maps internal data keys (e.g., `"template_serial_number"`) to the `QLabel` widgets responsible for displaying their values. This facilitates programmatic updates.
- `summary_fields`: A list of tuples `(label_text, key)` that defines the static labels and their corresponding data keys to be displayed. This list includes various template attributes like serial number, client, campaign, name, description, resolution, bit depth, frame rate, scan mode, start frame, and configuration details.

## 5. Signals and Slots

- **Signals:** This widget does not emit any custom signals, as its primary role is to display information.
- **Slots (Public Methods):**
  - `set_template_summary_widget_data(self, data: dict)`: A public method that acts as a slot to update all the template fields based on the provided dictionary. This is the main interface for external components to push data to the template summary.
  - `get_template_summary_widget_data(self)`: A public method that retrieves the currently displayed text from all value labels. This can be useful for debugging or for saving the displayed state.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: Imports `ui_config` to set layout properties such as `PANEL_PADDING`, `PANEL_LAYOUT_SPACING`, and to define the fixed height of the widget. This ensures visual consistency with other UI panels.
- **`TemplateHandler` (or a central data model/controller)**: This widget is a consumer of template data. A central application logic component (e.g., `TemplateHandler` in `src/core/template_manager/`) is responsible for loading template data and then passing this data dictionary to the `set_template_summary_widget_data()` method of `TemplateSummaryWidget`. This makes the template summary panel reactive to template loading events.

## 7. UI/UX Notes

The `TemplateSummaryWidget` is essential for providing transparency and control over project templates. By presenting all template-related data in a clear, organized, and read-only format, it allows the user to verify the contents of a template before applying it or exporting it. The use of `QGridLayout` with column stretching ensures that the summary is readable and well-aligned, regardless of the length of the displayed values.