#!/usr/bin/env python3

'''
File Name:        function_04-setup.py
Version:          2.1.5
Language:         Python script
Flame Version:    2025.x
Author:           Phil MAN - phil_man@mac.com
Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
Modified:         2024-05-18
Modifier:         Phil MAN - phil_man@mac.com

Description:      This program contains function(s) that are used to
                  create new logik projekts.

Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
                  e.g. '/home/$USER/workspace/GitHub'

Changelist:       The full changelist is at the end of this document.
'''

import os
import datetime
import logging
import shutil
import subprocess
import sys

from PySide6.QtWidgets import (
    QApplication, 
    QFileDialog, 
    QMessageBox,
)

# ========================================================================== #
# This section configures logging.
# ========================================================================== #

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("function_04-setup.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ========================================================================== #
# This section defines global variables.
# ========================================================================== #

projekt_log_dir = ""
projekt_creation_log_file = ""
projekt_setup_file = ""
projekt_setup_template = ""
has_projekt_setup_template = ""

# ========================================================================== #
# This section defines variables based on the date.
# ========================================================================== #

# Year Options
YYYY = datetime.datetime.now().strftime("%Y")

# Month Options
MM = datetime.datetime.now().strftime("%m")

# Day Options
DD = datetime.datetime.now().strftime("%d")

# Current Date and Time Options
NOW_DATE = datetime.datetime.now().strftime("%F")
NOW_TIME = datetime.datetime.now().strftime("%H-%M")
now_h_m = datetime.datetime.now().strftime("%H-%M")
NOW_NOW = f"{NOW_DATE}-{NOW_TIME}"

# ========================================================================== #
# This section creates directories and files for the new logik projekt.
# ========================================================================== #

def create_projekt_directories(script_path):
    '''
    Function to create directories for logik projekt setup

    Args:
        script_path (str): The base path of the script.
    '''
    global projekt_log_dir
    projekt_log_dir = os.path.join(script_path, 'log', YYYY, MM, DD)

    if not os.path.exists(projekt_log_dir):
        os.makedirs(projekt_log_dir)
        logger.debug(f"Created directory: {projekt_log_dir}")
    else:
        logger.debug(f"Directory already exists: {projekt_log_dir}")

# -------------------------------------------------------------------------- #

def backup_file(file):
    '''
    Function to backup existing files

    Args:
        file (str): The file to be backed up.
    '''
    if os.path.isfile(file):
        shutil.move(file, f"{file}.bak")
        logger.debug(f"Backed up file: {file} to {file}.bak")

# -------------------------------------------------------------------------- #

def create_log_file(filename):
    '''
    Function to create log file

    Args:
        filename (str): The name of the log file to create.
    '''
    log_file = os.path.join(projekt_log_dir, filename)
    backup_file(log_file)
    with open(log_file, 'w') as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Logik Projekt Setup Log\n")
    logger.debug(f"Created log file: {log_file}")

# -------------------------------------------------------------------------- #

def create_setup_file(filename):
    '''
    Function to create setup file

    Args:
        filename (str): The name of the setup file to create.
    '''
    setup_file = os.path.join(projekt_log_dir, filename)
    backup_file(setup_file)
    open(setup_file, 'a').close()
    logger.debug(f"Created setup file: {setup_file}")

# ========================================================================== #
# This section prompts the user to choose a logik projekt template.
# ========================================================================== #

def browse_for_template(operating_system, app):
    '''
    Function to browse for projekt setup template

    Args:
        operating_system (str): The operating system (Linux or macOS).
        app (QApplication): The QApplication instance.
    
    Returns:
        str: The chosen projekt setup template path.
    '''
    if operating_system == "Linux":
        chosen_projekt_setup_template, _ = QFileDialog.getOpenFileName(
            None, "Select Projekt Setup File", "", "All Files (*)"
        )
        logger.debug(f"Linux selected projekt setup template: {chosen_projekt_setup_template}")
    else:
        chosen_projekt_setup_template = subprocess.run(
            [
                'osascript', '-e',
                'tell application "System Events" to activate',
                '-e', 'POSIX path of (choose file with prompt "Select Projekt Setup File")'
            ],
            capture_output=True, text=True
        ).stdout.strip()
        logger.debug(f"macOS selected projekt setup template: {chosen_projekt_setup_template}")

    if not chosen_projekt_setup_template:
        logger.error("File selection canceled.")
        print("File selection canceled.")
        exit(1)

    return chosen_projekt_setup_template

# -------------------------------------------------------------------------- #

def prompt_for_template_gui(app):
    '''
    Function to prompt user for projekt setup template using a GUI

    Args:
        app (QApplication): The QApplication instance.
    '''
    global has_projekt_setup_template

    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Question)
    msg_box.setText("Do you have a projekt setup template?")
    msg_box.setWindowTitle("Projekt Setup Template")
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    
    result = msg_box.exec()
    
    if result == QMessageBox.Yes:
        has_projekt_setup_template = True
        return browse_for_template(operating_system, app)
    else:
        has_projekt_setup_template = False
        return None

# ========================================================================== #
# This section defines the function to setup a new logik projekt template.
# ========================================================================== #

def setup_logik_projekt(script_path, operating_system, app):
    '''
    Function to setup logik projekt and initialize global variables

    Args:
        script_path (str): The base path of the script.
        operating_system (str): The operating system (Linux or macOS).
        app (QApplication): The QApplication instance.
    '''
    logger.debug(f"Setting up logik projekt at {script_path} for {operating_system}")
    create_projekt_directories(script_path)

    projekt_creation_log_filename = f"{NOW_NOW}-projekt_creation_log"
    create_log_file(projekt_creation_log_filename)
    global projekt_creation_log_file
    projekt_creation_log_file = os.path.join(projekt_log_dir, projekt_creation_log_filename)

    projekt_setup_filename = f"{NOW_NOW}-projekt_setup_file"
    create_setup_file(projekt_setup_filename)
    global projekt_setup_file
    projekt_setup_file = os.path.join(projekt_log_dir, projekt_setup_filename)

    projekt_setup_template_name = "projekt_setup_template"
    global projekt_setup_template
    projekt_setup_template = os.path.join(projekt_log_dir, projekt_setup_template_name)

    chosen_projekt_setup_template = prompt_for_template_gui(app)

    if has_projekt_setup_template:
        if not os.path.isfile(projekt_setup_template):
            shutil.copy(chosen_projekt_setup_template, projekt_setup_template)
            logger.debug("Chosen projekt setup template backed up.")
            print("  Chosen projekt setup template backed up.")
    else:
        create_projekt_directories(script_path)
        create_log_file(projekt_creation_log_filename)

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

if __name__ == "__main__":
    app = QApplication(sys.argv)
    script_path = os.path.dirname(os.path.realpath(__file__))
    operating_system = "Linux" if os.name == "posix" else "macOS"
    setup_logik_projekt(script_path, operating_system, app)
    sys.exit(app.exec())





















# import os
# import datetime
# import logging
# import shutil
# from tkinter import filedialog, Tk
# import subprocess

# # ========================================================================== #
# # This section configures logging.
# # ========================================================================== #

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     handlers=[
#         logging.FileHandler("function_04-setup.log"),
#         logging.StreamHandler()
#     ]
# )
# logger = logging.getLogger(__name__)

# # ========================================================================== #
# # This section defines global variables.
# # ========================================================================== #

# projekt_log_dir = ""
# projekt_creation_log_file = ""
# projekt_setup_file = ""
# projekt_setup_template = ""
# has_projekt_setup_template = ""

# # ========================================================================== #
# # This section defines variables based on the date.
# # ========================================================================== #

# # Year Options
# YYYY = datetime.datetime.now().strftime("%Y")

# # Month Options
# MM = datetime.datetime.now().strftime("%m")

# # Day Options
# DD = datetime.datetime.now().strftime("%d")

# # Current Date and Time Options
# NOW_DATE = datetime.datetime.now().strftime("%F")
# NOW_TIME = datetime.datetime.now().strftime("%H-%M")
# now_h_m = datetime.datetime.now().strftime("%H-%M")
# NOW_NOW = f"{NOW_DATE}-{NOW_TIME}"

# # ========================================================================== #
# # This section creates directories and files for the new logik projekt.
# # ========================================================================== #

# def create_projekt_directories(script_path):
#     '''
#     Function to create directories for logik projekt setup

#     Args:
#         script_path (str): The base path of the script.
#     '''
#     global projekt_log_dir
#     projekt_log_dir = os.path.join(script_path, 'log', YYYY, MM, DD)

#     if not os.path.exists(projekt_log_dir):
#         os.makedirs(projekt_log_dir)
#         logger.debug(f"Created directory: {projekt_log_dir}")
#     else:
#         logger.debug(f"Directory already exists: {projekt_log_dir}")


# # -------------------------------------------------------------------------- #

# def backup_file(file):
#     '''
#     Function to backup existing files

#     Args:
#         file (str): The file to be backed up.
#     '''
#     if os.path.isfile(file):
#         shutil.move(file, f"{file}.bak")

# # -------------------------------------------------------------------------- #

# def create_log_file(filename):
#     '''
#     Function to create log file

#     Args:
#         filename (str): The name of the log file to create.
#     '''
#     log_file = os.path.join(projekt_log_dir, filename)
#     backup_file(log_file)
#     with open(log_file, 'w') as f:
#         f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Logik Projekt Setup Log\n")
#     logger.debug(f"Created log file: {log_file}")

# # -------------------------------------------------------------------------- #

# def create_setup_file(filename):
#     '''
#     Function to create setup file

#     Args:
#         filename (str): The name of the setup file to create.
#     '''
#     setup_file = os.path.join(projekt_log_dir, filename)
#     backup_file(setup_file)
#     open(setup_file, 'a').close()
#     logger.debug(f"Created setup file: {setup_file}")

# # ========================================================================== #
# # This section prompts the user to choose a logik projekt template.
# # ========================================================================== #

# def browse_for_template(operating_system):
#     '''
#     Function to browse for projekt setup template

#     Args:
#         operating_system (str): The operating system (Linux or macOS).
    
#     Returns:
#         str: The chosen projekt setup template path.
#     '''
#     if operating_system == "Linux":
#         root = Tk()
#         root.withdraw()
#         chosen_projekt_setup_template = filedialog.askopenfilename(
#             title="Select Projekt Setup File"
#         )
#         root.destroy()
#         logger.debug(f"Linux selected projekt setup template: {chosen_projekt_setup_template}")
#     else:
#         chosen_projekt_setup_template = subprocess.run(
#             [
#                 'osascript', '-e',
#                 'tell application "System Events" to activate',
#                 '-e', 'POSIX path of (choose file with prompt "Select Projekt Setup File")'
#             ],
#             capture_output=True, text=True
#         ).stdout.strip()
#         logger.debug(f"macOS selected projekt setup template: {chosen_projekt_setup_template}")

#     if not chosen_projekt_setup_template:
#         logger.error("File selection canceled.")
#         print("File selection canceled.")
#         exit(1)

#     return chosen_projekt_setup_template

# # -------------------------------------------------------------------------- #

# def prompt_for_template():
#     '''
#     Function to prompt user for projekt setup template
#     '''
#     global has_projekt_setup_template
#     answer = input("  Do you have a projekt setup template? Y/N [N]: ").strip().upper() or "N"
#     logger.debug(f"User has projekt setup template: {answer}")

#     if answer == "Y":
#         has_projekt_setup_template = True
#         chosen_projekt_setup_template = browse_for_template(operating_system)
#         return chosen_projekt_setup_template
#     else:
#         has_projekt_setup_template = False
#         return None

# # ========================================================================== #
# # This section defines the function to setup a new logik projekt template.
# # ========================================================================== #

# def setup_logik_projekt(script_path, operating_system):
#     '''
#     Function to setup logik projekt and initialize global variables

#     Args:
#         script_path (str): The base path of the script.
#         operating_system (str): The operating system (Linux or macOS).
#     '''
#     logger.debug(f"Setting up logik projekt at {script_path} for {operating_system}")
#     create_projekt_directories(script_path)

#     projekt_creation_log_filename = f"{NOW_NOW}-projekt_creation_log"
#     create_log_file(projekt_creation_log_filename)
#     global projekt_creation_log_file
#     projekt_creation_log_file = os.path.join(projekt_log_dir, projekt_creation_log_filename)

#     projekt_setup_filename = f"{NOW_NOW}-projekt_setup_file"
#     create_setup_file(projekt_setup_filename)
#     global projekt_setup_file
#     projekt_setup_file = os.path.join(projekt_log_dir, projekt_setup_filename)

#     projekt_setup_template_name = "projekt_setup_template"
#     global projekt_setup_template
#     projekt_setup_template = os.path.join(projekt_log_dir, projekt_setup_template_name)

#     chosen_projekt_setup_template = prompt_for_template()

#     if has_projekt_setup_template:
#         if not os.path.isfile(projekt_setup_template):
#             shutil.copy(chosen_projekt_setup_template, projekt_setup_template)
#             logger.debug("Chosen projekt setup template backed up.")
#             print("  Chosen projekt setup template backed up.")
#     else:
#         create_projekt_directories(script_path)
#         create_log_file(projekt_creation_log_filename)

# # ========================================================================== #
# # This section defines how to handle the main script function.
# # ========================================================================== #

# if __name__ == "__main__":
#     script_path = os.path.dirname(os.path.realpath(__file__))
#     operating_system = "Linux" if os.name == "posix" else "macOS"
#     setup_logik_projekt(script_path, operating_system)

# # -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

# -------------------------------------------------------------------------- #
'''
# Disclaimer:       This program is part of LOGIK-PROJEKT.
#                   LOGIK-PROJEKT is free software.

#                   You can redistribute it and/or modify it under the terms
#                   of the GNU General Public License as published by the
#                   Free Software Foundation, either version 3 of the License,
#                   or any later version.

#                   This program is distributed in the hope that it will be
#                   useful, but WITHOUT ANY WARRANTY; without even the
#                   implied warranty of MERCHANTABILITY or FITNESS FOR A
#                   PARTICULAR PURPOSE.

#                   See the GNU General Public License for more details.

#                   You should have received a copy of the GNU General
#                   Public License along with this program.

#                   If not, see <https://www.gnu.org/licenses/>.
'''
# -------------------------------------------------------------------------- #
# Changelist:       
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-04-20 - 16:20:00
# comments:              refactored monolithic program into separate functions
# -------------------------------------------------------------------------- #
# version:               2.0.0
# modified:              2024-04-29 - 11:29:27
# comments:              testing production readiness
# -------------------------------------------------------------------------- #
# version:               2.0.1
# modified:              2024-04-30 - 07:06:00
# comments:              Removed 'declare -g' statements for macOS compatibility
# -------------------------------------------------------------------------- #
# version:               2.0.2
# modified:              2024-04-30 - 12:29:07
# comments:              added 'umask 0' statements for rsync commands
# -------------------------------------------------------------------------- #
# version:               2.0.3
# modified:              2024-05-03 - 10:16:09
# comments:              Restored CamelCase keys for projekt_metadata_xml_file
# -------------------------------------------------------------------------- #
# version:               2.0.4
# modified:              2024-05-03 - 10:56:34
# comments:              Restore 'jobs_dir' to /JOBS
# -------------------------------------------------------------------------- #
# version:               2.1.4
# modified:              2024-05-18 - 18:00:11
# comments:              Added GNU GPLv3 Disclaimer.
# -------------------------------------------------------------------------- #
# version:               2.1.5
# modified:              2024-05-18 - 18:45:00
# comments:              Minor modification to Disclaimer.
