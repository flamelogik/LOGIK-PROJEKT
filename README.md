# [LOGIK-PROJEKT](https://github.com/flamelogik/LOGIK-PROJEKT)

### Table of Contents
- Introduction
- Key Features
- System Requirements
  - Hardware Requirements
  - Recommended Operating Systems
  - Software Requirements
  - Useful Software
- Preparation
  - Workstation Preparation (Linux)
  - Workstation Preparation (macOS)
- Installation And Configuration
  - Flame 2025 Installation
  - Post Flame 2025 Installation
  - Configure Flame Preferences
  - LOGIK-PROJEKT Installation
  - Running LOGIK-PROJEKT
  - Troubleshooting Permissions and Python
  - Application Tree
  - Disclaimer

-------------------------------------------------------------------------------

## Introduction

LOGIK-PROJEKT is a toolkit designed for the creation, business continuity and lifecycle management of Digital Content Creation (DCC) projekts.

LOGIK-PROJEKT automates and standardizes projekt setup, allowing stakeholders to focus on creative tasks, not technical impediments.

LOGIK-PROJEKT has been developed with a strong emphasis on artist empowerment, primarily focused on Autodesk Flame.

Uniquely, LOGIK-PROJEKT users can freely collaborate using bespoke, shared or inherited directory structures.

The LOGIK-PROJEKT application is a GUI that streamlines the decision-making process for users, enabling them to generate a site-configurable "LOGIK-PROJEKT" that includes:

- Organized, configurable filesystem directories.
- An optional Autodesk Flame Projekt with its own dedicated directories.
- Flame Projekt bookmarks that link filesystem and Flame Projekt folders.
- A customizable suite of presets, scripts, templates and utilities.


-------------------------------------------------------------------------------

## Key Features

- **Portal Root Directory**: Simple implementation and strategy for Business Continuity and redundancy purposes.
- **Automated Projekt Setup**: Create new projekts with predefined settings & structures.
- **Customizable Parameters**: User-configurable projekt parameters and values.
- **Template Management**: Export and Import projekt templates for collaborative environments.
- **Flame Integration**: Seamlessly integrates with Autodesk Flame.
- **Intuitive GUI**: User-friendly interfaceguides users through the projekt creation process.
- **Robust Logging**: Comprehensive logging for tracking application behavior and troubleshooting.

-------------------------------------------------------------------------------

## System Requirements

### Hardware Requirements

- Linux or macOS workstation, capable of running `Autodesk Flame 2026+`

### Recommended Operating Systems

- [`Autodesk Rocky Linux 9.5`](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/CentOS-ISO-installer-and-Linux-Driver-Kernel-Utilities-for-Flame-Family.html?msockid=172861bfea6e668204c6745eeb806704)
- [`Apple® macOS® Sonoma 15+`](https://support.apple.com/mac)

### Software Requirements

- [`Autodesk Flame 2026`](https://help.autodesk.com/view/FLAME/2026/ENU/)
- `/PROJEKTS` - (root level mount point for PROJEKT storage)

### Useful Software:

- [`Microsoft VisualStudio Code`](https://code.visualstudio.com/Download)
- [`GitHub Desktop`](https://desktop.github.com/download/)

-------------------------------------------------------------------------------

## Preparation

### Workstation Preparation (Linux)

-------------------------------------------------------------------------------

- **`Get HostName (Linux)`**

    ```bash
    # Get Static HostName (equivalent to macOS HostName)
    hostnamectl status | grep "Static hostname"

    # Get Transient HostName (equivalent to macOS LocalHostName)
    hostnamectl status | grep "Transient hostname"

    # Get Pretty HostName (equivalent to macOS ComputerName)
    hostnamectl status | grep "Pretty hostname"
    ```

-------------------------------------------------------------------------------

- **`Set HostName (Linux)`**

    ```bash
    # Set the Static HostName (equivalent to macOS HostName)
    sudo hostnamectl set-hostname "new-static-hostname"

    # Set the Transient HostName (equivalent to macOS LocalHostName)

    sudo hostnamectl set-hostname "new-transient-hostname" --transient

    # Set Pretty HostName (equivalent to macOS ComputerName)

    sudo hostnamectl set-hostname "new-pretty-hostname" --pretty
    ```

-------------------------------------------------------------------------------

- **`Create a test directory for LOGIK-PROJEKTS`**

    ```bash
    # Create a test directory for LOGIK-PROJEKTS:
    sudo mkdir -p -m 777 /home/shared/PROJEKTS
    ```

-------------------------------------------------------------------------------

- **`Link test PROJEKTS directory to /PROJEKTS (Linux)`**

    ```bash
    # Link test PROJEKTS directory to /PROJEKTS:
    sudo ln -s /home/shared/PROJEKTS /PROJEKTS
    ```

-------------------------------------------------------------------------------

- **`Reboot workstation`**

    ```bash
    # Reboot workstation: (optional)
    sudo reboot
    ```

-------------------------------------------------------------------------------

- **`Unlink /PROJEKTS before linking to alternative PROJEKTS directory`**

    ```bash
    # Unlink /PROJEKTS before linking to alternative PROJEKTS directory:
    sudo unlink /PROJEKTS
    ```

-------------------------------------------------------------------------------

- **`Link /PROJEKTS to alternative PROJEKTS directory: (examples)`**

    ```bash
    # Link /PROJEKTS to alternative PROJEKTS directory: (examples)
    sudo ln -s /mnt/NAS_FAST/PROJEKTS /PROJEKTS
    sudo ln -s /mnt/NAS_SLOW/PROJEKTS /PROJEKTS
    sudo ln -s /Volumes/My_Lucid_Link_Drive/PROJEKTS /PROJEKTS
    sudo ln -s /Volumes/Client_Lucid_Link_Drive/PROJEKTS /PROJEKTS
    ```

-------------------------------------------------------------------------------

### Workstation Preparation (macOS):

-------------------------------------------------------------------------------

- **`Get HostName (macOS)`**

    ```bash
    # Check HostName (equivalent to Linux Static hostname)
    scutil --get HostName

    # Check LocalHostName (equivalent to Linux Transient HostName)
    scutil --get LocalHostName

    # Check ComputerName (equivalent to Linux Pretty HostName)
    scutil --get ComputerName
    ```

-------------------------------------------------------------------------------

- **`Set HostName (macOS)`**

    ```bash
    # Set the HostName (equivalent to Linux Static hostname)
    sudo scutil --set HostName <new-hostname>

    # Set LocalHostName (equivalent to Linux Transient HostName)
    sudo scutil --set LocalHostName <new-local-hostname>

    # Set ComputerName (equivalent to Linux Pretty HostName)
    sudo scutil --set ComputerName <new-computer-name>
    ```

-------------------------------------------------------------------------------

- **`Create a test directory for LOGIK-PROJEKTS`**

    ```bash
    # Create a test directory for LOGIK-PROJEKTS:
    sudo mkdir -p -m 777 /home/shared/PROJEKTS
    ```

-------------------------------------------------------------------------------

- **`Link test PROJEKTS directory to /PROJEKTS (macOS)`**

    ```bash
    # Create /etc/synthetic.conf to link /PROJEKTS to test PROJEKTS directory:
    echo "PROJEKTS	System/Volumes/Data/Users/Shared/PROJEKTS" | sudo tee /etc/synthetic.conf

    # (The whitespace between PROJEKTS and the path MUST BE A TAB, NOT WHITESPACE)
    ```

-------------------------------------------------------------------------------

- **`Modify ownership and permissions (macOS 26)`**

    ```bash
    # It may be necessary to change ownership and permissions under macOS 26:

    # Change ownership of /etc/synthetic.conf:
    sudo chown root:wheel /etc/synthetic.conf

    # Change permissions of /etc/synthetic.conf:
    sudo chmod 644 /etc/synthetic.conf

    # (The whitespace between PROJEKTS and the path MUST BE A TAB, NOT WHITESPACE)
    ```

-------------------------------------------------------------------------------

- **`Reboot workstation`**

    ```bash
    # Reboot workstation: (required)
    sudo reboot
    ```

-------------------------------------------------------------------------------

## Installation And Configuration

-------------------------------------------------------------------------------

### Flame Installation:

-------------------------------------------------------------------------------

- **`Install Flame (Linux)`**

    ```bash
    # install recommended operating system
    # install DKU
    # install flame
    ```

-------------------------------------------------------------------------------

- **`Install Flame (macOS)`**

    ```bash
    # install recommended operating system
    # install flame
    ```

-------------------------------------------------------------------------------

### Post Flame Installation:

- **`Post Flame Installation (Linux)`**

    ```bash
    # start flame
    # license the application
    # create a test projekt
    ```

-------------------------------------------------------------------------------

- **`Post Flame Installation (macOS)`**

    ```bash
    # start flame
    # license the application
    # create a test projekt

    # You may need to enable these applications in:
    # System Preferences | Privacy & Security | Full Disk Access

        # DLmpd
        # Flame
        # ifffsWiretapServer
        # Python3.11
        # swdb
        # sw_dbd
        # sw_serverd
        # Terminal
        # Visual StudioCode
        # wiretapgateway
    ```

-------------------------------------------------------------------------------

### Configure Flame Preferences

- **`Configure Flame Preferences`**

    ```bash
    User Tokens tab
        ├── set User Name
        └── set User Nickname

    Timeline tab
        ├── set Default Shot Name to:
        └── <name>_<background segment###>0

    Batch/BFX Tab
        ├── set Default batch iteration name to
        └── <batch name>_v<iteration####>_<workstation>_<user nickname>

    Media Panel Tab
        ├── set Batch shelf to 1
        ├── set Reel Group to 2
        ├── set Show Batch iterations (first column)
        └── set Desktop Column: Set to “Copy From/To Batch”
    ```

-------------------------------------------------------------------------------

### LOGIK-PROJEKT Installation

- **`LOGIK-PROJEKT Installation`**

    ```bash
    # Download or fork the release version of the LOGIK-PROJEKT repository
    # from: https://github.com/flamelogik/LOGIK-PROJEKT
    # to:   /path/to/your/home/workspace/GitHub/

    # Make a directory in your home directory
    mkdir -p -m 775 ~/workspace/GitHub/

    # Change directory to your new directory
    cd ~/workspace/GitHub/

    # Git Clone the LOGIK-PROJEKT repository
    git clone git@github.com:flamelogik/LOGIK-PROJEKT.git

    # Change to the LOGIK-PROJEKT directory
    cd ~/workspace/GitHub/LOGIK-PROJEKT

    # Establish the path to the current Autodesk Flame Python installation
    install/get_current_adsk_python.sh

    # Create Desktop Applications for LOGIK-PROJEKT
    install/create_desktop_apps.sh
    ```

-------------------------------------------------------------------------------

## Running LOGIK-PROJEKT

- **`Linux`**: Look for `LOGIK-PROJEKT` in your Activities menu or double-click the desktop launcher.
- **`macOS`**: Locate `LOGIK-PROJEKT.app` in the projekt folder and double-click it.

-------------------------------------------------------------------------------

## Application Structure

The core application logic and UI components are organized within the `src/` directory:

```bash
src/
├── app.py                                            # Main application entry point and orchestrator
├── core/                                             # Contains the core business logic and data models
│   ├── app_logic.py                                  # Facade for core application logic, interacts with UI
│   ├── functions/                                    # Collection of utility functions grouped by purpose
│   │   ├── copy/                                     # Functions for copying files and configurations
│   │   │   ├── copy_current_session_files.py
│   │   │   ├── copy_flame_bookmarks.py
│   │   │   ├── copy_flame_presets.py
│   │   │   └── copy_flame_python_scripts.py
│   │   ├── create/                                   # Functions for creating various projekt-related assets
│   │   │   ├── create_flame_archive_script.py
│   │   │   ├── create_flame_launcher_script.py
│   │   │   ├── create_flame_setup_dirs.py
│   │   │   ├── create_flame_startup_script.py
│   │   │   ├── create_flame_symbolic_links.py
│   │   │   ├── create_flame_wiretap_node.py
│   │   │   ├── create_projekt_backup_script.py
│   │   │   ├── create_projekt_filesystem_dirs.py
│   │   │   ├── create_projekt_launcher_alias.py
│   │   │   └── create_projekt_pgsql_db.py
│   │   ├── get/                                      # Functions for retrieving data and configurations
│   │   │   ├── get_application_paths.py
│   │   │   ├── get_bit_depth_values.py
│   │   │   ├── get_cache_float_values.py
│   │   │   ├── get_cache_integers_values.py
│   │   │   ├── get_default_template_values.py
│   │   │   ├── get_flame_bookmarks_path.py
│   │   │   ├── get_flame_software_versions.py
│   │   │   ├── get_frame_rate_values.py
│   │   │   ├── get_init_config_values.py
│   │   │   ├── get_json_data.py
│   │   │   ├── get_logik_projekt_config_values.py
│   │   │   ├── get_ocio_config_values.py
│   │   │   ├── get_projekt_summary_data.py
│   │   │   ├── get_resolution_values.py
│   │   │   ├── get_scan_mode_values.py
│   │   │   ├── get_start_frame_values.py
│   │   │   ├── get_sysconfig_flame_catalog_dir.py
│   │   │   ├── get_sysconfig_flame_home_dir.py
│   │   │   ├── get_sysconfig_flame_media_dir.py
│   │   │   └── get_sysconfig_flame_setups_dir.py
│   │   └── io/                                       # Functions for input/output operations
│   │       ├── export_logik_projekt_template.py
│   │       ├── export_session_adsk_json.py
│   │       ├── export_session_variables.py
│   │       ├── export_session_xml.py
│   │       └── import_logik_projekt_template.py
│   ├── projekt_manager/                              # Modules related to projekt creation and management
│   │   ├── projekt_creator.py                        # Handles the actual creation of projekts and file structures
│   │   └── projekt_models.py                         # Data models for projekt parameters
│   ├── template_manager/                             # Modules for handling projekt templates
│   │   ├── template_handler.py                       # Manages template import/export logic
│   │   ├── template_models.py                        # Data models for template information and parameters
│   │   └── template_serializers.py                   # Handles serialization/deserialization of templates
│   ├── unused/                                       # Contains modules that are currently not in use
│   │   ├── config_utils.py
│   │   ├── logik_projekt_dark_theme.py
│   │   ├── script_utils.py
│   │   └── string_utils.py
│   └── utils/                                        # General utility functions used across the core logic
│       ├── backup_utils.py
│       ├── calculated_name_utils.py
│       ├── flame_software_utils.py                   # Utilities for interacting with Flame software
│       ├── logik_projekt_utils.py
│       ├── ocio_utils.py                             # Utilities for OpenColorIO (OCIO) configurations
│       ├── path_utils.py                             # Path manipulation utilities
│       ├── system_info_utils.py                      # System information retrieval utilities
│       ├── threaded_logging_utils.py                 # Utilities for thread-safe logging
│       └── validation_utils.py                       # Utilities for data validation
├── ui/                                               # Contains all User Interface related components
│   ├── app_window.py                                 # Defines the main app window layout and panel integration
│   ├── panels/                                       # Individual UI panels that make up the main window
│   │   ├── flame_options_panel.py                    # Panel for Flame-specific settings
│   │   ├── projekt_summary_panel.py                  # Panel displaying a summary of the projekt to be created
│   │   ├── projekt_template_panel.py                 # Panel for importing existing projekt templates
│   │   ├── template_info_panel.py                    # Panel for basic template information input
│   │   ├── template_parameters_panel.py              # Panel for technical template parameters input
│   │   └── template_summary_panel.py                 # Panel displaying a summary of the template being built
│   ├── themes/                                       # UI themes and styling
│   │   ├── logik_projekt_spectrum_color.py           # Color definitions for the theme
│   │   └── modular_dark_theme.py                     # Defines the application's dark theme
│   ├── ui_config.py                                  # Centralized UI config constants (dimensions, margins, etc.)
│   └── widgets/                                      # Reusable UI widgets (buttons, comboboxes, entry fields)
│       ├── button/                                   # Custom button widgets
│       │   ├── create_projekt_widget.py
│       │   ├── export_template_widget.py
│       │   ├── flame_catalog_dir_widget.py
│       │   ├── flame_home_dir_widget.py
│       │   ├── flame_media_dir_widget.py
│       │   ├── flame_setups_dir_widget.py
│       │   └── import_template_widget.py
│       ├── combobox/                                 # Custom combobox widgets
│       │   ├── bit_depth_widget.py
│       │   ├── cache_float_widget.py
│       │   ├── cache_integer_widget.py
│       │   ├── flame_software_choice_widget.py
│       │   ├── frame_rate_widget.py
│       │   ├── init_config_widget.py
│       │   ├── ocio_config_widget.py
│       │   ├── projekt_config_widget.py
│       │   ├── resolution_widget.py
│       │   ├── scan_mode_widget.py
│       │   └── start_frame_widget.py
│       ├── display/                                  # Widgets for displaying information (read-only)
│       │   ├── projekt_summary_widget.py
│       │   ├── projekt_template_widget.py
│       │   └── template_summary_widget.py
│       └── entry/                                    # Custom text entry widgets
│           ├── aspect_ratio_widget.py
│           ├── calculated_name_widget.py
│           ├── campaign_name_widget.py
│           ├── client_name_widget.py
│           ├── description_widget.py
│           ├── resolution_height_widget.py
│           ├── resolution_width_widget.py
│           └── serial_number_widget.py
└── utils/                                            # General utilities not directly tied to core logic or UI
    └── common/                                       # Common utility functions
        └── create/                                   # Functions for customizing structures
            ├── create_banners.py
            ├── create_customized_filesystem_template.py
            ├── create_logs.py
            ├── create_separators.py
            ├── create_timestamp.py
            ├── directory_structure_analysis.py
            ├── directory_structure_to_bookmarks.py
            ├── directory_structure_to_json.py
```
