#!/usr/bin/env python3
# ------------------------------------------------------------------------- #
# Filename:      create_ocio_config_json_file.py
# Purpose:       Generates a structured JSON file containing OCIO Color
#                Space information.
# Description:   Loads an Autodesk Flame OCIO config, extracts color space
#                data, and saves it as a JSON file for downstream
#                processing.

# Author:        phil_man@mac.com
# Copyright:     Copyright (c) 2025
# Disclaimer:    Disclaimer at bottom of script.
# License:       GNU General Public License v3.0 (GPL-3.0) .
#                https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:       2026.1.0
# Status:        Production
# Type:          Application
# Created:       2025-07-01
# Modified:      2025-08-25

# Changelog:     Changelog at bottom of script.
# ------------------------------------------------------------------------- #

# ------------------------------------------------------------------------- #
# This section defines the import statements and directory paths.
# ------------------------------------------------------------------------- #

import os
import json
import traceback
import PyOpenColorIO as ocio
import logging
import datetime

# ------------------------------------------------------------------------- #

# Define the path to the Autodesk Colour Mgmt Directory.
adsk_colour_mgmt_dir = (
    '/opt/'
    'Autodesk/'
    'colour_mgmt'
)

# Define the path to the OCIO config directory.
ocio_config_directory = (
    'configs/'
    'flame_configs/'
    '2026.0/'
    'aces2.0_config'
)

# Define the name of the OCIO config file.
ocio_config_filename = (
    'config.ocio'
)

# Define the path to the OCIO config file.
config_file_path = (
    os.path.join(
        adsk_colour_mgmt_dir,
        ocio_config_directory,
        ocio_config_filename
    )
)

# ------------------------------------------------------------------------- #
# Setup Logging
# ------------------------------------------------------------------------- #

log_dir = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..',
        '..',
        'logs',
    )
)

os.makedirs(log_dir, exist_ok=True)
log_filename = os.path.join(
    log_dir,
    (f"ocio_config_json_"
     f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)

# ------------------------------------------------------------------------- #
# First Try Block: Generate Markdown Report
# ------------------------------------------------------------------------- #

logging.info(f"Attempting to load config from: {config_file_path}")
logging.info(f"File exists: {os.path.exists(config_file_path)}")

try:
    # Load the OCIO config file.
    config = ocio.Config.CreateFromFile(config_file_path)

    # Define the path to the Available OCIO Color Spaces output file.
    output_file_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            '..',
            '..',
            '..',
            'cfg',
            'site-cfg',
            'ocio',
            (f'ocio_v{config.getMajorVersion()}_'
             f'{config.getMinorVersion()}_color_space_names.md')
        )
    )

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    # Get the list of color spaces.
    color_spaces = config.getColorSpaces()

    # Get the list of color space names as strings.
    color_space_names = [cs.getName() for cs in color_spaces]

    # Define the separator line.
    separator_line = "+ " + "-" * 75 + " +\n"

    with open(output_file_path, 'w') as f:
        f.write(f"# {config.getDescription()} : OCIO Color Spaces\n\n")
        f.write("```bash\n")
        f.write(separator_line)
        f.write("  OCIO Configuration Details\n")
        f.write("+ " + "-" * 75 + " +\n")
        f.write(f"  Colour_Mgmt Dir:         "
                f"{adsk_colour_mgmt_dir}\n")
        f.write(f"  Config Filepath:         "
                f"{ocio_config_directory}/\n")
        f.write(f"  Config Filename:         "
                f"{ocio_config_filename}\n\n")
        f.write("+ " + "-" * 75 + " +\n")
        f.write(f"  OCIO Profile Version:    "
                f"{config.getMajorVersion()}."
                f"{config.getMinorVersion()}\n")
        f.write(f"  Config Name:             "
                f"{config.getName()}\n")
        f.write(f"  Description:             "
                f"{config.getDescription()}\n\n")
        f.write("+ " + "-" * 75 + " +")
        f.write("  Available Color Spaces\n")
        f.write("+ " + "-" * 75 + " +\n")
        for cs_name in color_space_names:
            f.write(f"- {cs_name}\n")
        f.write("\n" + "+ " + "-" * 75 + " +")
        f.write("```\n")

    logging.info(f"Successfully wrote color spaces to {output_file_path}")

except ocio.Exception as e:
    logging.error(f"OCIO Error Type: {type(e).__name__}")
    logging.error(f"OCIO Error Message: {str(e)}")
    logging.error("Full traceback:")
    traceback.print_exc()
except FileNotFoundError as e:
    logging.error(f"File Not Found Error: {e}")
except Exception as e:
    logging.error(f"Unexpected error: {type(e).__name__}")
    logging.error(f"Error message: {str(e)}")
    traceback.print_exc()

# ------------------------------------------------------------------------- #
# Second Try Block: Generate JSON Configuration
# ------------------------------------------------------------------------- #

try:
    # Load the OCIO config file.
    config = ocio.Config.CreateFromFile(config_file_path)

    # Define the path to the JSON output file.
    json_output_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            '..',
            '..',
            '..',
            'cfg',
            'site-cfg',
            'ocio',
            (f'ocio_v{config.getMajorVersion()}_'
             f'{config.getMinorVersion()}_config.json')
        )
    )

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(json_output_path), exist_ok=True)

    # Get the list of color space names as strings.
    color_space_names = [
        cs.getName() for cs in config.getColorSpaces()
    ]

    # Create the dictionary for the JSON output.
    ocio_data = {
        "ocio_configuration": {
            "name": config.getDescription(),
            "configuration_details": {
                "colour_management_directory": adsk_colour_mgmt_dir,
                "config_filepath": f"{ocio_config_directory}/",
                "config_filename": ocio_config_filename
            },
            "profile_information": {
                "version": (f"{config.getMajorVersion()}."
                            f"{config.getMinorVersion()}"),
                "name": config.getName(),
                "description": config.getDescription()
            },
            "available_color_spaces": color_space_names
        }
    }

    # Write the JSON file.
    with open(json_output_path, 'w') as f:
        json.dump(ocio_data, f, indent=2)

    logging.info(
        f"Successfully wrote OCIO configuration to {json_output_path}"
    )

except ocio.Exception as e:
    logging.error(f"OCIO Error Type: {type(e).__name__}")
    logging.error(f"OCIO Error Message: {str(e)}")
    logging.error("Full traceback:")
    traceback.print_exc()
except FileNotFoundError as e:
    logging.error(f"File Not Found Error: {e}")
except Exception as e:
    logging.error(f"Unexpected error: {type(e).__name__}")
    logging.error(f"Error message: {str(e)}")
    traceback.print_exc()


# ------------------------------------------------------------------------- #

# DISCLAIMER:    This file is part of LOGIK-PROJEKT.

#                Copyright © 2025 STRENGTH IN NUMBERS

#                LOGIK-PROJEKT creates directories, files, scripts & tools
#                for use with Autodesk Flame and other software.

#                LOGIK-PROJEKT is free software.

#                You can redistribute it and/or modify it under the terms
#                of the GNU General Public License as published by the
#                Free Software Foundation, either version 3 of the License,
#                or any later version.

#                This program is distributed in the hope that it will be
#                useful, but WITHOUT ANY WARRANTY; without even the

#                implied warranty of MERCHANTABILITY or
#                FITNESS FOR A PARTICULAR PURPOSE.

#                See the GNU General Public License for more details.
#                You should have received a copy of the GNU General
#                Public License along with this program.

#                If not, see <https://www.gnu.org/licenses/gpl-3.0.en.html>.

#                Contact: phil_man@mac.com

# ------------------------------------------------------------------------- #
# C2 A9 32 30 32 35 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 #
# ------------------------------------------------------------------------- #
# Changelog:
# ------------------------------------------------------------------------- #