import os
import re
import datetime
import logging

logger = logging.getLogger(__name__)

def generate_backup_filename(filepath: str) -> str:
    """
    Generates a backup filename with the current date.

    Args:
        filepath (str): The original file path.

    Returns:
        str: The backup filename.
    """
    date_str = datetime.datetime.now().strftime("%Y_%m_%d")
    base, ext = os.path.splitext(filepath)
    return f"{base}-{date_str}.bak"


def modify_script_file(filepath: str, search_replace_dict: dict):
    """
    Modifies a script file by performing search and replace operations.

    Args:
        filepath (str): The path to the script file.
        search_replace_dict (dict): A dictionary where keys are search strings
                                    and values are replace strings.
    """
    try:
        with open(filepath, 'r') as file:
            script_content = file.read()

        for search, replace in search_replace_dict.items():
            script_content = re.sub(re.escape(search), replace, script_content)

        with open(filepath, 'w') as file:
            file.write(script_content)

        logger.info(f"Successfully modified script: {os.path.basename(filepath)}")

    except Exception as e:
        logger.error(f"Error modifying script file {os.path.basename(filepath)}: {e}")


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
