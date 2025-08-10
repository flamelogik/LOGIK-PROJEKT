# Insight: `projekt_models.py`

## 1. Module Type

`projekt_models.py` is a Python module that defines the data model for Autodesk Flame project configurations.

## 2. Purpose

The primary purpose of this module is to provide a structured and type-hinted way to encapsulate all the parameters required for creating, managing, and interacting with an Autodesk Flame project within the LOGIK-PROJEKT application. It acts as a central data container for project-related information.

## 3. Behavior and Functionality

- **`ProjektParameters` Dataclass:**
  - This dataclass is decorated with `@dataclass`, which automatically generates methods like `__init__`, `__repr__`, `__eq__`, etc., based on the defined fields.
  - It defines numerous fields, each representing a specific piece of information related to a Flame project or the LOGIK-PROJEKT environment.
  - Fields are categorized for clarity:
    - **Environment Data:** `current_user`, `current_group`, `current_workstation`, `current_os`.
    - **Flame Software Data:** `flame_software_choice`, `flame_software_name`, `flame_software_version`, `flame_software_sanitized_name`, `flame_software_sanitized_version`.
    - **Flame Projekt Data:** A comprehensive set of parameters defining the Flame project itself, including its name, nickname, description, various directory paths (`home`, `setups_dir`, `media_dir`, `catalog_dir`), resolution (`width`, `height`, `ratio`), frame rate (`rate`), color management (`ocio`, `ocio_path`, `ocio_name`), and cache formats (`cachef`, `cachef_id`, `cachei`, `cachei_id`).
    - **LOGIK PROJEKT Data:** `logik_projekt_name`, `logik_projekt_path`, `logik_projekt_config_name`, `logik_projekt_config_tree`, `logik_projekt_config_bookmarks`, `logik_projekt_config_workspace`.
    - **Workflow Options:** `launch_flame_after_creation` (a boolean flag).
  - All fields are initialized with default empty string values (or `False` for boolean) to ensure that an instance can be created without providing all parameters, and to provide a clear default state.

## 4. Key Classes

- **`class ProjektParameters`:**
  - Purpose: A dataclass serving as the central data model for all parameters related to an Autodesk Flame project within the LOGIK-PROJEKT system.
  - Attributes: A comprehensive list of attributes covering environment, Flame software, Flame project specifics, LOGIK-PROJEKT details, and workflow options.

## 5. Signals and Slots

This module defines a data structure and does not interact with PySide6 signals or slots. It is purely a data model.

## 6. Dependencies and Relationships

- **Standard Python Libraries:** `dataclasses` (specifically `dataclass` and `field`), `typing` (specifically `Optional`).
- **Relationship to `projekt_creator.py`:** The `ProjektParameters` dataclass is the primary input for the `ProjektCreator` class (and its `create_projekt` method). The `projekt_creator.py` module relies heavily on this data structure to access all the necessary information for building a Flame project.
- **Relationship to UI/Data Collection:** This dataclass is likely populated by data collected from the user interface (e.g., input forms) or from configuration files. It provides a clear contract for what data is expected and how it should be structured.
- **Relationship to Data Persistence:** Instances of `ProjektParameters` could potentially be serialized to and deserialized from JSON or other formats for saving and loading project configurations.

## 7. Other Useful Information

- **Data Integrity and Type Hinting:** Using a dataclass with type hints (`str`, `bool`) improves code readability, maintainability, and allows for static analysis tools to catch potential type-related errors early.
- **Centralized Data Definition:** By defining all project parameters in one place, this module ensures consistency across the application regarding how project data is structured and accessed.
- **Readability:** Dataclasses provide a concise way to define classes that primarily serve as data containers, making the code cleaner compared to traditional `__init__` methods with many parameters.
