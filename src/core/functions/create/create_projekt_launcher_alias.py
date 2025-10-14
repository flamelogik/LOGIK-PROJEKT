#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     create_projekt_launcher_alias.py
# Purpose:      Creates a shell alias for launching the Flame project.
# Description:  This script generates a shell alias to simplify the execution
#               of the Flame project launcher script.

# Author:       phil_man@mac.com
# Copyright:    Copyright (c) 2025
# Disclaimer:   Disclaimer at bottom of script.
# License:      GNU General Public License v3.0 (GPL-3.0).
#               https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:      2026.1.0
# Status:       Development
# Type:         Utility
# Created:      2025-07-01
# Modified:     2025-10-08

# Changelog:    Changelog at bottom of script.
# -------------------------------------------------------------------------- #

import os
import logging
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def create_projekt_launcher_alias(alias_name: str, launcher_script_path: str):
    """
    Creates a shell alias for launching the Flame project.

    Args:
        alias_name (str): The name for the alias (e.g., 'start_my_projekt').
        launcher_script_path (str): The absolute path to the launcher 
        script to be aliased.
    """
    logging.info(
        f"Attempting to create project launcher alias '{alias_name}'..."
    )

# -------------------------------------------------------------------------- #

    # This is a placeholder for the alias creation logic.
    # The following is a commented-out example of how this could 
    # be implemented.

    # try:
    #     shell_path = os.environ.get('SHELL', '')
    #     home_dir = Path.home()
    #     rc_file_path = None

    #     if 'bash' in shell_path:
    #         rc_file_path = home_dir / '.bashrc'
    #     elif 'zsh' in shell_path:
    #         rc_file_path = home_dir / '.zshrc'
    #     else:
    #         logging.warning(
    #             f"Unsupported shell detected: {shell_path}. "
    #             "Alias creation skipped."
    #         )
    #         return

    #     if not rc_file_path.exists():
    #         logging.warning(
    #             f"Shell configuration file not found: {rc_file_path}. "
    #             "Alias creation skipped."
    #         )
    #         return

    #     alias_command = (
    #         f'\nalias {alias_name}="bash {launcher_script_path}"\n'
    #     )
    #     alias_comment = (
    #         f'# Alias for LOGIK-PROJEKT: {alias_name}\n'
    #     )

    #     # Check if the alias already exists to avoid duplicates
    #     with open(rc_file_path, 'r', encoding='utf-8') as f:
    #         if alias_command in f.read():
    #             logging.info(
    #                 f"Alias '{alias_name}' already exists in "
    #                 f"{rc_file_path}. Skipping."
    #             )
    #             return

    #     # Append the alias to the rc file
    #     with open(rc_file_path, 'a', encoding='utf-8') as f:
    #         f.write('\n')
    #         f.write(alias_comment)
    #         f.write(alias_command)

    #     logging.info(
    #         f"Successfully added alias '{alias_name}' to {rc_file_path}."
    #     )
    #     logging.info(
    #         "Please restart your terminal or source the config file "
    #         "(e.g., 'source ~/.bashrc') to use the new alias."
    #     )

    # except Exception as e:
    #     logging.error(
    #         f"An unexpected error occurred during alias creation: {e}"
    #     )

# -------------------------------------------------------------------------- #

    logging.info(
        "Alias creation step is currently a placeholder "
        "and has been skipped.")


if __name__ == "__main__":
    # Example usage for direct script execution and testing
    if len(sys.argv) != 3:
        print(
            "Usage: python create_projekt_launcher_alias.py "
            "<alias_name> <launcher_script_path>")
        sys.exit(1)

    alias = sys.argv[1]
    script_path = sys.argv[2]

    create_projekt_launcher_alias(alias, script_path)


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
