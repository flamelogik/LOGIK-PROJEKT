# Static Analysis: `src/core/app_logic.py`

## Overview
The `AppLogic` class serves as the core business logic handler for the LOGIK-PROJEKT application. It acts as an orchestrator, delegating specific tasks related to template management and project creation to specialized modules and functions. It centralizes the high-level operations that the UI (`AppWindow`) interacts with.

## Dependencies
- **Python Standard Library**: `json`, `os`
- **Local Modules (src.core)**:
    - `src.core.projekt_manager.projekt_creator.ProjektCreator`
    - `src.core.projekt_manager.projekt_models.ProjektParameters` (used by delegated functions)
    - `src.core.template_manager.template_handler.TemplateHandler`
    - `src.core.template_manager.template_models.TemplateInfo`
    - `src.core.template_manager.template_models.TemplateParameters`
    - `src.core.utils.ocio_utils` (used by delegated functions)
    - `src.core.utils.system_info_utils` (used by delegated functions)
    - `src.core.utils.flame_software_utils` (used by delegated functions)
    - `src.core.functions.io.export_logik_projekt_template.export_logik_projekt_template`
    - `src.core.functions.io.import_logik_projekt_template.import_logik_projekt_template`
    - `src.core.functions.get.get_default_template_values.get_default_template_values`
    - `src.core.functions.get.get_projekt_summary_data.get_projekt_summary_data`
    - `src.core.projekt_manager.projekt_creator.create_projekt`

## Class: `AppLogic`

### Purpose
To encapsulate and manage the core business logic of the LOGIK-PROJEKT application, providing a clean interface for the UI to interact with, and abstracting away the complexities of template handling and project creation.

### Initialization (`__init__`)
- Instantiates `TemplateHandler()` and assigns it to `self.template_handler`.
- Instantiates `ProjektCreator()` and assigns it to `self.projekt_creator`.

### Methods

#### `import_logik_projekt_template(self, file_path: str) -> tuple[TemplateInfo, TemplateParameters, str]`
- **Purpose**: Imports a LOGIK-PROJEKT template from a specified JSON file.
- **Delegation**: Directly calls the standalone function `import_logik_projekt_template`.
- **Returns**: A tuple containing `TemplateInfo` object, `TemplateParameters` object, and a success message string.
- **Error Handling**: Docstring indicates it can raise `FileNotFoundError`, `json.JSONDecodeError`, or generic `Exception`.

#### `export_logik_projekt_template(self, template_info_data: dict, template_params_data: dict) -> str`
- **Purpose**: Exports template data to a current_session-template.json file.
- **Delegation**: Directly calls the standalone function `export_logik_projekt_template`.
- **Returns**: A success message string.
- **Error Handling**: Docstring indicates it can raise a generic `Exception`.

#### `load_default_template_parameters(self) -> dict`
- **Purpose**: Loads default template parameters from a configuration file.
- **Delegation**: Directly calls the standalone function `load_default_template_parameters`.
- **Returns**: A dictionary containing the mapped default parameters.

#### `get_projekt_summary_data(self, template_info: TemplateInfo, template_parameters: TemplateParameters, flame_options_data: dict) -> dict`
- **Purpose**: Generates comprehensive project summary data based on template information, template parameters, and Flame configuration options.
- **Delegation**: Directly calls the standalone function `get_projekt_summary_data`.
- **Returns**: A dictionary containing all the project summary data.

#### `create_projekt(self, projekt_summary_data: dict)`
- **Purpose**: Initiates the creation of a new project using the provided summary data.
- **Delegation**: Directly calls the standalone function `create_projekt`.
- **Returns**: None.

## Observations
- The `AppLogic` class primarily acts as a facade or a coordinator, centralizing access to various core functionalities that are implemented as standalone functions or within other dedicated classes (like `TemplateHandler` and `ProjektCreator`).
- This design promotes modularity and reusability of the underlying functions, as they can be called directly or through the `AppLogic` class.
- The class itself holds instances of `TemplateHandler` and `ProjektCreator`, suggesting that these might manage state or more complex, multi-step operations that are not fully exposed by the simple pass-through methods shown.
- The imports reflect the modules and functions that `AppLogic` directly uses or delegates to, ensuring a clear and manageable dependency graph.
- The clear separation of concerns (UI in `AppWindow`, core logic in `AppLogic`, specific tasks in dedicated functions/modules) is a good architectural pattern.
