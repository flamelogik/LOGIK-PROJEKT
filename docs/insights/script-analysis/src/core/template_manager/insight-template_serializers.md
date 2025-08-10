# Insight: `template_serializers.py`

## 1. Module Type

`template_serializers.py` is a Python module responsible for serializing and deserializing template data to and from JSON format.

## 2. Purpose

The primary purpose of this module is to handle the conversion between Python objects (`TemplateInfo` and `TemplateParameters` dataclasses) and a persistent JSON representation. This enables saving template configurations to files and loading them back into the application.

## 3. Behavior and Functionality

- **`TemplateSerializer` Class:**
  - All methods are static, meaning they can be called directly on the class without needing to instantiate an object.
  - **`save_to_json(template_info: TemplateInfo, template_parameters: TemplateParameters, file_path: str)`:**
    - Takes instances of `TemplateInfo` and `TemplateParameters` and a `file_path`.
    - Constructs a dictionary `data` by mapping attributes from both `template_info` and `template_parameters` to specific string keys (e.g., "Template Serial Number", "Template Resolution").
    - Writes this `data` dictionary to the specified `file_path` as a JSON file, with an indent of 4 for readability.
  - **`load_from_json(file_path: str) -> dict`:**
    - Takes a `file_path` to a JSON file.
    - Reads the content of the JSON file and returns it as a Python dictionary.
  - **`deserialize_template_data(data: dict) -> tuple[TemplateInfo, TemplateParameters]`:**
    - Takes a dictionary `data` (typically loaded from a JSON file).
    - Creates new instances of `TemplateInfo` and `TemplateParameters`.
    - Populates the attributes of these new instances by retrieving values from the input `data` dictionary using `.get()` with default empty strings, ensuring robustness against missing keys.
    - Returns a tuple containing the deserialized `TemplateInfo` and `TemplateParameters` objects.

## 4. Key Classes and Functions

- **`class TemplateSerializer`:**
  - Purpose: Provides static methods for converting `TemplateInfo` and `TemplateParameters` objects to/from JSON.
  - Methods:
    - `save_to_json(template_info: TemplateInfo, template_parameters: TemplateParameters, file_path: str) -> None`:
      - Serializes template data into a JSON file.
    - `load_from_json(file_path: str) -> dict`:
      - Loads raw JSON data from a file into a dictionary.
    - `deserialize_template_data(data: dict) -> tuple[TemplateInfo, TemplateParameters]`:
      - Deserializes a dictionary of template data into `TemplateInfo` and `TemplateParameters` objects.

## 5. Signals and Slots

This module is a pure utility module focused on data serialization and does not interact with PySide6 signals or slots.

## 6. Dependencies and Relationships

- **Standard Python Libraries:** `json` (for JSON encoding and decoding).
- **Internal Dependencies:**
  - `src.core.template_manager.template_models.TemplateInfo`: The data model for template metadata that this serializer handles.
  - `src.core.template_manager.template_models.TemplateParameters`: The data model for template parameters that this serializer handles.
- **Relationship to `template_handler.py`:** The `TemplateHandler` module utilizes the `TemplateSerializer` to perform the actual file I/O and object-to-data/data-to-object conversions. `TemplateSerializer` provides the low-level serialization mechanism that `TemplateHandler` orchestrates.
- **Data Persistence:** This module is crucial for the persistence of template configurations, allowing them to be saved and reloaded across application sessions.

## 7. Other Useful Information

- **Separation of Concerns:** By dedicating a module solely to serialization/deserialization, it keeps the `TemplateHandler` focused on managing templates and the `template_models` focused on data structure, leading to a cleaner and more maintainable codebase.
- **Robustness:** The use of `.get()` with default values during deserialization makes the process resilient to changes in the JSON structure (e.g., if new fields are added or old ones removed, the deserialization won't crash).
- **Readability of JSON:** The `indent=4` in `json.dump` ensures that the saved JSON files are human-readable, which is beneficial for debugging and manual inspection of template data.
