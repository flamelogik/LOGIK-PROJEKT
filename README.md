# [LOGIK-PROJEKT](https://github.com/flamelogik/LOGIK-PROJEKT)


### Table of Contents
- Introduction
- System Requirements
  - Hardware Requirements
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

    # Check Static HostName (macOS HostName)
    hostnamectl status | grep "Static hostname"

    # Check Pretty HostName (macOS ComputerName)
    hostnamectl status | grep "Pretty hostname"

    # Check Transient HostName (macOS LocalHostName)
    hostnamectl status | grep "Transient hostname"

-------------------------------------------------------------------------------

    # Set the Static HostName (equivalent to macOS HostName)
    sudo hostnamectl set-hostname <new-static-hostname>

    # Set Pretty HostName (macOS ComputerName)
    sudo hostnamectl set-hostname "<new-pretty-hostname>" --pretty

    # Set the Transient HostName (equivalent to macOS LocalHostName)
    sudo hostnamectl set-hostname <new-transient-hostname> --transient
    
-------------------------------------------------------------------------------
    
    [Create a test directory for LOGIK-PROJEKTS:]
    sudo mkdir -p -m 777 /home/shared/PROJEKTS

-------------------------------------------------------------------------------

    [Link /PROJEKTS to test PROJEKTS directory:]
    sudo ln -s /home/shared/PROJEKTS /PROJEKTS

-------------------------------------------------------------------------------

    [Reboot workstation:]
    sudo reboot

-------------------------------------------------------------------------------

### Workstation Preparation (macOS):

    # Check HostName (Linux Static hostname)
    scutil --get HostName

    # Check LocalHostName (Linux Transient HostName)
    scutil --get LocalHostName

    # Check ComputerName (Linux Pretty HostName)
    scutil --get ComputerName

-------------------------------------------------------------------------------

    # Set the HostName (equivalent to Linux Static hostname)
    sudo scutil --set HostName <new-hostname>

    # Set LocalHostName (Linux Transient HostName)
    sudo scutil --set LocalHostName <new-local-hostname>

    # Set ComputerName (Linux Pretty HostName)
    sudo scutil --set ComputerName <new-computer-name>

-------------------------------------------------------------------------------

    [Create a test directory for LOGIK-PROJEKTS:]
    sudo mkdir -p -m 777 /Users/Shared/PROJEKTS

-------------------------------------------------------------------------------

    [Create /etc/synthetic.conf to link /PROJEKTS to test PROJEKTS directory:]
    sudo cat "PROJEKTS   Users/Shared/PROJEKTS" > /etc/synthetic.conf

-------------------------------------------------------------------------------

    [Reboot workstation:]
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

-------------------------------------------------------------------------------
