# Insight: `app_logic.py`

## 1. Module Type

`app_logic.py` is a core application logic module. It acts as a facade or a coordinator for various business logic operations within the LOGIK-PROJEKT application.

## 2. Purpose

The primary purpose of this module is to centralize the high-level business logic, providing a clean interface for the UI (`AppWindow`) to interact with. It orchestrates calls to specialized modules and functions for tasks like template management, project creation, and data summarization.

## 3. Behavior and Functionality

- **`AppLogic` Class:**
  - **Initialization (`__init__`):**
    - Instantiates `TemplateHandler()` and `ProjektCreator()`. This indicates that `AppLogic` delegates the actual template and project creation tasks to these specialized classes.
  - **`import_logik_projekt_template(self, file_path: str)`:**
    - Purpose: Imports a LOGIK-PROJEKT template from a specified JSON file.
    - Behavior: Calls the standalone function `import_logik_projekt_template` (from `src/core/functions/io/import_logik_projekt_template.py`).
    - Returns: A tuple containing `TemplateInfo` object, `TemplateParameters` object, and a success message string.
  - **`export_logik_projekt_template(self, template_info_data: dict, template_params_data: dict)`:**
    - Purpose: Exports template data to a `current_session-template.json` file.
    - Behavior: Calls the standalone function `export_logik_projekt_template` (from `src/core/functions/io/export_logik_projekt_template.py`).
    - Returns: A success message string.
  - **`get_default_template_values(self)`:**
    - Purpose: Loads default template parameters from a configuration file.
    - Behavior: Calls the standalone function `get_default_template_values` (from `src/core/functions/get/get_default_template_values.py`).
    - Returns: A dictionary containing the mapped default parameters.
  - **`get_projekt_summary_data(self, template_info: TemplateInfo, template_parameters: TemplateParameters, flame_options_data: dict)`:**
    - Purpose: Generates comprehensive project summary data based on template information, template parameters, and Flame configuration options.
    - Behavior: Calls the standalone function `get_projekt_summary_data` (from `src/core/functions/get/get_projekt_summary_data.py`).
    - Returns: A dictionary containing all the project summary data.
  - **`create_projekt(self, projekt_summary_data: dict)`:**
    - Purpose: Initiates the creation of a new project using the provided summary data.
    - Behavior: Calls the standalone function `create_projekt` (from `src/core/projekt_manager/projekt_creator.py`).
    - Returns: None.

## 4. Key Classes

- **`AppLogic`:**
  - Purpose: Encapsulates and manages the core business logic, acting as a facade for the UI.
  - Relationships: Interacts with `TemplateHandler`, `ProjektCreator`, and various standalone utility functions for specific tasks.

## 5. Dependencies and Relationships

- **Standard Python Libraries:** `json`, `os`, `logging`.
- **Internal Dependencies:**
  - `src.core.projekt_manager.projekt_creator.ProjektCreator`
  - `src.core.projekt_manager.projekt_models.ProjektParameters`
  - `src.core.template_manager.template_handler.TemplateHandler`
  - `src.core.template_manager.template_models.TemplateInfo`
  - `src.core.template_manager.template_models.TemplateParameters`
  - `src.core.functions.io.export_logik_projekt_template.export_logik_projekt_template`
  - `src.core.functions.io.import_logik_projekt_template.import_logik_projekt_template`
  - `src.core.functions.get.get_default_template_values.get_default_template_values`
  - `src.core.functions.get.get_projekt_summary_data.get_projekt_summary_data`
  - `src.core.projekt_manager.projekt_creator.create_projekt`
  - `src.core.utils.ocio_utils`
  - `src.core.utils.system_info_utils`
  - `src.core.utils.flame_software_utils`
- **Relationship to the Entire Application:** `AppLogic` is a central component that bridges the UI layer with the backend logic, ensuring that user actions are translated into appropriate business operations.

## 6. Other Useful Information

- **Facade Pattern:** `AppLogic` exemplifies the Facade design pattern, providing a simplified interface to a complex subsystem.
- **Modularity:** The design promotes modularity by delegating specific tasks to other modules, making the codebase easier to understand, test, and maintain.
- **Extensibility:** New business logic or integrations can be added by extending `AppLogic` or by creating new utility functions that `AppLogic` can orchestrate.