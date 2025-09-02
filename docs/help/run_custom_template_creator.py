#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     run_custom_template_creator.py
# Purpose:      Wrapper script to run create_customized_filesystem_template.py
#               with the Autodesk Python interpreter specified in a .pref file.
# Description:  Reads the path to the Autodesk Python executable from
#               install/current_adsk_python_version.pref and then executes
#               src/utils/common/create/create_customized_filesystem_template.py
#               using that specific Python version.

# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2026.1.0
# Status:       Development
# Type:         Utility
# Created:      2025-08-07
# Modified:     2025-08-07

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #

import sys
import os
import subprocess
from pathlib import Path


def get_repository_root_dir():
    """
    Finds the repository root directory by searching for a marker file.
    """
    current_dir = Path(__file__).resolve().parent
    while current_dir != current_dir.parent:
        if (current_dir / ".repository_root.dir").exists():
            return current_dir
        current_dir = current_dir.parent
    raise FileNotFoundError("Repository root marker '.repository_root.dir' not found.")


def main():
    try:
        repo_dir = get_repository_root_dir()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Define the path to the .pref file relative to the repository root
    python_pref_file = repo_dir / "install" / "current_adsk_python_version.pref"

    # Define the path to the target Python script relative to the repository root
    target_script = repo_dir / "src" / "utils" / "common" / "create" / "create_customized_filesystem_template.py"

    # Read the Python executable path from the .pref file
    if not python_pref_file.is_file():
        print(f"Error: Python preference file not found at {python_pref_file}")
        sys.exit(1)

    try:
        with open(python_pref_file, 'r') as f:
            adsk_python_exec = f.read().strip()
    except IOError as e:
        print(f"Error reading Python preference file: {e}")
        sys.exit(1)

    # Check if the Autodesk Python executable exists and is executable
    if not Path(adsk_python_exec).is_file() or not os.access(adsk_python_exec, os.X_OK):
        print(f"Error: Autodesk Python executable not found or not executable at {adsk_python_exec}")
        sys.exit(1)

    print(f"Using Autodesk Python: {adsk_python_exec}")
    print(f"Running script: {target_script}")

    # Execute the target Python script using the Autodesk Python executable
    try:
        # Get the current environment and set PYTHONPATH
        env = os.environ.copy()
        env['PYTHONPATH'] = str(repo_dir) + os.pathsep + env.get('PYTHONPATH', '')

        # Use subprocess.run to execute the script with the specified interpreter
        # capture_output=False allows the child process's stdout/stderr to go directly to the console
        result = subprocess.run(
            [adsk_python_exec, str(target_script)],
            check=False,
            capture_output=False,
            env=env
        )
        if result.returncode != 0:
            print(f"Script exited with error code {result.returncode}")
            sys.exit(result.returncode)
    except FileNotFoundError:
        print(f"Error: The specified Python executable '{adsk_python_exec}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

# -------------------------------------------------------------------------- #
# Changelog:
# -------------------------------------------------------------------------- #
# Version:      2026.1.0
# Modification: 2025-08-07
# Changelist:
#   - Initial creation of the Python wrapper script.
#   - Reads Autodesk Python executable path from .pref file.
#   - Executes target script using the specified Python interpreter.
#   - Includes error handling for file existence and executability.
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

#               If not, see <https://www.gnu.org/licenses/gpl-3.0.0.en.html>.

#               Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #
