#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     create_flame_wiretap_node.py
# Purpose:      Creates a Flame project node using wiretap_create_node.
# Description:  This script executes a bash command to create a new Autodesk
#               Flame project node via the Wiretap API, using a provided
#               XML configuration.

# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2026.1.0
# Status:       Production
# Type:         Utility
# Created:      2025-07-01
# Modified:     2025-10-08

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #

import subprocess
import logging

logger = logging.getLogger(__name__)


def create_flame_wiretap_node(flame_projekt_name, projekt_xml_path):
    """
    Create the logik projekt flame project node using wiretap_create_node.
    """

    bash_command = f"""

    umask 0

    /opt/Autodesk/wiretap/tools/current/wiretap_create_node \
    -h 127.0.0.1:IFFFS \
    -n /projects \
    -t PROJECT \
    -d "{flame_projekt_name}" \
    -s XML \
    -f "{projekt_xml_path}"
    """

    logging.info(f"Running the following bash command:\n{bash_command}")

    process = (
        subprocess.Popen(
            bash_command,
            shell=True,
            executable='/bin/bash',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    )
    stdout, stderr = process.communicate()

    if stdout:
        logging.info(
            f"Command stdout:\n{stdout.decode()}"
        )
    if stderr:
        logging.error(
            f"Command stderr:\n{stderr.decode()}"
        )


# -------------------------------------------------------------------------- #

# DISCLAIMER:   This file is part of LOGIK-PROJEKT.

#               Copyright © 2025 STRENGTH IN NUMBERS

#               LOGIK-PROJEKT creates directories, files, scripts & tools
#               for use with Autodesk Flame and other software.

#               LOGIK-PROJEKT is free software.

#               You can redistribute it and/or modify it under the terms
#               of the GNU General Public License as published by the
#               Free Software Foundation, either version 3 of the License,
#               or any later version.

#               This program is distributed in the hope that it will be
#               useful, but WITHOUT ANY WARRANTY; without even the
#               implied warranty of MERCHANTABILITY or
#               FITNESS FOR A PARTICULAR PURPOSE.

#               See the GNU General Public License for more details.
#               You should have received a copy of the GNU General
#               Public License along with this program.

#               If not, see <https://www.gnu.org/licenses/gpl-3.0.en.html>.

#               Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #
# C2 A9 32 30 32 35 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 #
# -------------------------------------------------------------------------- #
# Changelog:
# -------------------------------------------------------------------------- #
