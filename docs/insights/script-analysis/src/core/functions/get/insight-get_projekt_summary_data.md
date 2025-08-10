# Insight: `get_projekt_summary_data.py`

## 1. Module Type

`get_projekt_summary_data.py` is a Python utility module. It provides a single function to compile and generate a comprehensive summary of project-related data from various sources.

## 2. Purpose

The primary purpose of this module is to consolidate all relevant information about a new project—including user inputs, system environment details, and Flame-specific configurations—into a single, structured dictionary. This summary data is then used for display in UI panels (like `ProjektSummaryWidget`) and for driving the actual project creation process.

## 3. Behavior and Functionality

- **Data Aggregation:** The `get_projekt_summary_data()` function takes three main inputs:
  - `template_info`: An object (instance of `TemplateInfo`) containing basic project details (e.g., calculated name, description).
  - `template_parameters`: An object (instance of `TemplateParameters`) containing detailed technical parameters (e.g., resolution, frame rate, OCIO config).
  - `flame_options_data`: A dictionary containing Flame-specific options (e.g., software choice, directory paths).
- **Environment Data Collection:** It retrieves current user, group, workstation hostname, and operating system information using utility functions from `system_info_utils`.
- **Flame Software Parsing:** It processes the `flame_software_choice` to extract sanitized software names and versions, which are crucial for constructing Flame project names and paths.
- **Dynamic Path Resolution:** It intelligently resolves Flame project directory paths (home, setups, media, catalog) based on user input and predefined rules (e.g., replacing `<project home>` placeholders or appending project names to custom paths).
- **OCIO Details Extraction:** It uses `ocio_utils.get_ocio_details_from_relative_path` to get the full OCIO name and path from the selected OCIO configuration.
- **Data Structuring:** It constructs a large dictionary containing all the aggregated and processed data, with clear and consistent keys.
- **Return Value:** Returns the comprehensive project summary as a dictionary.

## 4. Key Functions

- `get_projekt_summary_data(template_info: TemplateInfo, template_parameters: TemplateParameters, flame_options_data: dict) -> dict`:
  - Purpose: Generates a consolidated dictionary of all project summary data.
  - Arguments: `template_info` (basic project info), `template_parameters` (detailed technical parameters), `flame_options_data` (Flame-specific settings).
  - Returns: A dictionary containing the complete project summary.

## 5. Signals and Slots

This module is a pure utility module and does not interact with PySide6. Therefore, it does not define or use any signals or slots.

## 6. Dependencies and Relationships

- **`src.core.template_manager.template_models`:** Imports `TemplateInfo` and `TemplateParameters` to define the structure of input data.
- **`src.core.utils.system_info_utils`:** Depends on this module for retrieving system-specific information (user, group, hostname).
- **`src.core.utils.flame_software_utils`:** Depends on this module for sanitizing Flame software version names and numbers.
- **`src.core.utils.ocio_utils`:** Depends on this module for extracting OCIO configuration details.
- **`AppLogic`:** This module is a core component of `AppLogic`. `AppLogic` calls `get_projekt_summary_data()` to prepare the data needed for the `ProjektSummaryPanel` and for the actual project creation process.
- **UI Panels:** The output of this function is directly consumed by `ProjektSummaryPanel` to display the final project details to the user.

## 7. Other Useful Information

- **Central Data Hub:** This module acts as a central data hub, bringing together disparate pieces of information from various UI inputs and system queries into a single, coherent data structure. This is crucial for maintaining data consistency and simplifying downstream processes.
- **Business Logic:** It encapsulates significant business logic related to how project names are constructed, paths are resolved, and Flame-specific data is prepared.
- **Flexibility:** By taking structured inputs, it remains flexible and can adapt to changes in how UI data is collected or how Flame options are defined, as long as the input data models are consistent.
- **Debugging:** The comprehensive output dictionary is invaluable for debugging, allowing developers to inspect the exact data that will be used for project creation.