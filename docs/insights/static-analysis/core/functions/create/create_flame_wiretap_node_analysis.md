# Static Analysis: `src/core/functions/create/create_flame_wiretap_node.py`

## Overview
The `create_flame_wiretap_node.py` script defines a function to create a new Autodesk Flame project node using the `wiretap_create_node` command-line utility. It executes a bash command to interact with the Wiretap API, configuring the new project with a specified name and an XML configuration file.

## Dependencies
- **Python Standard Library**: `subprocess`, `logging`

## Function: `create_flame_wiretap_node(flame_projekt_name, projekt_xml_path)`

### Purpose
To programmatically create a Flame project node on the Wiretap server, enabling automated project setup within the Flame ecosystem.

### Arguments
- `flame_projekt_name` (str): The name of the Flame project to be created.
- `projekt_xml_path` (str): The absolute path to the XML configuration file that defines the project's settings.

### Logic
1.  **Construct Bash Command**: A multi-line bash command string is constructed using an f-string. This command calls `/opt/Autodesk/wiretap/tools/current/wiretap_create_node` with several arguments:
    - `-h 127.0.0.1:IFFFS`: Specifies the Wiretap server host and port.
    - `-n /projects`: Specifies the Wiretap namespace for projects.
    - `-t PROJECT`: Indicates that a project node is being created.
    - `-d "{flame_projekt_name}"`: Sets the display name of the new project.
    - `-s XML`: Specifies that the project configuration is provided via an XML file.
    - `-f "{projekt_xml_path}"`: Provides the path to the XML configuration file.
    - The `umask 0` command is included to ensure that the created project has broad read/write permissions.
2.  **Log Command**: The constructed bash command is logged for debugging and auditing purposes.
3.  **Execute Command**: `subprocess.Popen` is used to execute the `bash_command`.
    - `shell=True`: Allows the command to be executed through the shell.
    - `executable='/bin/bash'`: Explicitly specifies bash as the shell interpreter.
    - `stdout=subprocess.PIPE`, `stderr=subprocess.PIPE`: Captures the standard output and standard error streams of the command.
4.  **Communicate and Decode**: `process.communicate()` waits for the command to complete and retrieves its stdout and stderr. These are then decoded from bytes to UTF-8 strings.
5.  **Log Output**: If stdout or stderr contain any output, they are logged as informational or error messages, respectively.

### Error Handling
- The script captures `stdout` and `stderr` from the executed bash command and logs them, providing insight into any issues encountered by `wiretap_create_node`.
- Python-level exceptions during the `subprocess.Popen` call are not explicitly caught within this function, but would propagate up to the calling function.

## Observations
- This script is a critical component for automating the creation of Flame projects, directly interacting with Autodesk's Wiretap API.
- The use of `subprocess.Popen` is appropriate for executing external shell commands and capturing their output.
- The hardcoded path to `wiretap_create_node` (`/opt/Autodesk/wiretap/tools/current/wiretap_create_node`) makes the script dependent on a specific Autodesk installation path.
- The `umask 0` is important for ensuring proper permissions for the newly created Flame project, especially in multi-user environments.
- While `subprocess.Popen` is used, `subprocess.run` is generally preferred for simpler command execution as it handles `communicate()` automatically and provides a more direct way to check the exit code.
