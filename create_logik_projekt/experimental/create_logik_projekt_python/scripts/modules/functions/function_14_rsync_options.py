#!/usr/bin/env python3

import os
import datetime

# -------------------------------------------------------------------------- #

# File Name:        function_14-rsync_options.py
# Version:          2.1.5
# Language:         Python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-05-18
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program contains function(s) that are used to
#                   create new logik projekts.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section creates a variable to store rsync options.
# ========================================================================== #

# The following command is too long:
# 'rsync -av --no-group --no-perms --no-times --size-only --ignore-existing '

# Wrap the rsync options as a list into the variable 'sync_opts'
sync_opts = ['-av', '--no-group', '--no-perms', '--no-times', '--size-only', '--ignore-existing']
# sync_opts = '-av --no-group --no-perms --no-times --size-only --ignore-existing'
# sync_opts = '-av --ignore-existing'
# sync_opts = '-av'

# To use the variable in your rsync command
# rsync_command = ['rsync'] + sync_opts + ['source_directory/', 'destination_directory/']
# os.system(' '.join(rsync_command))

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines a function to create directories for logik projekt setup
# ========================================================================== #

def create_metadata_directories():
    now = datetime.datetime.now()
    script_path = os.path.dirname(os.path.abspath(__file__))
    YYYY = str(now.year)
    MM = str(now.month).zfill(2)
    DD = str(now.day).zfill(2)
    projekt_log_dir = os.path.join(script_path, 'xml', YYYY, MM, DD)
    if not os.path.isdir(projekt_log_dir):
        os.makedirs(projekt_log_dir)

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines a function to write metadata to file
# ========================================================================== #

def write_projekt_metadata():
    create_metadata_directories()
    now = datetime.datetime.now()
    script_path = os.path.dirname(os.path.abspath(__file__))
    YYYY = str(now.year)
    MM = str(now.month).zfill(2)
    DD = str(now.day).zfill(2)
    projekt_metadata_xml_file = os.path.join(script_path, 'xml', YYYY, MM, DD, 'projekt_metadata.xml')
    with open(projekt_metadata_xml_file, 'w') as f:
        f.write('<Project>')
        f.write('<Name>{}</Name>'.format(name))
        f.write('<Nickname>{}</Nickname>'.format(nickname))
        # Add other metadata fields here
        f.write('</Project>')
    print('projekt XML:', os.path.basename(projekt_metadata_xml_file))

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

if __name__ == "__main__":
    write_projekt_metadata()
