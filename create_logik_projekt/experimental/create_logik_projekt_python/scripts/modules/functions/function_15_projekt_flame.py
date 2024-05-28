#!/usr/bin/env python3

import os

# -------------------------------------------------------------------------- #

# File Name:        function_15-projekt_flame.py
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
# This section creates the new logik projekt flame projekt.
# ========================================================================== #

# Function to create a logik projekt flame projekt using wiretap_create_node
def create_wiretap_projekt():
    # Set the umask to 0
    os.umask(0)

    # Create the logik projekt flame projekt node using wiretap_create_node
    # -n <parent node ID>
    # -d <display name>
    # -t <server-specific node type string (default = NODE)>
    # [-h <host name or IP address> (default = 127.0.0.1)]
    # [-s <metadata stream name> (default = none]
    # [-f <file containing metadata> (default = none)]
    # [-g <effective group>] (assumes super-user privileges)

    # Create a logik projekt flaem projekt node using wiretap
    os.system('/opt/Autodesk/wiretap/tools/current/wiretap_create_node '
              '-n /volumes/stonefs '
              f'-d "{name}" '
              '-s XML '
              f'-f "{projekt_metadata_xml_file}" | sed "s/^/  /"')
    print(f'\n{separator}\n')

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

if __name__ == "__main__":
    create_wiretap_projekt()
