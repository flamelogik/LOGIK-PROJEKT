___
# [LOGIK-PROJEKT](https://github.com/flamelogik/LOGIK-PROJEKT)
Projekt Creation, Workflow & LifeCycle Management for Autodesk Flame 2025.
___
LOGIK-PROJEKT was developed with Autodesk Flame 2025, Python 3.11, and PySide 6.
___
### Requirements:
* [Autodesk Flame 2025](https://help.autodesk.com/view/FLAME/2025/ENU/)
* /PROJEKTS - (root level symbolic link for PROJEKT storage)
___
### Useful Software:
* [Microsoft VisualStudio Code](https://code.visualstudio.com/Download)
* [GitHub Desktop](https://desktop.github.com/download/)
___
### Workstation Preparation Linux:

    # Check Static HostName (macOS HostName)
    hostnamectl status | grep "Static hostname"

    # Check Pretty HostName (macOS ComputerName)
    hostnamectl status | grep "Pretty hostname"

    # Check Transient HostName (macOS LocalHostName)
    hostnamectl status | grep "Transient hostname"
___
    # Set Static HostName (macOS HostName)
    sudo hostnamectl set-hostname <new-static-hostname>

    # Set Pretty HostName (macOS ComputerName)
    sudo hostnamectl set-hostname "<new-pretty-hostname>" --pretty

    # Set Transient HostName (macOS LocalHostName)
    sudo hostnamectl set-hostname <new-transient-hostname> --transient
___
    [Create a test PROJEKTS directory:]
    sudo mkdir -p -m 777 /home/shared/PROJEKTS
___
    [Link /PROJEKTS to test PROJEKTS directory:]
    sudo ln -s /home/shared/PROJEKTS /PROJEKTS
___
### Workstation Preparation macOS:

    # Check HostName (Linux Static hostname)
    scutil --get HostName

    # Check LocalHostName (Linux Transient HostName)
    scutil --get LocalHostName

    # Check ComputerName (Linux Pretty HostName)
    scutil --get ComputerName
___
    # Set HostName (Linux Static hostname)
    sudo scutil --set HostName <new-hostname>

    # Set LocalHostName (Linux Transient HostName)
    sudo scutil --set LocalHostName <new-local-hostname>

    # Set ComputerName (Linux Pretty HostName)
    sudo scutil --set ComputerName <new-computer-name>
___
    [Create a test PROJEKTS directory:]
    sudo mkdir -p -m 777 /Users/Shared/PROJEKTS
___
    [Create /etc/synthetic.conf to link /PROJEKTS to test PROJEKTS directory:]
    sudo cat "PROJEKTS   Users/Shared/PROJEKTS" > /etc/synthetic.conf
___
    [Reboot workstation:]
    sudo reboot
___
### Flame 2025 Installation:

* install DKU (Linux only)
* install flame 2025
* if necessary create a new stone called 'stonefs'

___
### Post Flame 2025 Installation:

#### (Linux)
* start flame 
* license the application
* create a test project

#### (macOS)
* start flame 
* license the application
* create a test project

Enable these applications in:
System Preferences / Privacy & Security / Full Disk Access /

* DLmpd
* Flame
* ifffsWiretapServer
* Python3.11
* swdb
* sw_dbd
* sw_serverd
* Terminal
* Visual StudioCode
* wiretapgateway 

___
### Configure Flame Preferences:

1. User Tokens tab
* set User Name
* set User Nickname
2. Timeline tab
* set Default Shot Name to:
* ```<name>_<background segment###>0```
3. Batch/BFX Tab
* set Default batch iteration name to
* ```<batch name>_v<iteration####>_<workstation>_<user nickname>```
4. Media Panel Tab
* set Batch shelf to 1
* set Reel Group to 2
* set Show Batch iterations (first column) 
* set Desktop Column: Set to “Copy From/To Batch”

___
### LOGIK-PROJEKT Installation:

Setting up the /PROJEKTS directory:
1. fork the repo from [GitHub](https://github.com/flamelogik/LOGIK-PROJEKT)
2. run ```install/get_current_adsk_python.sh```
3. run ```install/create_desktop_apps.sh```
4. on first run answer ’N’ to say you don’t have a projekt template
5. assign ‘test’ to client name
6. assign ‘test’ to campaign name
7. choose resolution
8. choose frame rate
9. choose bit depth
10. choose color science
11. press enter to launch flame or escape to cancel
12. if you press enter, flame will launch with the newly defined project (-J option)
13. it will create a workspace with the name of your workstation
14. it will create the library layout with the create_layout python script
15. save flame
16. quit flame
17. create the first archive:/PROJEKTS/test_test/flame/archives/test_test_2025_my_workstation.sh
18. create the first rsync backup:/PROJEKTS/test_test/backup_scripts/test_test_*.sh
19. you can exclude directories from the rsync by modifying the exclusion_list file
20. When you are RESTORING ARCHIVEs make sure you’re using the “Convert to Local” Path

___
#### DISCLAIMER:
    This file is part of LOGIK-PROJEKT.
    Copyright © 2024 man-made-mekanyzms

    LOGIK-PROJEKT creates directories, files, scripts & tools
    for use with Autodesk Flame and other software.
    LOGIK-PROJEKT is free software.
    You can redistribute it and/or modify it under the terms
    of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License,
    or any later version.
    This program is distributed in the hope that it will be
    useful, but WITHOUT ANY WARRANTY; without even the
    implied warranty of MERCHANTABILITY or FITNESS FOR A
    PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General
    Public License along with this program.
    If not, see <https://www.gnu.org/licenses/>.

    Contact: phil_man@mac.com
___