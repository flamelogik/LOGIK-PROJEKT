# Insight: `get_resolution_values.py`

## 1. Module Type

`get_resolution_values.py` is a Python utility module. It provides a single function to retrieve a comprehensive list of resolution presets from multiple JSON configuration files, following a specified load order.

## 2. Purpose

The primary purpose of this module is to centralize and manage the available resolution options for the application. It allows for a flexible and extensible system where resolution presets can be defined in separate JSON files and loaded in a specific order, ensuring that UI components (like a `QComboBox`) are populated with accurate and up-to-date choices.

## 3. Behavior and Functionality

- **Load Order Driven:** The `get_resolution_values()` function first reads `resolution_load_order.json` (whose path is defined by `GetApplicationPaths.RESOLUTION_LOAD_ORDER_FILE`). This file dictates which individual resolution JSON files to load and in what sequence.
- **Modular JSON Loading:** It iterates through the filenames specified in the load order. For each filename, it constructs the full path (relative to `GetApplicationPaths.RESOLUTION_PATH`) and attempts to open and parse the JSON content.
- **Data Extraction:** It expects the resolution JSON files to have a nested structure, specifically looking for `"items"` within `"items"` to extract individual resolution dictionaries. Each resolution dictionary is expected to contain a `"resolution_name"` key.
- **Data Aggregation:** All successfully extracted resolution dictionaries are appended to a single list, which is then returned.
- **Robust Error Handling:** It includes `try-except` blocks to gracefully handle `FileNotFoundError` (for the load order file or individual resolution files), `json.JSONDecodeError` (if any JSON file is malformed), and general `Exception`s during file operations. In case of an error, it prints a message and returns an empty list.

## 4. Key Functions

- `get_resolution_values() -> list[dict]`:
  - Purpose: Retrieves a list of resolution preset dictionaries from configured JSON files.
  - Returns: A list of dictionaries, where each dictionary represents a resolution preset (e.g., `{"resolution_name": "1920x1080", "width": 1920, "height": 1080, ...}`), or an empty list if an error occurs.

## 5. Signals and Slots

This module is a pure utility module and does not interact with PySide6. Therefore, it does not define or use any signals or slots.

## 6. Dependencies and Relationships

- **Standard Python Libraries:** `json`, `os`.
- **`src.core.functions.get.get_application_paths`:** It relies on `GetApplicationPaths` to provide the standardized paths to the `RESOLUTION_PATH` (base directory for resolution JSONs) and `RESOLUTION_LOAD_ORDER_FILE`.
- **JSON Configuration Files:** It is critically dependent on the existence and correct formatting of `resolution_load_order.json` and the individual resolution JSON files it references.
- **`src.ui.panels.template_parameters_panel.py`:** This module is used by `TemplateParametersPanel` to populate the `ResolutionWidget`'s options. The `TemplateParametersPanel` calls `get_resolution_values()` and then passes the returned list to the `set_values()` method of its `ResolutionWidget` instance.

## 7. Other Useful Information

- **Modular Configuration:** This design allows for a highly modular and flexible way to manage resolution presets. New presets can be added by simply creating new JSON files and updating the `resolution_load_order.json`.
- **Prioritization:** The load order file enables prioritization, allowing certain resolution lists to override or supplement others, which is useful for managing different client or project requirements.
- **Data Integrity:** By providing predefined and validated resolution options, it reduces the chance of user input errors and ensures consistency in project settings.
- **Maintainability:** Changes to resolution options can be made by editing JSON files, without requiring code modifications or redeployment.