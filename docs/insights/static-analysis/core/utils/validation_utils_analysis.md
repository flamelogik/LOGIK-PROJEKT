# Static Analysis: `src/core/utils/validation_utils.py`

## Overview
The `validation_utils.py` module provides utility functions for validating various input parameters used throughout the LOGIK-PROJEKT application. These functions ensure data integrity and provide feedback to the user or calling processes about the validity of inputs.

## Dependencies
- **Python Standard Library**: `re` (used in `validate_init_config`)

## Function: `validate_client_campaign_names(client_name: str, campaign_name: str) -> tuple[bool, str]`

### Purpose
To validate that the provided client name and campaign name are not empty or consist only of whitespace.

### Arguments
- `client_name` (str): The client name string to validate.
- `campaign_name` (str): The campaign name string to validate.

### Logic
- Checks if `client_name` (after stripping whitespace) is empty. If so, returns `(False, "Client Name cannot be empty.")`.
- Checks if `campaign_name` (after stripping whitespace) is empty. If so, returns `(False, "Campaign Name cannot be empty.")`.
- If both are non-empty, returns `(True, "")`.

### Returns
- `tuple[bool, str]`: A tuple where the first element is `True` if validation passes and `False` otherwise. The second element is an empty string on success, or an error message on failure.

## Function: `validate_init_config(init_config_name: str, resolution_w: str, resolution_h: str, frame_rate: str) -> tuple[bool, str]`

### Purpose
To validate that the provided `init_config_name` (a Flame initialization configuration filename) is consistent with the selected resolution and framerate. It extracts resolution and framerate information from the `init_config_name` and compares it with the provided values.

### Arguments
- `init_config_name` (str): The name of the Flame initialization configuration file (e.g., `"1920x1080@25000p.cfg"`).
- `resolution_w` (str): The width component of the selected resolution.
- `resolution_h` (str): The height component of the selected resolution.
- `frame_rate` (str): The selected frame rate string (e.g., `"25.000 fps"`).

### Logic
1.  **Initialize**: Sets `mismatch_found` to `False` and `warning_message_parts` to an empty list.
2.  **Validate Resolution**: 
    - Constructs `expected_resolution_string` (e.g., `"1920x1080"`).
    - Checks if `expected_resolution_string` is present in `init_config_name`. If not, sets `mismatch_found` to `True` and adds `"resolution"` to `warning_message_parts`.
3.  **Validate Framerate**: 
    - Extracts the numeric framerate part from `init_config_name` using a regular expression (e.g., `"25000"` from `@25000p.cfg`).
    - Extracts the numeric framerate part from `frame_rate` by removing `.` and `" fps"` (e.g., `"25000"` from `"25.000 fps"`).
    - Compares the extracted numeric framerates. If they don't match, sets `mismatch_found` to `True` and adds `"framerate"` to `warning_message_parts`.
4.  **Return Result**: 
    - If `mismatch_found` is `True`, constructs a warning message indicating which parts (resolution and/or framerate) do not match and asks the user if they want to continue. Returns `(False, message)`.
    - If no mismatch is found, returns `(True, "")`.

### Returns
- `tuple[bool, str]`: A tuple where the first element is `True` if validation passes and `False` otherwise. The second element is an empty string on success, or a warning message on mismatch.

## Function: `validate_logik_projekt_name(logik_projekt_name: str) -> tuple[bool, str]`

### Purpose
To validate that the provided `logik_projekt_name` is not empty or consists only of whitespace.

### Arguments
- `logik_projekt_name` (str): The LOGIK-PROJEKT name string to validate.

### Logic
- Checks if `logik_projekt_name` (after stripping whitespace) is empty. If so, returns `(False, "LOGIK Projekt Name cannot be empty.")`.
- If it is non-empty, returns `(True, "")`.

### Returns
- `tuple[bool, str]`: A tuple where the first element is `True` if validation passes and `False` otherwise. The second element is an empty string on success, or an error message on failure.

## Observations
- This module centralizes common validation logic, promoting code reusability and consistency in input checks.
- The `validate_init_config` function demonstrates complex string parsing and comparison using regular expressions to ensure data consistency between different input fields.
- The validation functions return a tuple of `(bool, str)`, which is a clear and effective way to communicate both the validation result and a descriptive message.
- The messages are user-friendly, guiding the user on what needs to be corrected or confirming a potential mismatch.