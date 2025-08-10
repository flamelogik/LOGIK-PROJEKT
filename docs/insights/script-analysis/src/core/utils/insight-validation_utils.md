# Insight: `validation_utils.py`

## 1. Module Type

`validation_utils.py` is a Python utility module. It provides functions for validating various input parameters within the application.

## 2. Purpose

The primary purpose of this module is to ensure the integrity and correctness of user inputs and selected configurations before they are processed by other parts of the application. It centralizes validation logic to provide consistent feedback to the user.

## 3. Behavior and Functionality

- **`validate_client_campaign_names(client_name, campaign_name)`:**
  - Checks if both `client_name` and `campaign_name` are non-empty after stripping whitespace.
  - Returns `(True, "")` if both are valid, otherwise `(False, "Error Message")` indicating which field is empty.
- **`validate_init_config(init_config_name, resolution_w, resolution_h, frame_rate)`:**
  - Validates if the `init_config_name` (e.g., a Flame initialization configuration file name) matches the provided `resolution_w`, `resolution_h`, and `frame_rate`.
  - Extracts resolution (e.g., "1920x1080") from `init_config_name` and compares it with the combined `resolution_w` and `resolution_h`.
  - Extracts the numeric framerate (e.g., "25000") from both `init_config_name` and `frame_rate` and compares them.
  - If mismatches are found for resolution or framerate, it returns `(False, "Warning Message")` suggesting a discrepancy and asking for confirmation to proceed.
  - Returns `(True, "")` if all parameters match or no mismatches are found.
- **`validate_logik_projekt_name(logik_projekt_name)`:**
  - Checks if `logik_projekt_name` is non-empty after stripping whitespace.
  - Returns `(True, "")` if valid, otherwise `(False, "Error Message")`.

## 4. Key Functions

- `validate_client_campaign_names(client_name: str, campaign_name: str) -> tuple[bool, str]`:
  - Purpose: Validates that client and campaign names are not empty.
  - Arguments: `client_name` (string), `campaign_name` (string).
  - Returns: A tuple `(is_valid: bool, message: str)`. `message` is empty if valid, otherwise contains an error.
- `validate_init_config(init_config_name: str, resolution_w: str, resolution_h: str, frame_rate: str) -> tuple[bool, str]`:
  - Purpose: Validates consistency between an initialization configuration name and selected resolution/framerate.
  - Arguments: `init_config_name` (string, e.g., "1920x1080@25000p.cfg"), `resolution_w` (string), `resolution_h` (string), `frame_rate` (string, e.g., "25.000 fps").
  - Returns: A tuple `(is_valid: bool, message: str)`. `message` is empty if valid, otherwise contains a warning.
- `validate_logik_projekt_name(logik_projekt_name: str) -> tuple[bool, str]`:
  - Purpose: Validates that the LOGIK-PROJEKT name is not empty.
  - Arguments: `logik_projekt_name` (string).
  - Returns: A tuple `(is_valid: bool, message: str)`. `message` is empty if valid, otherwise contains an error.

## 5. Signals and Slots

This module is a pure utility module and does not interact with PySide6. Therefore, it does not define or use any signals or slots.

## 6. Dependencies and Relationships

- **Standard Python Libraries:** `re` (for regular expressions in `validate_init_config`).
- **Relationship to UI/Input Forms:** Functions in this module are likely called directly by the UI layer or by application logic that processes user inputs from forms. They provide immediate feedback on the validity of the data.
- **Relationship to Configuration/Project Creation:** The validation of `init_config_name` is crucial for ensuring that the selected Flame project settings are consistent, preventing potential issues during project creation or setup.

## 7. Other Useful Information

- **User Feedback:** The validation functions return messages that can be directly presented to the user, guiding them to correct invalid inputs.
- **Separation of Concerns:** By isolating validation logic into a dedicated module, the code remains clean and maintainable. Other modules can rely on these functions to ensure data quality without implementing validation themselves.
- **Flexibility:** The `validate_init_config` function demonstrates how validation can be tailored to specific naming conventions and data formats, which is important for integrating with external systems like Autodesk Flame.
