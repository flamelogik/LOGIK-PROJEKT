# Insight: `template_handler.py`

## 1. Module Type

`template_handler.py` is a Python module that provides a high-level interface for managing project templates within the LOGIK-PROJEKT application.

## 2. Purpose

The primary purpose of this module is to centralize the operations related to saving, loading, and listing project templates. It acts as an intermediary between the application's core logic/UI and the data serialization/deserialization mechanisms for templates.

## 3. Behavior and Functionality

- **`TemplateHandler` Class:**
  - **`__init__(self)`:**
    - Initializes an instance of `TemplateSerializer`, which is used for handling the actual reading and writing of template data to/from files.
  - **`export_template(self, template_info: TemplateInfo, template_parameters: TemplateParameters, file_name: str)`:**
    - Takes `TemplateInfo` and `TemplateParameters` objects, along with a desired `file_name`.
    - Constructs the absolute path where the template JSON file will be saved (within `config/logik-projekt-configuration/logik-projekt-templates`).
    - Ensures the target directory exists using `path_utils.create_directory()`.
    - Delegates the actual saving of the data to `self.template_serializer.save_to_json()`.
    - Prints a confirmation message to the console.
  - **`import_template(self, file_path: str) -> tuple[TemplateInfo, TemplateParameters]`:**
    - Takes the `file_path` of a template JSON file.
    - Delegates the loading of raw JSON data to `self.template_serializer.load_from_json()`.
    - Delegates the deserialization of the loaded data into `TemplateInfo` and `TemplateParameters` objects to `self.template_serializer.deserialize_template_data()`.
    - Prints a confirmation message to the console.
    - Returns the deserialized `TemplateInfo` and `TemplateParameters` objects.
  - **`get_available_templates(self) -> list[str]`:**
    - Determines the directory where templates are stored.
    - Checks if the template directory exists.
    - Lists all files ending with `.json` in that directory.
    - Returns a list of filenames of available templates.

## 4. Key Classes and Functions

- **`class TemplateHandler`:**
  - Purpose: Manages the lifecycle of project templates (saving, loading, listing).
  - Methods:
    - `export_template(template_info: TemplateInfo, template_parameters: TemplateParameters, file_name: str) -> None`:
      - Saves template data to a JSON file.
    - `import_template(file_path: str) -> tuple[TemplateInfo, TemplateParameters]`:
      - Loads template data from a JSON file and deserializes it into `TemplateInfo` and `TemplateParameters` objects.
    - `get_available_templates() -> list[str]`:
      - Retrieves a list of all available template filenames.

## 5. Signals and Slots

This module is a core logic module and does not directly interact with PySide6 signals or slots. It focuses on data management and file operations.

## 6. Dependencies and Relationships

- **Internal Dependencies (from `src.core.template_manager`):**
  - `template_models.TemplateInfo`: The data model for template metadata.
  - `template_models.TemplateParameters`: The data model for the actual project parameters stored in a template.
  - `template_serializers.TemplateSerializer`: This module heavily relies on `TemplateSerializer` to perform the low-level tasks of reading from and writing to JSON files, and converting between raw data and Python objects.
- **Internal Dependencies (from `src.core.utils`):**
  - `path_utils.get_repository_root_dir`: Used to determine the base path for template storage.
  - `path_utils.create_directory`: Used to ensure the template storage directory exists.
- **External Dependencies:**
  - `os`: Standard Python library for operating system interactions, particularly path manipulation.
- **Relationship to UI/Application Logic:** The `TemplateHandler` would be used by the application's UI or other core logic components that need to save user-defined templates, load existing templates to pre-fill forms, or display a list of available templates.

## 7. Other Useful Information

- **Abstraction Layer:** This module provides a clean abstraction over the details of template storage and serialization, allowing other parts of the application to interact with templates using high-level methods.
- **Modularity:** By separating the handling logic from the serialization logic (`TemplateSerializer`) and data models (`TemplateInfo`, `TemplateParameters`), the system becomes more modular and easier to maintain.
- **Centralized Template Management:** All template-related file operations are routed through this handler, ensuring consistency in how templates are stored and accessed.
