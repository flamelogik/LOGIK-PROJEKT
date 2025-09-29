# LOGIK-PROJEKT: Custom Configuration Guide

<a id="toc"></a>
## Table of Contents
- [Purpose of the Script](#purpose-of-the-script)
- [Where to put your custom directory structure](#where-to-put-your-custom-directory-structure)
- [How to Run the Script](#how-to-run-the-script)
  - [Running Directly with System Python](#running-directly-with-system-python)
  - [Running with Autodesk Python (Recommended)](#running-with-autodesk-python-recommended)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Key Concepts](#key-concepts)
- [Sharing Custom Templates](#sharing-custom-templates)
  - [For the Template Creator](#for-the-template-creator)
  - [For the Collaborator](#for-the-collaborator)
- [Troubleshooting](#troubleshooting)

This guide explains how to use the [`run_custom_template_creator.py`](./run_custom_template_creator.py) script to generate custom projekt configurations for LOGIK-PROJEKT. This script allows you to define a new projekt structure based on an existing directory tree, and then integrate it into the LOGIK-PROJEKTS's template system.

## Purpose of the Script

The [`run_custom_template_creator.py`](./run_custom_template_creator.py) script is a wrapper for the [`create_customized_filesystem_template.py`](../src/utils/common/create/create_customized_filesystem_template.py) script, which automates the process of:
1.  Analyzing a user-provided directory structure.
2.  Generating a JSON representation of this directory structure.
3.  Creating corresponding Autodesk Flame bookmarks based on the structure.
4.  Updating the application's site preferences to include this new custom template, making it available for use within the LOGIK-PROJEKT application.

[back to top](#toc)

## Where to put your custom directory structure

```bash
cfg/site-cfg/logik-projekt-cfg/logik-projekt-templates/filesystem-templates/custom-filesystem-templates
```

[back to top](#toc)

## How to Run the Script

### Running Directly with System Python

You can run this script directly from your terminal. Navigate to the root directory of your LOGIK-PROJEKT repository and execute the script:

```bash
python3 src/utils/common/create/create_customized_filesystem_template.py
```
Or you can select the script in Visual Studio Code and 'Run' the python script.

### Running with Autodesk Python (Recommended)

To ensure the script runs with the specific Autodesk Python interpreter configured for your Flame environment, use the provided wrapper script:

```bash
python3 docs/help/run_custom_template_creator.py
```

This wrapper script will automatically locate the Autodesk Python executable specified in `install/current_adsk_python_version.pref` and use it to run the `create_customized_filesystem_template.py` script. This is the recommended method to avoid potential compatibility issues with different Python versions.

[back to top](#toc)

## Inputs

Upon execution, the script will prompt you to select a directory:

*   **Choose a project directory template**: A GUI file dialog will appear (if PySide6 is installed and available). Use this to navigate to and select the root directory of your desired custom filesystem template. This is the directory whose structure you want to convert into a LOGIK-PROJEKT template.
*   **Command Line Fallback**: If PySide6 is not available or the GUI dialog fails, the script will fall back to a command-line prompt, asking you to enter the full path to your project directory template.

[back to top](#toc)

## Outputs

The script generates several files and updates the application's site preferences:

1.  **Filesystem Tree JSON File**:
    *   **Location**: `pref/site-prefs/custom-prefs/<your_template_name>/filesystem-tree.json`
    *   **Content**: A JSON file representing the hierarchical structure of the directory you selected. This file defines the folders and subfolders that will be created when a new project is generated using this template.

2.  **Flame Bookmarks JSON File**:
    *   **Location**: `pref/site-prefs/custom-prefs/<your_template_name>/cf_bookmarks.json`
    *   **Content**: A JSON file containing Autodesk Flame-compatible bookmarks. These bookmarks link directly to the folders defined in your custom filesystem template, allowing for quick navigation within Flame.

3.  **Flame Workspace JSON File**:
    *   **Location**: `pref/site-prefs/custom-prefs/<your_template_name>/flame-workspace.json`
    *   **Content**: A copy of the default Flame workspace template, placed within your custom template's directory. This ensures that each custom template can have its own associated Flame workspace configuration.

4.  **Site Preferences Update**:
    *   **File Updated**: `pref/site-prefs/logik-projekt-site-prefs.json`
    *   **Content**: The script automatically adds an entry for your new custom template under the `"PROJEKT Configurations"` section. This entry includes the `PROJEKT Configuration Name` (derived from your chosen directory's name), and the paths to the generated `filesystem-tree.json`, `flame-workspace.json`, and `cf_bookmarks.json` files. This makes your new template discoverable and usable within the LOGIK-PROJEKT application's UI.

[back to top](#toc)

## Key Concepts

*   **Directory Structure Template**: A pre-defined folder hierarchy that you wish to use as a blueprint for new LOGIK-PROJEKT projects.
*   **Flame Bookmarks**: Shortcuts within Autodesk Flame that allow quick access to specific directories.
*   **Site Preferences**: A central configuration file (`logik-projekt-site-prefs.json`) that stores global settings and registered project templates for the LOGIK-PROJEKT application.

[back to top](#toc)

## Sharing Custom Templates

You can easily share your custom templates with collaborators. The key is to share the original source directory structure, not the generated configuration files.

### For the Template Creator

1.  **Locate Your Source Template**: Navigate to the directory where you store your custom filesystem templates. The recommended location is:
    ```
    cfg/site-cfg/logik-projekt-cfg/logik-projekt-templates/filesystem-templates/custom-filesystem-templates/
    ```
2.  **Zip Your Template**: Inside this directory, you will find the folder you originally used to create your template (e.g., `my-awesome-template`). Create a zip archive of this folder.
3.  **Send the Zip File**: Email or share this zip file with your collaborators.

### For the Collaborator

1.  **Receive the Zip File**: Get the template zip file from your collaborator.
2.  **Unzip the Template**: Unzip the archive into the same location within your own LOGIK-PROJEKT repository:
    ```
    cfg/site-cfg/logik-projekt-cfg/logik-projekt-templates/filesystem-templates/custom-filesystem-templates/
    ```
    After unzipping, you should have a new folder (e.g., `my-awesome-template`) in this directory.
3.  **Run the Script**: Now, you need to run the template creator script to analyze the new template and register it with your local LOGIK-PROJEKT application. Follow the instructions in the [How to Run the Script](#how-to-run-the-script) section above.
4.  **Select the New Template**: When the script prompts you to "Choose a project directory template", select the folder you just unzipped.
5.  **Complete the Process**: The script will generate the necessary configuration files and update your `logik-projekt-site-prefs.json`. Your collaborator's custom template will now be available for you to use in the LOGIK-PROJEKT application.

[back to top](#toc)

## Troubleshooting

*   **"PySide6 not available" Warning**: If you see this warning, the GUI file dialog will not appear. You will need to manually enter the path to your template directory in the terminal. Ensure PySide6 is installed correctly if you prefer the GUI.
*   **"No folder selected" or "Invalid folder selected" Error**: Ensure you provide a valid, existing directory path when prompted.
*   **"Error creating backup directories" or "Error backing up files"**: Check your file permissions for the `pref/site-prefs/custom-prefs/` directory and its subdirectories. The script needs write access to create and backup files there.
*   **"Custom modules not available" Warning**: This indicates that some internal dependencies of the script are missing. Ensure your Python environment is correctly set up and all required `src/` modules are accessible.

[back to top](#toc)