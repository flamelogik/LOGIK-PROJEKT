# filename: debug_and_log.py

'''
# -------------------------------------------------------------------------- #

# File Name:        debug_and_log.py
# Version:          0.0.1
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-05-18
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program defines files and folders and sets up
#                   debugging and logging capabilities.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #
'''

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

import os

# import pdb; pdb.set_trace()

import logging

from datetime import datetime

# ========================================================================== #
# This section defines paths and files.
# ========================================================================== #

# script_path = os.path.abspath(__file__)
# script_name = os.path.basename(script_path)
# script_name_without_extension = os.path.splitext(script_name)[0]
# script_directory = os.path.dirname(script_path)
# log_directory = os.path.join(script_directory, 'log')

# if not os.path.exists(log_directory):
#     os.makedirs(log_directory)

# log_filename = f"{datetime.now():%Y-%m-%d-%H-%M}_{script_name}.debug.log"
# log_filepath = os.path.join(log_directory, log_filename)

# ========================================================================== #
# This section enables debugging.
# ========================================================================== #

def setup_logging(script_directory):
    """
    Set up logging for the script.

    Args:
        script_directory (str): The directory where the script is located.

    Returns:
        str: The full path to the log file.
    """
    # Navigate to the log directory from the script directory
    log_directory = os.path.join(script_directory, '..', '..', '..', 'log')
    log_directory = os.path.abspath(log_directory)

    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_filename = f"{datetime.now():%Y-%m-%d-%H-%M}_logik_projekt_creator.debug.log"
    log_filepath = os.path.join(log_directory, log_filename)

    logging.basicConfig(
        filename=log_filepath,
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    return log_filepath
# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

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

# Changelist:       
# -------------------------------------------------------------------------- #
