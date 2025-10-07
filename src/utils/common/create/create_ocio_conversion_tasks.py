#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:      create_ocio_conversion_tasks.py
# Purpose:       Creates JSON files that describe how to make new CTF files.
# Description:   Loads JSON data and use OCIO to create new CTF files.

# Author:        phil_man@mac.com
# Copyright:     Copyright (c) 2025
# Disclaimer:    Disclaimer at bottom of script.
# License:       GNU General Public License v3.0 (GPL-3.0) .
#                https://www.gnu.org/licenses/gpl-3.0.en.html

# Version:       2026.1.0
# Status:        Production
# Type:          Application
# Created:       2025-07-01
# Modified:      2025-10-04

# Changelog:     Changelog at bottom of script.
# -------------------------------------------------------------------------- #

# -------------------------------------------------------------------------- #
# This section defines the import statements and directory paths.
# -------------------------------------------------------------------------- #

import os
import json
import re
import logging
import datetime

# -------------------------------------------------------------------------- #

# Define the directory containing the camera CTF files.
camera_ctf_dir = (
    '/'
    'opt/'
    'Autodesk/'
    'colour_mgmt/'
    'configs/'
    'legacy_configs/'
    'syncolor_ctfs/'
    'camera'
)

# Define the output directory for the JSON files.
json_output_dir = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..',
        '..',
        'cfg',
        'site-cfg',
        'flame-cfg',
        'flame-presets',
        'colour_mgmt',
        'transforms',
        'flame-colortoolkit',
        'json'
    )
)

# Define the target color spaces.
target_color_spaces = {
    'ACES2065-1': 'ACES-AP0',
    'ACEScg': 'ACES-AP1',
    # 'Linear Rec.709 (sRGB)': 'Scene-Linear-sRGB',
    # 'Linear P3-D65': 'P3-D65',
    # 'Linear Rec.2020': 'Rec2020',
    # 'Rec.1886 Rec.709 - Display': 'Rec709-Display',
}

# -------------------------------------------------------------------------- #
# Setup Logging
# -------------------------------------------------------------------------- #

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
    (f"ocio_conversion_tasks_"
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


def get_input_space_from_ctf_name(ctf_file_name):
    """
    Infers the OCIO input space name from the CTF file name.
    This function needs to be comprehensive and cover all expected CTF
    naming conventions.
    """

    if "AppleLog" in ctf_file_name:
        return "Apple Log"

    elif "Alexa-v2-LogC" in ctf_file_name:
        return "ARRI LogC3 (EI800)"
    elif "Alexa-v3-LogC" in ctf_file_name:
        return "ARRI LogC3 (EI800)"
    elif "LogC4" in ctf_file_name:
        return "ARRI LogC4"
    elif "LinearARRIWideGamut4" in ctf_file_name:
        return "Linear ARRI Wide Gamut 4"

    elif "BMDFilm" in ctf_file_name:
        return "BMDFilm WideGamut Gen5"
    elif "DaVinciIntermediate" in ctf_file_name:
        return "DaVinci Intermediate WideGamut"
    elif "LinearBMDWideGamut" in ctf_file_name:
        return "Linear BMD WideGamut Gen5"
    elif "LinearDaVinciWideGamut" in ctf_file_name:
        return "Linear DaVinci WideGamut"

    elif "CanonLog2" in ctf_file_name:
        return "CanonLog2 CinemaGamut D55"
    elif "CanonLog3" in ctf_file_name:
        return "CanonLog3 CinemaGamut D55"
    elif "C500_CinemaGamut_D55" in ctf_file_name:
        return "CanonLog2 CinemaGamut D55"
    elif "C500_CinemaGamut_Tng" in ctf_file_name:
        return "CanonLog2 CinemaGamut D55"
    elif "C500_DCI-P3+_D55" in ctf_file_name:
        return "CanonLog2 CinemaGamut D55"
    elif "C500_DCI-P3+_Tng" in ctf_file_name:
        return "CanonLog2 CinemaGamut D55"

    elif "VLog" in ctf_file_name:
        return "V-Log V-Gamut"
    elif "LinearVGamut" in ctf_file_name:
        return "Linear V-Gamut"

    elif "REDlogFilm" in ctf_file_name:
        return "Log3G10 REDWideGamutRGB"
    elif "LinearDRAGONcolor2" in ctf_file_name:
        return "Linear REDcolor2"
    elif "LinearDRAGONcolor" in ctf_file_name:
        return "Linear REDcolor"
    elif "LinearREDWideGamutRGB" in ctf_file_name:
        return "Linear REDWideGamutRGB"
    elif "LinearREDcolor2" in ctf_file_name:
        return "Linear REDcolor2"
    elif "LinearREDcolor3" in ctf_file_name:
        return "Linear REDcolor3"
    elif "LinearREDcolor4" in ctf_file_name:
        return "Linear REDcolor4"
    elif "LinearREDcolor" in ctf_file_name:
        return "Linear REDcolor"
    elif "Log3G10-REDWideGamutRGB" in ctf_file_name:
        return "Log3G10 REDWideGamutRGB"

    elif "SLog2" in ctf_file_name:
        return "S-Log2 S-Gamut"
    elif "SLog3" in ctf_file_name:
        return "S-Log3 S-Gamut3"
    elif "F35-SLog" in ctf_file_name:
        return "S-Log3 S-Gamut3"
    elif "F65-Raw" in ctf_file_name:
        return "Raw"
    elif "LinearSGamut3-Venice" in ctf_file_name:
        return "Linear Venice S-Gamut3"
    elif "LinearSGamut3" in ctf_file_name:
        return "Linear S-Gamut3"
    elif "Raw-SGamut3" in ctf_file_name:
        return "Raw"

    elif "Phantom-Log2" in ctf_file_name:
        return "Phantom-Log2"

    elif "HybridLogGamma" in ctf_file_name:
        return "Camera Rec.2100-HLG"

    elif "untonemapped_Rec709-camera" in ctf_file_name:
        return "Camera Rec.709"

    return "Unknown"  # Default if no match is found


def get_latest_ocio_config_file():
    """
    Finds the OCIO config JSON file with the highest version number.
    """
    json_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            '..',
            '..',
            '..',
            'cfg',
            'site-cfg',
            'ocio'
        )
    )
    if not os.path.isdir(json_dir):
        logging.warning(f"JSON directory not found at {json_dir}")
        return None

    pattern = re.compile(r'ocio_v(\d+)_(\d+)_config\.json')

    latest_version = (-1, -1)
    latest_file = None

    for filename in os.listdir(json_dir):
        match = pattern.match(filename)
        if match:
            major = int(match.group(1))
            minor = int(match.group(2))

            if (major > latest_version[0] or
                    (major == latest_version[0] and
                     minor > latest_version[1])):
                latest_version = (major, minor)
                latest_file = os.path.join(json_dir, filename)

    return latest_file


# -------------------------------------------------------------------------- #
# Main function to generate the conversion tasks.
# -------------------------------------------------------------------------- #


def generate_conversion_tasks():
    # Find and load the latest OCIO config file.
    latest_ocio_config_path = get_latest_ocio_config_file()
    available_color_spaces = []

    if latest_ocio_config_path:
        logging.info(
            f"Using latest OCIO config: "
            f"{os.path.basename(latest_ocio_config_path)}"
        )
        try:
            with open(latest_ocio_config_path, 'r') as f:
                ocio_data = json.load(f)
            available_color_spaces = (
                ocio_data.get("ocio_configuration", {})
                .get("available_color_spaces", [])
            )
            if not available_color_spaces:
                logging.error(
                    "Could not find 'available_color_spaces' in the "
                    "config file. Exiting."
                )
                return
        except (json.JSONDecodeError, FileNotFoundError) as e:
            logging.error(
                f"Error reading or parsing OCIO config file: {e}. "
                f"Exiting."
            )
            return
    else:
        logging.error(
            "No OCIO config file found. Cannot validate color spaces. "
            "Exiting."
        )
        return

    # Ensure the root output directory exists.
    os.makedirs(json_output_dir, exist_ok=True)

    # Walk through the camera CTF directory.
    for root, dirs, files in os.walk(camera_ctf_dir):
        for file in files:
            if file.endswith('.ctf') and '_to_ACES' in file:
                ctf_path = os.path.join(root, file)
                ctf_file_name = os.path.basename(ctf_path)

                # Infer the input space from the CTF file name.
                input_space_ocio = get_input_space_from_ctf_name(
                    ctf_file_name
                )

                if input_space_ocio == "Unknown":
                    logging.warning(
                        f"Could not infer input space for {ctf_file_name}. "
                        f"Skipping."
                    )
                    continue

                # Validate the inferred space against the available OCIO
                # color spaces.
                if input_space_ocio not in available_color_spaces:
                    logging.warning(
                        f"Inferred space '{input_space_ocio}' for "
                        f"{ctf_file_name} is not in the available OCIO "
                        f"config spaces. Skipping."
                    )
                    continue

                # Infer the camera space name for the output file name.
                # Replace any spaces with underscores, but preserve hyphens
                # from original CTF name.
                camera_space_name = (
                    ctf_file_name
                    .replace('_to_ACES.ctf', '')
                    .replace(' ', '_')
                )

                for target_space_ocio, target_space_name in (
                        target_color_spaces.items()):
                    # Ensure conversion_name and output_clf_name also
                    # replace any spaces with underscores
                    conversion_name_raw = (
                        f"{camera_space_name}_to_{target_space_name}"
                    )
                    conversion_name = conversion_name_raw.replace(' ', '_')
                    output_clf_name = f"{conversion_name}.clf"

                    conversion_task = {
                        "name": conversion_name,
                        "output_clf": output_clf_name,
                        "input_space": input_space_ocio,
                        "target_space": target_space_ocio,
                        "inputs": [
                            {
                                "file": ctf_path,
                                "inverse": False
                            }
                        ]
                    }

                    # Create the same subdirectory structure in the output
                    # directory.
                    relative_path = os.path.relpath(root, camera_ctf_dir)
                    output_subdirectory = os.path.join(
                        json_output_dir,
                        relative_path
                    )
                    os.makedirs(output_subdirectory, exist_ok=True)

                    # Write each conversion task to a separate JSON file in
                    # the correct subdirectory.
                    json_filename = f"{conversion_name}.json"
                    json_filepath = os.path.join(
                        output_subdirectory,
                        json_filename
                    )
                    with open(json_filepath, 'w') as f:
                        json.dump(conversion_task, f, indent=2)

                    # Make the output path relative for cleaner printing
                    printed_path = os.path.join(relative_path, json_filename)
                    logging.info(f"Generated: {printed_path}")

    logging.info(
        f"\nSuccessfully generated all conversion tasks in "
        f"{json_output_dir}"
    )


# -------------------------------------------------------------------------- #
# Run the main function.
# -------------------------------------------------------------------------- #


if __name__ == '__main__':
    generate_conversion_tasks()


# -------------------------------------------------------------------------- #

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

# -------------------------------------------------------------------------- #
# C2 A9 32 30 32 35 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 #
# -------------------------------------------------------------------------- #
# Changelog:
# -------------------------------------------------------------------------- #
