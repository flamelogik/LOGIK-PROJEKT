# Static Analysis: `src/core/utils/data_transformers.py`

## Overview
The `data_transformers.py` script provides utility functions for transforming data strings into a more usable format. Specifically, it includes functions for extracting a simplified code from a cache string and parsing a resolution string into its width, height, and pixel aspect ratio components.

## Dependencies
- **Python Standard Library**: `re` (for regular expressions)

## Functions

#### `get_cache_code(cache_string: str) -> str`
- **Purpose**: Extracts a simplified code or ID from a given cache string.
- **Signature**: `def get_cache_code(cache_string: str) -> str:`
- **Logic**:
    1.  Converts the `cache_string` to lowercase.
    2.  Replaces spaces and colons with underscores (`re.sub(r'[\s:]+', '_', cache_string)`).
    3.  Removes any characters that are not alphanumeric, underscore, hyphen, or period (`re.sub(r'[^a-zA-Z0-9_.-]', '', part)`).
    4.  Returns the resulting sanitized string.
- **Observations**:
    -   The docstring notes that this is a placeholder and would need actual parsing logic, implying that the current implementation is a basic sanitization rather than a complex parsing.
    -   It's useful for converting human-readable cache descriptions into machine-friendly identifiers.

#### `parse_resolution_string(resolution_string: str) -> tuple[int, int, float]`
- **Purpose**: Parses a resolution string (e.g., "1920x1080 | 1.0") into its width, height, and pixel aspect ratio components.
- **Signature**: `def parse_resolution_string(resolution_string: str) -> tuple[int, int, float]:`
- **Logic**:
    1.  **Input Validation**: Checks if `resolution_string` is empty. If so, prints a message and returns `None, None, None`.
    2.  **Split by '|'**: Splits the `resolution_string` by `'|'` to separate the resolution part from the ratio part.
    3.  **Extract Resolution**: Splits the resolution part by `'x'` or `'X'` to get width and height.
    4.  **Extract Pixel Aspect Ratio**: If a ratio part exists, it's converted to a float; otherwise, it defaults to `1.0`.
    5.  **Return**: Returns `width`, `height`, and `pixel_aspect_ratio`.
    6.  **Error Handling**: Uses a `try-except` block to catch `ValueError` (e.g., if `int()` or `float()` conversion fails) or `IndexError` (if parts are missing). Prints an error message and returns `None, None, None`.
- **Observations**:
    -   This function is critical for extracting numerical resolution data from a formatted string, which is common in UI inputs or configuration files.
    -   The function includes `print` statements for debugging, which should ideally be replaced with a proper logging mechanism in a production environment.
    -   The return of `None, None, None` on failure requires callers to handle these `None` values gracefully.
