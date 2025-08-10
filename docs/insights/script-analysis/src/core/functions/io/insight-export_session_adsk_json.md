# Insight: `export_session_adsk_json.py`

## 1. Module Type

`export_session_adsk_json.py` is a Python utility script designed for exporting project data in a JSON format specifically tailored for Autodesk applications.

## 2. Purpose

The primary purpose of this module is to generate a `current_session-adsk.json` file containing a subset of the LOGIK-PROJEKT's current session data. This JSON file is formatted in a way that Autodesk applications (like Flame) can readily consume, facilitating integration and automated project setup within the Autodesk ecosystem.

## 3. Behavior and Functionality

- **`export_session_adsk_json(projekt_summary_data)`:**
  - Takes a dictionary `projekt_summary_data` as input, which contains comprehensive project configuration details.
  - Defines the output directory as `pref/session-preferences` and the output filename as `current_session-adsk.json`.
  - Ensures the output directory exists using `os.makedirs(output_dir, exist_ok=True)`.
  - Defines two helper functions, `to_int` and `to_float`, to safely convert input values to integer and float types, respectively, logging warnings for conversion failures.
  - Constructs an `adsk_data` dictionary by extracting and mapping relevant values from `projekt_summary_data` to specific keys expected by Autodesk applications (e.g., "Name", "ProjectDir", "Resolution", "FrameRate"). It uses the `to_int` and `to_float` helpers for numerical fields.
  - Writes the `adsk_data` dictionary to the specified JSON file with an indent of 4 for readability.
  - Logs an info message upon successful export or an error message if the export fails.

## 4. Key Functions

- `export_session_adsk_json(projekt_summary_data: dict) -> None`:
  - Purpose: Exports a subset of project data into a JSON file formatted for Autodesk software consumption.
  - Arguments: `projekt_summary_data` (a dictionary containing all project configuration data).
  - Returns: None.

## 5. Signals and Slots

This module is a pure utility function and does not interact with PySide6 signals or slots.

## 6. Dependencies and Relationships

- **Standard Python Libraries:** `json` (for JSON serialization), `os` (for file system operations), `logging` (for logging messages).
- **Relationship to Project Creation Workflow:** This function is a critical step in the overall project creation process orchestrated by `projekt_creator.py`. It prepares the necessary configuration data that Autodesk applications will use to understand and load the newly created project.
- **Relationship to Autodesk Applications:** The module's output (`current_session-adsk.json`) is specifically designed for direct consumption by Autodesk software, highlighting its role in integrating LOGIK-PROJEKT with the Autodesk ecosystem.

## 7. Other Useful Information

- **Interoperability:** This module is key to the interoperability between LOGIK-PROJEKT and Autodesk applications, enabling seamless data exchange.
- **Data Transformation:** It performs a data transformation, taking a general project summary and converting it into a specialized format required by external software.
- **Robustness:** The inclusion of `to_int` and `to_float` helper functions with error handling makes the data conversion process more robust, preventing crashes due to unexpected input types.
