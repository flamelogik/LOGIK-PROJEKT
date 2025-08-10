# Insight: `calculated_name_utils.py`

## 1. Module Type

`calculated_name_utils.py` is a Python utility module. It provides functions for generating standardized names based on input components.

## 2. Purpose

The primary purpose of this module is to create consistent and sanitized project or asset names from user-provided serial numbers, client names, and campaign names. It offers various naming conventions ("recipes") that can be easily switched.

## 3. Behavior and Functionality

- **`_sanitize_part(part)`:**
  - A private helper function that sanitizes a single string part.
  - Replaces spaces and problematic characters (like `/` and `:`) with underscores.
  - Removes any characters that are not alphanumeric, underscore, or hyphen.
- **`get_calculated_name(serial, client, campaign)`:**
  - Takes `serial`, `client`, and `campaign` as input strings.
  - Sanitizes each part using `_sanitize_part`.
  - Provides multiple "recipes" for combining these sanitized parts into a final calculated name.
  - Recipes include variations in casing (lowercase, uppercase, title case) and order of components, as well as options to use the current date as a serial.
  - Ensures the final name does not contain double underscores and removes leading/trailing underscores.

## 4. Key Functions

- `_sanitize_part(part: str) -> str`:
  - Purpose: Cleans up a string part for use in a filename.
  - Arguments: `part` (the string to sanitize).
  - Returns: The sanitized string.
- `get_calculated_name(serial: str, client: str, campaign: str) -> str`:
  - Purpose: Generates a calculated name based on provided project details and a chosen naming convention.
  - Arguments: `serial` (serial number), `client` (client name), `campaign` (campaign name).
  - Returns: The final calculated and sanitized name string.

## 5. Signals and Slots

This module is a pure utility module and does not interact with PySide6. Therefore, it does not define or use any signals or slots.

## 6. Dependencies and Relationships

- **Standard Python Libraries:** `re` (for regular expressions), `datetime` (for date-based naming recipes).
- **Relationship to Project Creation Workflow:** This module is crucial for maintaining naming consistency across the LOGIK-PROJEKT application. It is likely used by modules responsible for creating new projects or assets, ensuring that generated directories and files adhere to predefined naming conventions. It provides the core logic for generating the `projekt_name` which is a fundamental identifier in the system.

## 7. Other Useful Information

- **Configurable Naming Conventions:** The "recipe" approach within `get_calculated_name` allows for easy customization of naming conventions without altering the core sanitization logic. This is a powerful feature for adapting to different client or project requirements.
- **Robustness:** The sanitization steps ensure that the generated names are filesystem-friendly and avoid issues with special characters.
- **Centralized Naming Logic:** By centralizing the naming logic, the module ensures consistency across the application and simplifies future modifications to naming conventions.
