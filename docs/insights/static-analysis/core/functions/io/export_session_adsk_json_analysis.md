# Static Analysis: `src/core/functions/io/export_session_adsk_json.py`

## Overview
The `export_session_adsk_json.py` script defines a function to export a subset of project data into a JSON file, specifically formatted for consumption by Autodesk applications. This file, named `current_session-adsk.json`, is stored in the `pref/session-preferences` directory.

## Dependencies
- **Python Standard Library**: `json`, `os`, `logging`

## Function: `export_session_adsk_json(projekt_summary_data: dict)`

### Purpose
To generate a JSON file containing key project parameters and settings in a structure that can be easily read and utilized by Autodesk software, facilitating integration and automated project setup.

### Arguments
- `projekt_summary_data` (dict): A dictionary containing comprehensive project summary data, from which relevant information for Autodesk applications will be extracted.

### Logic
1.  **Define Output Paths**: Sets the `output_dir` to `"pref/session-preferences"` and `output_filename` to `"current_session-adsk.json"`. It then constructs the full `output_path`.
2.  **Ensure Directory**: Ensures the `output_dir` exists, creating it if necessary (`os.makedirs(..., exist_ok=True)`).
3.  **Helper Functions**: Defines two nested helper functions:
    -   `to_int(value)`: Attempts to convert a value to an integer. Logs a warning if conversion fails and returns the original value.
    -   `to_float(value)`: Attempts to convert a value to a float. Logs a warning if conversion fails and returns the original value.
4.  **Construct `adsk_data` Dictionary**: Creates a dictionary named `adsk_data` by extracting specific keys from `projekt_summary_data` and mapping them to Autodesk-friendly keys (e.g., `"Name"`, `"ProjectDir"`, `"Resolution"`). It uses the `to_int` and `to_float` helper functions for type conversion where appropriate.
5.  **Write JSON to File**: 
    - Opens the `output_path` in write mode (`'w'`).
    - Uses `json.dump()` to write the `adsk_data` to the file with an indent of 4 for readability.
    - Logs an informational message upon successful export.

### Error Handling
- Catches general `Exception` during the file writing process. If an error occurs, it logs an error message including the exception details.
- The `to_int` and `to_float` helper functions include basic error handling for type conversion, logging warnings if conversion is not possible.

## Observations
- This script is essential for enabling interoperability between the LOGIK-PROJEKT application and Autodesk software by providing a standardized data exchange format.
- The explicit mapping of keys from `projekt_summary_data` to `adsk_data` ensures that only relevant information is exported and that it conforms to the expected structure for Autodesk applications.
- The use of helper functions for type conversion (`to_int`, `to_float`) makes the data mapping more robust and handles potential inconsistencies in input data types.
- The `json.dump` with `indent=4` ensures the output JSON is human-readable, which is beneficial for debugging and manual inspection.
