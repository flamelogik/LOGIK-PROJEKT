# Static Analysis: `src/core/utils/calculated_name_utils.py`

## Overview
The `calculated_name_utils.py` module provides utility functions for generating standardized and sanitized names, typically for projects or assets. It includes a function to sanitize individual parts of a name and a main function to combine these parts into a calculated name based on various configurable "recipes."

## Dependencies
- **Python Standard Library**: `re`, `datetime`

## Function: `_sanitize_part(part: str) -> str`

### Purpose
To clean up a single string part by replacing spaces and problematic characters with underscores and removing non-alphanumeric characters.

### Arguments
- `part` (str): The string part to be sanitized.

### Logic
1.  **Replace Spaces and Problematic Characters**: Uses `re.sub(r'[\s:]+', '_', part)` to replace one or more whitespace characters, slashes, or colons with a single underscore.
2.  **Remove Invalid Characters**: Uses `re.sub(r'[^a-zA-Z0-9_-]', '', part)` to remove any characters that are not alphanumeric, underscore, or hyphen.
3.  **Return**: Returns the sanitized string.

## Function: `get_calculated_name(serial: str, client: str, campaign: str) -> str`

### Purpose
To generate a standardized calculated name by combining and sanitizing input serial, client, and campaign strings. The function is designed to be easily configurable with different naming conventions ("recipes").

### Arguments
- `serial` (str): The serial number part of the name.
- `client` (str): The client name part of the name.
- `campaign` (str): The campaign name part of the name.

### Logic
1.  **Pre-Sanitization**: Calls `_sanitize_part()` on `serial`, `client`, and `campaign` to clean them individually, storing the results in `s_serial`, `s_client`, and `s_campaign`.
2.  **Naming Recipes**: The core of this function is a set of commented-out "recipes" for generating the `calculated_name`. Only one recipe should be active (uncommented) at a time. The default active recipe is:
    -   `calculated_name = f"{s_serial}_{s_client.lower()}_{s_campaign.lower()}"`: Combines sanitized serial, lowercase client, and lowercase campaign with underscores.
    -   Other commented-out recipes demonstrate variations like using uppercase, title case, omitting the serial, or incorporating the current date.
3.  **Final Sanitization**: 
    - `while "__" in calculated_name:`: Replaces any double underscores (which might result from empty input parts) with single underscores.
    - `calculated_name = calculated_name.strip('_')`: Removes any leading or trailing underscores.
4.  **Return**: Returns the final calculated and sanitized name.

### Observations
- This module is highly configurable, allowing users to easily switch between different naming conventions by uncommenting a single line of code.
- The use of regular expressions (`re` module) for sanitization is robust and efficient.
- The clear separation of sanitization logic (`_sanitize_part`) from the combination logic (`get_calculated_name`) promotes modularity.
- The detailed comments within `get_calculated_name` serve as excellent documentation for users who might want to customize the naming convention.
- The final sanitization steps ensure that the generated name is clean and well-formatted, regardless of the chosen recipe or input data.