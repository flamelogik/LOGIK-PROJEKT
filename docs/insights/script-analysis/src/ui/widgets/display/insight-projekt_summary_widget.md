# Insight: `projekt_summary_widget.py`

## 1. Widget Type

`ProjektSummaryWidget` is a composite `QWidget` that utilizes a `QGridLayout` to display a read-only summary of various project configuration details. It consists of multiple `QLabel` instances arranged in a two-column layout.

## 2. Purpose

This widget provides a comprehensive, at-a-glance overview of all the key parameters and settings chosen for the new project. It acts as a final confirmation screen before project creation, ensuring the user can review all details.

## 3. Behavior and Functionality

- **Read-Only Display:** All fields within this widget are `QLabel`s, making them read-only. This prevents accidental modification of the summarized data and ensures that the displayed information accurately reflects the current project configuration.
- **Data Population:** The `set_data(data)` method is the primary way to update the widget. It expects a dictionary where keys correspond to the `summary_fields` defined internally, and values are the data to be displayed. This allows for dynamic updates as the user makes selections in other parts of the UI.
- **Structured Layout:** A `QGridLayout` is used to arrange the labels and their corresponding values in a clear, tabular format. Column stretching ensures that value labels take up available space.
- **Fixed Height:** The widget has a fixed height, contributing to a consistent overall UI layout.

## 4. Key Attributes and Properties

- `self.layout`: A `QGridLayout` instance managing the arrangement of child widgets.
- `self.fields`: A dictionary that maps internal data keys (e.g., `"current_user"`) to the `QLabel` widgets responsible for displaying their values. This allows for easy programmatic access to update specific fields.
- `summary_fields`: A list of tuples `(label_text, key)` that defines the static labels and their corresponding data keys to be displayed.

## 5. Signals and Slots

- **Signals:** This widget does not emit any custom signals, as its primary role is to display information.
- **Slots (Public Methods):**
  - `set_data(self, data: dict)`: A public method that acts as a slot to update all the summary fields based on the provided dictionary. This is the main interface for external components to push data to the summary.
  - `get_data(self)`: A public method that retrieves the currently displayed text from all value labels. While primarily for display, this could be used for debugging or saving the displayed state.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: Imports `ui_config` to set layout properties such as `PANEL_PADDING`, `PANEL_LAYOUT_SPACING`, and to define the fixed height of the widget. This ensures visual consistency with other UI panels.
- **`AppLogic` (or a central data model/controller)**: This widget is a consumer of consolidated project data. A central application logic component is responsible for gathering all relevant information from various input widgets (e.g., `ClientNameWidget`, `ResolutionWidget`, `FlameSoftwareChoiceWidget`, etc.) and then passing this complete data dictionary to the `set_data()` method of `ProjektSummaryWidget`. This makes the summary panel reactive to user input across the application.

## 7. UI/UX Notes

The `ProjektSummaryWidget` is crucial for user confidence and error prevention. By presenting all collected data in a clear, organized, and read-only format, it allows the user to verify their selections before committing to project creation. The use of `QGridLayout` with column stretching ensures that the summary is readable and well-aligned, regardless of the length of the displayed values.