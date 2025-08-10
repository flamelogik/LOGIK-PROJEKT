#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     create_logs.py
# Purpose:      Provides functions for setting up and managing logs.
# Description:  This module offers utilities to create log files for both shell
#               and Python script executions, ensuring proper logging setup.

# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2026.1.0
# Status:       Production
# Type:         Utility
# Created:      2025-07-01
# Modified:     2025-08-03

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #

import os
import sys

def log_shell_script_activity(
    program_name
):
    """
    set up logging for shell scripts.

    args:
        program_name: name of the program being logged

    returns:
        path to the log file

    requires:
        repo_dir and projekt_now environment variables to be set
    """
    repo_dir = os.environ.get(
        'repo_dir'
    )
    projekt_now = os.environ.get(
        'projekt_now'
    )

    if not repo_dir:
        print(
            "error: repo_dir is not set.",
            file=sys.stderr
        )
        return None

    if not projekt_now:
        print(
            "error: projekt_now is not set.",
            file=sys.stderr
        )
        return None

    logs_dir = os.path.join(
        repo_dir,
        "logs",
        "shell-logs"
    )
    os.makedirs(
        logs_dir,
        exist_ok=True
    )

    log_name = f"{projekt_now}-{program_name}.log"
    program_log = os.path.join(
        logs_dir,
        log_name
    )

    # set environment variable for other scripts to use
    os.environ['program_log'] = program_log

    return program_log


def log_python_script_activity(
    program_name
):
    """
    set up logging for python scripts.

    args:
        program_name: name of the program being logged

    returns:
        path to the log file

    requires:
        repo_dir and projekt_now environment variables to be set
    """
    repo_dir = os.environ.get(
        'repo_dir'
    )
    projekt_now = os.environ.get(
        'projekt_now'
    )

    if not repo_dir:
        print(
            "error: repo_dir is not set.",
            file=sys.stderr
        )
        return None

    if not projekt_now:
        print(
            "error: projekt_now is not set.",
            file=sys.stderr
        )
        return None

    logs_dir = os.path.join(
        repo_dir,
        "logs",
        "python-logs"
    )
    os.makedirs(
        logs_dir,
        exist_ok=True
    )

    log_name = f"{projekt_now}-{program_name}.log"
    program_log = os.path.join(
        logs_dir,
        log_name
    )

    # set environment variable for other scripts to use
    os.environ['program_log'] = program_log

    return program_log


# if run directly, show usage information
if __name__ == "__main__":
    print(
        "this module provides logging functions for python scripts."
    )
    print(
        "import and use these functions in your main script."
    )
    print(
        "example:"
    )
    print(
        "  from create_logs import log_python_script_activity"
    )
    print(
        "  program_log = log_python_script_activity('my_program')"
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
