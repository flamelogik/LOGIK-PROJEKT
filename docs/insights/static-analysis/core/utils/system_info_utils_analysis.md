# Static Analysis: `src/core/utils/system_info_utils.py`

## Overview
The `system_info_utils.py` module provides a comprehensive set of utility functions for gathering detailed information about the current system, including user details, network configurations, operating system specifics, and group memberships. It is designed to collect various pieces of system data for reporting or internal application use.

## Dependencies
- **Python Standard Library**: `os`, `platform`, `socket`, `grp`, `pwd`, `subprocess`, `sys`
- **Typing**: `List`, `Dict`, `Any`

## Independent Functions

#### `get_current_user() -> Dict[str, Any]`
- **Purpose**: Retrieves detailed information about the current user.
- **Arguments**: None.
- **Logic**: Attempts to get username using `os.getlogin()` or environment variables. Uses `os.getuid()`, `os.getgid()`, `os.geteuid()`, `os.getegid()` for IDs. Uses `pwd.getpwuid()` to get real name, home directory, and shell.
- **Returns**: A dictionary containing user information (username, UIDs, GIDs, real name, home directory, shell). Includes an 'error' key if an exception occurs.
- **Error Handling**: Catches general `Exception` during information retrieval.

#### `get_fqdn() -> str`
- **Purpose**: Retrieves the Fully Qualified Domain Name (FQDN) of the host.
- **Arguments**: None.
- **Logic**: Uses `socket.getfqdn()`.
- **Returns**: The FQDN string or an error message if retrieval fails.
- **Error Handling**: Catches general `Exception`.

#### `get_hostnames() -> Dict[str, Any]`
- **Purpose**: Retrieves various hostname information, including hostname, FQDN, and aliases.
- **Arguments**: None.
- **Logic**: Uses `socket.gethostname()`, `socket.getfqdn()`, and `socket.gethostbyname_ex()`.
- **Returns**: A dictionary containing hostname, FQDN, and a list of aliases. Includes an 'error' key if an exception occurs.
- **Error Handling**: Catches general `Exception`.

#### `get_ipv4_addresses() -> List[str]`
- **Purpose**: Retrieves all IPv4 addresses associated with the host.
- **Arguments**: None.
- **Logic**: 
    - Gets local IP using `socket.gethostbyname(socket.gethostname())`.
    - Attempts to get an external IP by connecting to a public DNS server (8.8.8.8).
    - Attempts to use `netifaces` library to get all interface IPs. If `netifaces` is not available, falls back to `hostname -I` command on Linux.
- **Returns**: A list of IPv4 address strings. Includes an error message string if an exception occurs.
- **Error Handling**: Uses multiple `try-except` blocks for different methods of IP retrieval.

#### `get_os_info() -> Dict[str, Any]`
- **Purpose**: Retrieves detailed operating system information.
- **Arguments**: None.
- **Logic**: Uses `platform` module functions for general OS details. Includes platform-specific logic for Linux (using `distro` or `/etc/os-release`, `/etc/issue`, `uname -a`), Windows (`win32_edition`, `win32_ver`), and macOS (`mac_ver`).
- **Returns**: A dictionary containing various OS attributes.
- **Error Handling**: Uses `try-except` blocks for various platform-specific calls, returning partial data if some information cannot be retrieved.

#### `get_group_memberships() -> Dict[str, Any]`
- **Purpose**: Retrieves the current user's group memberships.
- **Arguments**: None.
- **Logic**: Uses `os.getgid()`, `grp.getgrgid()` for primary group. Uses `pwd.getpwuid()` and `grp.getgrall()` to list all groups the user belongs to. Includes an alternative method using `os.getgroups()`.
- **Returns**: A dictionary containing primary group info, a sorted list of all group memberships, and group count. Includes an 'error' key if an exception occurs.
- **Error Handling**: Catches general `Exception`.

## Dependent Functions (Level 1)

#### `get_primary_group() -> str`
- **Purpose**: Returns the current user's primary group name.
- **Arguments**: None.
- **Logic**: Calls `get_group_memberships()` and extracts the primary group name from the returned dictionary.
- **Returns**: The primary group name string or `"(unknown_group - could not retrieve primary group)"` if not found.

#### `get_short_hostname() -> str`
- **Purpose**: Returns the short hostname of the machine.
- **Arguments**: None.
- **Logic**: Calls `get_hostnames()` and extracts the hostname, then splits it by `.` to get the short name.
- **Returns**: The short hostname string.

#### `get_os_name() -> str`
- **Purpose**: Returns the operating system name.
- **Arguments**: None.
- **Logic**: Calls `get_os_info()` and extracts the system name.
- **Returns**: The OS name string or `'unknown'`.

## Dependent Functions (Level 2)

#### `print_system_info()`
- **Purpose**: Prints all collected system information in a formatted, human-readable way to standard output.
- **Arguments**: None.
- **Logic**: Calls various `get_*` functions (`get_hostnames`, `get_fqdn`, `get_ipv4_addresses`, `get_os_info`, `get_current_user`, `get_group_memberships`) and prints their results under categorized headers.
- **Returns**: None.

## Main Execution Block

#### `main()`
- **Purpose**: The main function to execute the system information gathering and printing process.
- **Arguments**: None.
- **Logic**: Calls `print_system_info()`.
- **Error Handling**: Catches `KeyboardInterrupt` for graceful exit and general `Exception` for other errors, printing messages and exiting the script.

## Observations
- This module provides a comprehensive suite of functions for system introspection, covering a wide range of operating system and network details.
- The functions are modular, with lower-level functions gathering raw data and higher-level functions processing and presenting it.
- Extensive use of Python's standard library modules (`os`, `platform`, `socket`, `grp`, `pwd`, `subprocess`) demonstrates reliance on built-in capabilities.
- The inclusion of platform-specific logic (Linux, Windows, macOS) makes the module adaptable to different environments.
- The `print_system_info` function serves as a good example of how to aggregate and display the collected data.
- The `main` execution block allows the script to be run directly for system information reporting.
