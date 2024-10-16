# [LOGIK-PROJEKT](https://github.com/flamelogik/LOGIK-PROJEKT)


### Table of Contents
- Introduction
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

# Introduction

LOGIK-PROJEKT is a toolset for the creation & lifecycle management of projekts
for Autodesk Flame 2025 and newer.

The tools were developed with Autodesk Flame 2025+, Python 3.11, & PySide 6.

-------------------------------------------------------------------------------

## System Requirements

-------------------------------------------------------------------------------

### Hardware Requirements
* Linux or macOS workstation, capable of running Autodesk Flame 2025+

### Recommended Operating Systems
* [Rocky Linux 9.3](https://efulfillment.autodesk.com/pub1/os/Rocky-9.3-x86_64-dvd-ADSK_REV001.iso?authparam=1838129638_fa5cc47ff425e619342caacbb9b8181d&ext=.iso)
* [Apple® macOS® Sonoma 14+](https://support.apple.com/mac)

### Software Requirements
* [Autodesk Flame 2025](https://help.autodesk.com/view/FLAME/2025/ENU/)
* /PROJEKTS - (root level symbolic link for PROJEKT storage)

### Useful Software:
* [Microsoft VisualStudio Code](https://code.visualstudio.com/Download)
* [GitHub Desktop](https://desktop.github.com/download/)

-------------------------------------------------------------------------------

## Preparation

-------------------------------------------------------------------------------

### Workstation Preparation (Linux):

    # Check Static HostName (equivalent to macOS HostName)
    hostnamectl status | grep "Static hostname"

    # Check Transient HostName (equivalent to macOS LocalHostName)
    hostnamectl status | grep "Transient hostname"

    # Check Pretty HostName (equivalent to macOS ComputerName)
    hostnamectl status | grep "Pretty hostname"

-------------------------------------------------------------------------------

    # Set the Static HostName (equivalent to macOS HostName)
    sudo hostnamectl set-hostname <new-static-hostname>

    # Set the Transient HostName (equivalent to macOS LocalHostName)
    sudo hostnamectl set-hostname <new-transient-hostname> --transient

    # Set Pretty HostName (equivalent to macOS ComputerName)
    sudo hostnamectl set-hostname "<new-pretty-hostname>" --pretty

-------------------------------------------------------------------------------
    
    # Create a test directory for LOGIK-PROJEKTS:
    sudo mkdir -p -m 777 /home/shared/PROJEKTS

-------------------------------------------------------------------------------

    # Link /PROJEKTS to test PROJEKTS directory:
    sudo ln -s /home/shared/PROJEKTS /PROJEKTS

-------------------------------------------------------------------------------

    # Reboot workstation:
    sudo reboot

-------------------------------------------------------------------------------

### Workstation Preparation (macOS):

    # Check HostName (equivalent to Linux Static hostname)
    scutil --get HostName

    # Check LocalHostName (equivalent to Linux Transient HostName)
    scutil --get LocalHostName

    # Check ComputerName (equivalent to Linux Pretty HostName)
    scutil --get ComputerName

-------------------------------------------------------------------------------

    # Set the HostName (equivalent to Linux Static hostname)
    sudo scutil --set HostName <new-hostname>

    # Set LocalHostName (equivalent to Linux Transient HostName)
    sudo scutil --set LocalHostName <new-local-hostname>

    # Set ComputerName (equivalent to Linux Pretty HostName)
    sudo scutil --set ComputerName <new-computer-name>

-------------------------------------------------------------------------------

    # Create a test directory for LOGIK-PROJEKTS:
    sudo mkdir -p -m 777 /Users/Shared/PROJEKTS

-------------------------------------------------------------------------------

    # Create /etc/synthetic.conf to link /PROJEKTS to test PROJEKTS directory:
    echo "PROJEKTS	System/Volumes/Data/Users/Shared/PROJEKTS" | sudo tee /etc/synthetic.conf

-------------------------------------------------------------------------------

    # Reboot workstation:
    sudo reboot

-------------------------------------------------------------------------------

## Installation And Configuration

-------------------------------------------------------------------------------

### Flame 2025 Installation:

    # (Linux)

    # upgrade operating system
    # install DKU
    # install flame 2025
    # create a stone called 'stonefs'

-------------------------------------------------------------------------------

    # (macOS)

    # upgrade operating system
    # install flame 2025
    # create a stone called 'stonefs'

-------------------------------------------------------------------------------

### Post Flame 2025 Installation:

    # (Linux)

    # start flame 
    # license the application
    # create a test project

-------------------------------------------------------------------------------

    # (macOS)

    # start flame 
    # license the application
    # create a test project

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

-------------------------------------------------------------------------------

### Configure Flame Preferences:

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

-------------------------------------------------------------------------------

### LOGIK-PROJEKT Installation:

    # Download or fork the release version of the LOGIK-PROJEKT repository
    # from: https://github.com/flamelogik/LOGIK-PROJEKT
    # to:   /path/to/your/home/workspace/GitHub/

    mkdir -p -m 775 ~/workspace/GitHub/
    cd ~/workspace/GitHub/
    git clone git@github.com:flamelogik/LOGIK-PROJEKT.git

    # Change to the LOGIK-PROJEKT directory
    cd ~/workspace/GitHub/LOGIK-PROJEKT

    # Establish the path to the current Autodesk Flame Python installation
    install/get_current_adsk_python.sh

    # Create Desktop Applications for LOGIK-PROJEKT
    install/create_desktop_apps.sh

-------------------------------------------------------------------------------

### Running LOGIK-PROJEKT:

    # On Linux, look in the Activities menu for LOGIK-PROJEKT.
    # Add the desktop launcher to your favorites.
    # Double click the desktop launcher to run LOGIK-PROJEKT.

    # On macOS, look in the LOGIK-PROJEKT folder for the LOGIK-PROJEKT.app.
    # Add the LOGIK-PROJEKT.app to your dock.
    # Double click the LOGIK-PROJEKT.app to run LOGIK-PROJEKT.

-------------------------------------------------------------------------------

### Troubleshooting Permissions and Python:

    # There may be permission errors on your PROJEKTS directory.
    # Check that the permissions on your PROJEKTS directory are 777.

    # Errors have been seen on Rocky Linux 8.7 and macOS 13 related to python:
    # On Rocky Linux 8.7 errors have been seen related to python3.6.
    # On macOS 13 errors have been seen related to python3.9.

    # Possible Solutions:

    1. Install the Desired Python Version:
    - First, ensure you have the desired Python version installed.
    - For example, to install Python 3.11:
        ```bash
        sudo dnf install python3.11
        ```

    2. Configure Alternatives:
    - Add the new Python version to the alternatives system:
        ```bash
        sudo alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
        sudo alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2
        ```

    3. Select the Default Python Version:
    - Use the `alternatives` command to choose the default Python version:
        ```bash
        sudo alternatives --config python3
        ```
        You will see a list of installed Python versions.
        Select the number corresponding to Python 3.11.

    4. Verify the Change:
    - Check the Python version to ensure the switch was successful:
        ```bash
        python3 --version
        ```

-------------------------------------------------------------------------------

### Application Tree

    LOGIK-PROJEKT/
    │
    ├── docs/                                      # Documentation
    │                                              
    ├── install/                                   # Installation scripts
    │   │                                          
    │   └── logs/                                  # Installation logs
    │                                              
    ├── modules/                                   # Python modules
    │   │                                          
    │   ├── functions/                             # Python Functions
    │   │   │                                      
    │   │   ├── backup/                            # Backup functions
    │   │   ├── create/                            # Create functions
    │   │   ├── export/                            # Export functions
    │   │   ├── get/                               # Get functions
    │   │   ├── link/                              # Link functions
    │   │   ├── run/                               # Run functions
    │   │   ├── scratch/                           # Scratch functions
    │   │   ├── shell/                             # Shell functions
    │   │   ├── string/                            # String functions
    │   │   ├── synchronize/                       # Synchronize functions
    │   │   ├── update/                            # Update functions
    │   │   └── wiretap/                           # Wiretap functions
    │   │                                          
    │   ├── version/                               # Scripts Version
    │   |                                          
    │   └── widgets/                               # Widgets
    │       │                                      
    │       ├── combo_box/                         # Combo box widgets
    │       ├── layout/                            # Layout widgets
    │       ├── line_edit/                         # Line edit widgets
    │       └── style_sheet/                       # Style sheet widgets
    │                                              
    └── resources/                                 # Resources
        │                                          
        ├── cfg/                                   # Configuration files
        │   │                                      
        │   ├── nuke/                              # Foundry Nuke configuration
        │   │                                      
        │   └── projekt_configuration/             # Projekt configuration
        │       │                                  
        │       ├── bookmarks/                     # Bookmarks
        │       ├── parameters/                    # Parameters
        │       ├── roots/                         # Roots
        │       └── tree/                          # Tree
        │                                          
        ├── docstrings/                            # Docstrings
        │                                          
        ├── flame/                                 # Flame Resources
        │   │                                      
        │   ├── opencolorio/                       # OpenColorIO
        │   |   │                                  
        │   │   └── ocio_scripts/                  # OCIO scripts
        │   │                                      
        │   ├── presets/                           # Flame Presets
        │   │   |                                  
        │   │   ├── batch/                         # Batch presets
        │   │   ├── bookmarks/                     # Bookmark presets
        │   │   ├── burn_metadata/                 # Burn metadata presets
        │   │   ├── cfg/                           # Configuration presets
        │   │   ├── export/                        # Export presets
        │   │   ├── import/                        # Import presets
        │   │   ├── mediahub/                      # Mediahub presets
        │   │   ├── media_import/                  # Media import presets
        │   │   ├── mediaImport/                   # MediaImport presets
        │   │   ├── overlays/                      # Overlays presets
        │   │   └── status/                        # Status presets
        │   │                                      
        │   ├── python/                            # Flame Python
        │   │   |                                  
        │   │   └── logik_projekt/                 # Logik Projekt Python
        │   │       │                              
        │   │       ├── openclip_tools/            # OpenClip tools
        │   │       │                              
        │   │       └── projekt_tools/             # Projekt tools
        │   │                                      
        │   ├── Syncolor/                          # Syncolor Presets
        │   │   |                                  
        │   │   └── Shared/                        # Shared presets
        │   │       |                              
        │   │       ├── policies/                  # Syncolor policies
        │   │       |                              
        │   │       └── transforms/                # Syncolor transforms
        │   │           |                          
        │   │           └── flame_colortoolkit/    # Flame ColorToolkit
        │   │                                      
        │   └── templates/                         # Flame Templates
        │                                          
        ├── icons/                                 # Application icons
        │                                          
        ├── tmp/                                   # Temporary files
        │                                          
        ├── utilities/                             # Application utilities
        │   │                                      
        │   └── flame_configs/                     # Flame configurations
        │       |                                  
        │       └── init_config/                   # Init configuration
        │                                          
        ├── version/                               # Application version
        │                                          
        └── www/                                   # HTML files

-------------------------------------------------------------------------------

### Disclaimer:

    This file is part of LOGIK-PROJEKT.
    Copyright © 2024 man-made-mekanyzms

    LOGIK-PROJEKT creates directories, files, scripts & tools for use with 
    Autodesk Flame and other software.

    LOGIK-PROJEKT is free software.

    You can redistribute it and/or modify it under the terms of the 
    GNU General Public License as published by the Free Software Foundation,
    either version 3 of the License, or any later version.

    This program is distributed in the hope that it will be useful, 
    but 
    WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
    or FITNESS FOR A PARTICULAR PURPOSE.

    See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program.

    If not, see <https://www.gnu.org/licenses/>.

    Contact: phil_man@mac.com
