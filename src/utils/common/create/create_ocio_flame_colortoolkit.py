#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:      create_ocio_flame_colortoolkit.py
# Purpose:       Creates the Flame_ColorToolkit Color Transform Files.
# Description:   Loads JSON files and generates CTF files.

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
import PyOpenColorIO as ocio
import logging
import datetime

# -------------------------------------------------------------------------- #

json_input_dir = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..',
        '..',
        'cfg',
        'site-cfg',
        'flame-cfg',
        'flame-scripts',
        'opencolorio',
        'flame_colortoolkit_files',
        'json'
    )
)

output_dir = os.path.abspath(
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
        'flame-colortoolkit'
    )
)

config = ocio.Config.CreateRaw()
logging.info("Using minimal OCIO config for writing CTF files only.")
os.makedirs(output_dir, exist_ok=True)

aces_to_acescg_path = (
    "/opt/Autodesk/colour_mgmt/configs/legacy_configs/"
    "syncolor_ctfs/primaries/ACES_to_ACEScg.ctf"
)

acescg_to_aces_path = (
    "/opt/Autodesk/colour_mgmt/configs/legacy_configs/"
    "syncolor_ctfs/primaries/ACEScg_to_ACES.ctf"
)


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
    (f"flame_colortoolkit_creation_"
     f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ],
    force=True
)

# -------------------------------------------------------------------------- #
# Helper Functions
# -------------------------------------------------------------------------- #


def create_forward_transform(conversion, transforms_list, conversion_name):
    """Builds the list of forward transforms."""
    ctf_input = conversion['inputs'][0]
    ctf_file_path = ctf_input.get('file')
    inverse = ctf_input.get('inverse', False)

    if not ctf_file_path or not os.path.exists(ctf_file_path):
        logging.warning(
            f"  - CTF file not found: {ctf_file_path}. Skipping."
        )
        return False

    file_transform = ocio.FileTransform(ctf_file_path)
    file_transform.setDirection(
        ocio.TRANSFORM_DIR_INVERSE if inverse
        else ocio.TRANSFORM_DIR_FORWARD
    )
    transforms_list.append(file_transform)
    logging.info(
        f"  - Stage 1: Added {os.path.basename(ctf_file_path)}"
    )

    if '-AP1' in conversion_name and os.path.exists(aces_to_acescg_path):
        transforms_list.append(ocio.FileTransform(aces_to_acescg_path))
        logging.info(
            f"  - Stage 2: Added {os.path.basename(aces_to_acescg_path)}"
        )
    elif '-AP1' in conversion_name:
        logging.warning(
            f"  - ACES to ACEScg CTF not found: {aces_to_acescg_path}"
        )
        return False

    return True


def create_inverse_transform(conversion, transforms_list, conversion_name):
    """Builds the list of inverse transforms."""
    if '-AP1' in conversion_name and os.path.exists(acescg_to_aces_path):
        t = ocio.FileTransform(acescg_to_aces_path)
        t.setDirection(ocio.TRANSFORM_DIR_FORWARD)
        transforms_list.append(t)
        logging.info(
            f"  - Stage 1 (Inverse): Added "
            f"{os.path.basename(acescg_to_aces_path)}"
        )
    elif '-AP1' in conversion_name:
        logging.warning(
            f"  - ACEScg to ACES CTF not found: {acescg_to_aces_path}"
        )
        return False

    ctf_input = conversion['inputs'][0]
    ctf_file_path = ctf_input.get('file')
    original_inverse = ctf_input.get('inverse', False)

    if not ctf_file_path or not os.path.exists(ctf_file_path):
        logging.warning(
            f"  - CTF file not found: {ctf_file_path}. Skipping."
        )
        return False

    t = ocio.FileTransform(ctf_file_path)
    t.setDirection(
        ocio.TRANSFORM_DIR_FORWARD if original_inverse
        else ocio.TRANSFORM_DIR_INVERSE
    )
    transforms_list.append(t)
    logging.info(
        f"  - Stage 2 (Inverse): Added inverted "
        f"{os.path.basename(ctf_file_path)}"
    )

    return True


def generate_inverse_name(original_name, original_output_name):
    """Generates a standard inverse name for a transform."""
    if '-AP0' in original_name:
        parts = original_name.replace('-AP0', '').split('_to_')
        if len(parts) == 2:
            return (
                f"ACES-AP0_to_{parts[0]}",
                f"ACES-AP0_to_{parts[0]}.ctf"
            )
        else:
            return (
                f"INVERSE_{original_name}",
                f"INVERSE_{original_output_name.replace('.clf', '.ctf')}"
            )
    if '-AP1' in original_name:
        parts = original_name.replace('-AP1', '').split('_to_')
        if len(parts) == 2:
            return (
                f"ACES-AP1_to_{parts[0]}",
                f"ACES-AP1_to_{parts[0]}.ctf"
            )
        else:
            return (
                f"INVERSE_{original_name}",
                f"INVERSE_{original_output_name.replace('.clf', '.ctf')}"
            )
    return (
        f"INVERSE_{original_name}",
        f"INVERSE_{original_output_name.replace('.clf', '.ctf')}"
    )


# -------------------------------------------------------------------------- #
# Write CTF with GroupTransform
# -------------------------------------------------------------------------- #


def write_ctf_and_recipe(group_transform, output_path, recipe_data):
    """
    Writes the GroupTransform to a .ctf file and a companion .json recipe
    file.
    """
    try:
        group_transform.write(
            "Color Transform Format",
            output_path,
            config
        )
        logging.info(f"  - Successfully created CTF: {output_path}")
    except Exception as e:
        logging.error(
            f"  - Failed to write CTF {output_path}: {str(e)}"
        )
        return False

    recipe_path = os.path.splitext(output_path)[0] + '.json'
    try:
        with open(recipe_path, 'w') as f:
            json.dump(recipe_data, f, indent=2)
        logging.info(f"  - Successfully created recipe: {recipe_path}")
    except Exception as e:
        logging.error(
            f"  - Failed to write recipe {recipe_path}: {str(e)}"
        )

    return True


# -------------------------------------------------------------------------- #
# Main Processing Loop
# -------------------------------------------------------------------------- #

logging.info("Starting CTF generation...")
logging.info(f"PyOpenColorIO version: {ocio.GetVersion()}")

for root, dirs, files in os.walk(json_input_dir):
    if root == json_input_dir:
        continue

    for filename in files:
        if filename.endswith('.json'):
            json_file_path = os.path.join(root, filename)
            try:
                with open(json_file_path, 'r') as f:
                    conversion = json.load(f)
            except json.JSONDecodeError:
                logging.error(
                    f"Invalid JSON: {json_file_path}. Skipping."
                )
                continue

            conversion_name = conversion.get('name')
            output_clf_name = conversion.get('output_clf')
            inputs = conversion.get('inputs')

            if not conversion_name or not output_clf_name or not inputs:
                logging.warning(
                    f"Skipping invalid conversion task in {filename}."
                )
                continue

            relative_path = os.path.relpath(root, json_input_dir)
            ctf_output_subdirectory = os.path.join(
                output_dir,
                relative_path
            )
            os.makedirs(ctf_output_subdirectory, exist_ok=True)

            output_ctf_name = output_clf_name.replace('.clf', '.ctf')

            # --- Process Forward Transform ---
            logging.info(
                f"Processing FORWARD conversion: {conversion_name}"
            )
            forward_transforms = []
            if create_forward_transform(
                    conversion,
                    forward_transforms,
                    conversion_name):
                if forward_transforms:
                    g = ocio.GroupTransform(forward_transforms)
                    # output_ctf_name is now expected to be clean from
                    # generate_conversion_tasks.py
                    out_path = os.path.join(
                        ctf_output_subdirectory,
                        output_ctf_name
                    )
                    recipe = {
                        "output_file": output_ctf_name,
                        "source_json": os.path.basename(json_file_path),
                        "transform_direction": "forward",
                        "source_transforms": [
                            {
                                "file": os.path.basename(t.getSrc()),
                                "direction": (
                                    "inverse"
                                    if t.getDirection() ==
                                    ocio.TRANSFORM_DIR_INVERSE
                                    else "forward"
                                )
                            } for t in g
                        ]
                    }
                    write_ctf_and_recipe(g, out_path, recipe)

            # --- Process Inverse Transform ---
            inverse_name, inverse_ctf_name = generate_inverse_name(
                conversion_name,
                output_ctf_name
            )
            logging.info(
                f"Processing INVERSE conversion: {inverse_name}"
            )
            inverse_transforms = []
            if create_inverse_transform(
                    conversion,
                    inverse_transforms,
                    conversion_name):
                if inverse_transforms:
                    g = ocio.GroupTransform(inverse_transforms)
                    # inverse_ctf_name is now expected to be clean from
                    # generate_conversion_tasks.py
                    inv_path = os.path.join(
                        ctf_output_subdirectory,
                        inverse_ctf_name
                    )
                    recipe = {
                        "output_file": inverse_ctf_name,
                        "source_json": os.path.basename(json_file_path),
                        "transform_direction": "inverse",
                        "source_transforms": [
                            {
                                "file": os.path.basename(t.getSrc()),
                                "direction": (
                                    "inverse"
                                    if t.getDirection() ==
                                    ocio.TRANSFORM_DIR_INVERSE
                                    else "forward"
                                )
                            } for t in g
                        ]
                    }
                    write_ctf_and_recipe(g, inv_path, recipe)

logging.info("Processing complete. All transforms generated.")


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
