# Insight: `template_models.py`

## 1. Module Type

`template_models.py` is a Python module that defines data models for project templates.

## 2. Purpose

The primary purpose of this module is to provide structured and type-hinted containers for information related to project templates within the LOGIK-PROJEKT application. It separates template metadata (`TemplateInfo`) from the actual project parameters (`TemplateParameters`) that a template defines.

## 3. Behavior and Functionality

- **`TemplateInfo` Dataclass:**
  - This dataclass is used to store metadata about a template.
  - Fields include:
    - `template_serial_number`: A unique identifier for the template.
    - `template_client_name`: The client name associated with the template.
    - `template_campaign_name`: The campaign name associated with the template.
    - `template_calculated_name`: A generated, sanitized name for the template.
    - `template_description`: A brief description of the template's purpose or characteristics.
  - All fields are initialized with default empty string values.

- **`TemplateParameters` Dataclass:**
  - This dataclass is used to store the actual project configuration parameters that a template represents.
  - Fields include various settings relevant to Autodesk Flame projects, such as:
    - Resolution details (`template_resolution`, `template_resolution_w`, `template_resolution_h`, `template_aspect_ratio`).
    - Technical specifications (`template_bit_depth`, `template_framerate`, `template_scan_mode`, `template_start_frame`).
    - Configuration references (`template_init_config`, `template_ocio_config`, `template_ocio_name`, `template_ocio_path`).
    - Cache settings (`template_cache_integer`, `template_cache_integer_id`, `template_cache_float`, `template_cache_float_id`).
  - All fields are initialized with default empty string values.

## 4. Key Classes

- **`class TemplateInfo`:**
  - Purpose: Defines the structure for storing descriptive information about a project template.
  - Attributes: `template_serial_number`, `template_client_name`, `template_campaign_name`, `template_calculated_name`, `template_description`.
- **`class TemplateParameters`:**
  - Purpose: Defines the structure for storing the specific technical parameters and settings that a project template configures.
  - Attributes: A comprehensive list of attributes covering resolution, frame rate, bit depth, OCIO settings, and cache formats.

## 5. Signals and Slots

This module defines data structures and does not interact with PySide6 signals or slots. It is purely a data model.

## 6. Dependencies and Relationships

- **Standard Python Libraries:** `dataclasses` (specifically `dataclass` and `field`), `typing` (specifically `Optional`).
- **Relationship to `template_handler.py`:** Instances of `TemplateInfo` and `TemplateParameters` are created, saved, and loaded by the `TemplateHandler` module. The `TemplateHandler` acts as the orchestrator for managing these data models.
- **Relationship to `template_serializers.py`:** The `TemplateSerializer` module is responsible for converting instances of `TemplateInfo` and `TemplateParameters` into a serializable format (e.g., JSON) and vice-versa.
- **Relationship to UI/Data Collection:** These dataclasses serve as the target for data collected from user input forms when creating or modifying templates, and as the source for populating UI elements when loading existing templates.

## 7. Other Useful Information

- **Clear Separation of Concerns:** By having separate dataclasses for `TemplateInfo` (metadata) and `TemplateParameters` (actual settings), the module promotes a clear separation of concerns, making the data model more organized and easier to understand.
- **Type Safety:** The use of dataclasses with type hints improves code readability and allows for better static analysis, ensuring that data is handled consistently throughout the application.
- **Extensibility:** The dataclass structure makes it easy to add new parameters to templates in the future without significantly refactoring existing code.
