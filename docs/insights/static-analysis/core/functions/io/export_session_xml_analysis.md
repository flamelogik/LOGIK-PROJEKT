# Static Analysis: `src/core/functions/io/export_session_xml.py`

## Overview
The `export_session_xml.py` script defines a function to process an XML template, replacing placeholders within its elements with provided data, and then exports the modified XML to a specified output file. This is typically used for generating configuration files for other applications, such as Autodesk Wiretap.

## Dependencies
- **Python Standard Library**: `xml.etree.ElementTree` (imported as `ET`), `os`, `logging`
- **Local Modules (src.core.functions.get)**:
    - `src.core.functions.get.get_application_paths.GetApplicationPaths`: Used to get the path to the Wiretap XML template.

## Function: `export_session_xml(data: dict, template_path: str, output_path: str)`

### Purpose
To dynamically generate an XML file by populating a template with specific data, enabling the creation of customized configuration files for external systems.

### Arguments
- `data` (dict): A dictionary containing key-value pairs where keys correspond to placeholders in the XML template's element text, and values are the data to be inserted.
- `template_path` (str): The absolute path to the XML template file.
- `output_path` (str): The absolute path where the processed XML file will be saved.

### Logic
1.  **Parse Template**: Attempts to parse the XML template file specified by `template_path` using `ET.parse()`.
2.  **Get Root Element**: Retrieves the root element of the parsed XML tree.
3.  **Recursive Placeholder Replacement (`replace_placeholders` inner function)**:
    - This is a recursive function that traverses the XML element tree.
    - For each `child` element, it checks if its `text` attribute exists and, after stripping whitespace, if it matches a key in the `data_dict`.
    - If a match is found, the `child.text` is replaced with the corresponding `str(value)` from `data_dict`.
    - The function then recursively calls itself for each `child` element to process nested elements.
4.  **Apply Replacement**: Calls `replace_placeholders(root, data)` to start the replacement process from the root of the XML tree.
5.  **Ensure Output Directory**: Creates the parent directories for the `output_path` if they don't exist (`os.makedirs(os.path.dirname(output_path), exist_ok=True)`).
6.  **Write Output XML**: Writes the modified XML tree to the `output_path` with UTF-8 encoding and an XML declaration (`tree.write(output_path, encoding="utf-8", xml_declaration=True)`).
7.  **Log Success**: Logs an informational message indicating successful XML generation and saving.

### Error Handling
- Catches `FileNotFoundError`: If the `template_path` (which is `GetApplicationPaths.WIRETAP_XML_TEMPLATE`) does not exist. Logs an error.
- Catches general `Exception`: Catches any other unexpected errors during XML processing (e.g., parsing errors, file writing issues). Logs an error.

## Observations
- This function provides a flexible way to generate dynamic XML configurations, which is particularly useful for integrating with systems that rely on XML for settings (like Autodesk Wiretap).
- The recursive `replace_placeholders` function is an elegant solution for handling nested XML structures.
- The use of `xml.etree.ElementTree` is a standard Python library for XML parsing and generation.
- The function ensures the output directory exists before writing, preventing common file system errors.
- The hardcoded `template_path` within the function call to `ET.parse` means that the `template_path` argument passed to `export_session_xml` is effectively ignored for the template source, which might be a bug or an intentional design choice for this specific utility.