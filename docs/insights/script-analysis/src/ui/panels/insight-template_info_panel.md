# Insight: `template_info_panel.py`

## 1. Widget Type

`TemplateInfoPanel` is a composite `QWidget` that serves as an input panel for core template information. It uses a `QGridLayout` to arrange several custom entry widgets.

## 2. Purpose

This panel allows users to input fundamental details for a project template, such as a serial number, client name, campaign name, and a general description. Crucially, it also dynamically calculates and displays a project name based on some of these inputs.

## 3. Behavior and Functionality

- **Input Fields:** It composes instances of `SerialNumberWidget`, `ClientNameWidget`, `CampaignNameWidget`, `CalculatedNameWidget`, and `DescriptionWidget` to gather user input.
- **Dynamic Name Calculation:** The `_update_calculated_name()` method is central to this panel. It listens for changes in the serial number, client name, and campaign name fields. When any of these change, it calls an external utility function (`get_calculated_name`) to generate a new project name and updates the `CalculatedNameWidget`.
- **Data Retrieval:** The `get_template_info()` method collects all the current values from its child widgets and returns them as a dictionary.
- **Data Setting:** The `set_template_info(info)` method allows for programmatically populating the panel's input fields, useful for loading data from existing templates.
- **Signal Emission:** It emits a custom `calculated_name_updated` signal whenever the calculated project name changes, notifying other parts of the application that might depend on this value.

## 4. Key Attributes and Properties

- `self.serial_number_widget`: An instance of `SerialNumberWidget`.
- `self.client_name_widget`: An instance of `ClientNameWidget`.
- `self.campaign_name_widget`: An instance of `CampaignNameWidget`.
- `self.calculated_name_widget`: An instance of `CalculatedNameWidget`.
- `self.description_widget`: An instance of `DescriptionWidget`.
- `self.calculated_name_updated`: A custom `Signal` emitted when the calculated name changes.

## 5. Signals and Slots

- **Custom Signals:**
  - `calculated_name_updated`: Emitted after the `_update_calculated_name` method is called and the calculated name is updated. This signal is crucial for keeping other parts of the UI (like summary panels) synchronized.
- **Internal Slots:**
  - `_update_calculated_name()`: A slot connected to the `textChanged` signals of the serial number, client name, campaign name, and description widgets. This method orchestrates the calculation and update of the project name.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: Imports `ui_config` for consistent layout and spacing parameters (`PANEL_LAYOUT_SPACING`, `PANEL_PADDING`).
- **Custom Entry Widgets (from `src/ui/widgets/entry`)**: This panel composes several custom input and display widgets, demonstrating a modular UI design.
- **`src.core.utils.calculated_name_utils`**: Directly calls `get_calculated_name` from this module to perform the logic for generating the project name. This separates the UI from the business logic of name calculation.
- **`AppLogic` (or main application controller)**: This panel is a primary source of user input. `AppLogic` would call `get_template_info()` to retrieve the user's selections. Conversely, `AppLogic` might call `set_template_info()` to load default or template-based settings into the panel.
- **`ProjektSummaryPanel` and `TemplateSummaryPanel`**: The `calculated_name_updated` signal from this panel would likely be connected to a slot in `AppLogic` that updates these summary panels to reflect the dynamically generated project name.

## 7. UI/UX Notes

This panel provides a highly interactive and user-friendly experience for defining project details. The real-time calculation of the project name as the user types provides immediate feedback and reinforces the naming conventions. The clear separation of input fields and the calculated output makes the process transparent. The ability to load and save these settings via `set_template_info()` and `get_template_info()` further enhances usability and workflow efficiency.