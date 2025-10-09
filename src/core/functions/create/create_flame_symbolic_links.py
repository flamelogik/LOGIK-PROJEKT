#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     create_flame_symbolic_links.py
# Purpose:      Creates symbolic links between LOGIK-PROJEKT directories and
#               Flame project setup directories.
# Description:  This script establishes symbolic links to integrate
#               LOGIK-PROJEKT resources (scripts, presets, templates) into
#               the Flame project environment, and also links
#               iteration directories.

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

import os
import logging
import time
from src.core.utils import path_utils


# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def create_flame_symbolic_links(
    logik_projekt_path: str,
    flame_projekt_setups_dir: str,
    current_workstation: str
):
    """
    Creates symbolic links between LOGIK-PROJEKT directories and 
    Flame project setup directories.

    Args:
        logik_projekt_path (str): Absolute path to LOGIK-PROJEKT directory.
        flame_projekt_setups_dir (str): Absolute path to the 
        Flame project's 'setups' directory.
        current_workstation (str): Name of the current workstation.
    """
    logging.info("Creating symbolic links...")

    links_to_create = [
        ("scripts", "logik_scripts"),
        (
            os.path.join(
                "cfg",
                "site-cfg",
                "flame-cfg",
                "flame-presets"
            ),
            "logik_presets",
        ),
        (
            os.path.join(
                "cfg",
                "site-cfg",
                "flame-cfg",
                "flame-templates"
            ),
            "logik_templates",
        ),
    ]

    for source_relative, destination_name in links_to_create:
        source_path = os.path.join(
            path_utils.get_repository_root_dir(),
            source_relative,
        )
        destination_path = os.path.join(
            flame_projekt_setups_dir,
            destination_name,
        )

        try:
            if os.path.exists(source_path):
                if not os.path.lexists(destination_path):
                    os.symlink(source_path, destination_path)
                    logging.info(
                        f"Created symlink: {destination_path} -> {source_path}"
                    )
                else:
                    if (
                        os.path.islink(destination_path)
                        and os.readlink(destination_path) == source_path
                    ):
                        logging.info(
                            (
                                "Symlink already exists and is correct: "
                                f"{destination_path} -> {source_path}"
                            )
                        )
                    else:
                        logging.warning(
                            (
                                "Destination path already exists "
                                "and is not a symlink "
                                "to the correct source, "
                                "or is a broken symlink: "
                                f"{destination_path}. Skipping."
                            )
                        )
            else:
                logging.warning(
                    (
                        "Source path for symlink does not exist: "
                        f"{source_path}. Skipping."
                    )
                )
        except OSError as e:
            logging.error(
                (
                    f"Error creating symbolic link for {source_path} "
                    f"to {destination_path}: {e}"
                )
            )
        except Exception as e:
            logging.error(
                (
                    "An unexpected error occurred while creating symlink for "
                    f"{source_path} to {destination_path}: {e}"
                )
            )
            # Create logik_projekt_path/flame/iterations ->
            # flame_projekt_setups_dir/batch/flame/iterations
            source_path_iterations = os.path.join(
                logik_projekt_path,
                "flame",
                "iterations"
            )
            destination_path_iterations = os.path.join(
                flame_projekt_setups_dir,
                "batch",
                "flame",
                "iterations"
            )
            try:
                if os.path.exists(source_path_iterations):
                    if not os.path.lexists(destination_path_iterations):
                        os.symlink(
                            source_path_iterations,
                            destination_path_iterations
                        )
                        logging.info(
                            f"""Created symlink: {destination_path_iterations} -> "
                            f"{source_path_iterations}"""
                        )
                    else:
                        if (
                            os.path.islink(destination_path_iterations)
                            and os.readlink(destination_path_iterations)
                            == source_path_iterations
                        ):
                            logging.info(
                                (
                                    "Symlink already exists and is correct: "
                                    f"{destination_path_iterations} -> "
                                    f"{source_path_iterations}"
                                )
                            )
                        else:
                            logging.warning(
                                (
                                    "Destination path already exists and "
                                    "is not a symlink to the correct source, "
                                    "or is a broken symlink: "
                                    f"{destination_path_iterations}. "
                                    "Skipping."
                                )
                            )
                else:
                    logging.warning(
                        (
                            f"Source path for symlink does not exist: "
                            f"{source_path_iterations}. Skipping."
                        )
                    )
            except OSError as e:
                logging.error(
                    (
                        "Error creating symbolic link for "
                        f"{source_path_iterations} to "
                        f"{destination_path_iterations}: {e}"
                    )
                )
            except Exception as e:
                logging.error(
                    f"""An unexpected error occurred while creating symlink for "
                    f"{source_path_iterations} to "
                    f"{destination_path_iterations}: {e}"""
                )

            # Create flame_projekt_setups_dir ->
            # logik_projekt_path/flame/{current_workstation}/setups
            source_path_setups = flame_projekt_setups_dir
            destination_path_setups = os.path.join(
                logik_projekt_path,
                "flame",
                "setups",
                current_workstation,
                "setups",
            )

            # Ensure the parent directory of the destination exists
            destination_parent_dir = os.path.dirname(destination_path_setups)
            logging.info(
                f"  Destination parent directory: {destination_parent_dir}"
            )
            logging.info(
                f"  Destination parent directory exists: "
                f"{os.path.exists(destination_parent_dir)}"
            )
            os.makedirs(destination_parent_dir, exist_ok=True)
            logging.info("  Ensured destination parent directory exists.")

            logging.info("Attempting to create symlink for setups directory:")
            logging.info(f"  Source: {source_path_setups}")
            logging.info(f"  Destination: {destination_path_setups}")
            logging.info(
                f"  Source exists: {os.path.exists(source_path_setups)}"
            )
            logging.info(
                f"  Destination exists (lexists): "
                f"{os.path.lexists(destination_path_setups)}"
            )
            if os.path.lexists(destination_path_setups):
                logging.info(
                    f"  Destination is symlink: "
                    f"{os.path.islink(destination_path_setups)}"
                )
                if os.path.islink(destination_path_setups):
                    logging.info(
                        f"  Destination symlink points to: "
                        f"{os.readlink(destination_path_setups)}"
                    )

            max_retries = 5
            retry_delay = 0.1  # seconds
            for attempt in range(max_retries):
                try:
                    if os.path.exists(source_path_setups):
                        if not os.path.lexists(destination_path_setups):
                            os.symlink(
                                source_path_setups,
                                destination_path_setups,
                            )
                            logging.info(
                                (
                                    "Created symlink: "
                                    f"{destination_path_setups} -> "
                                    f"{source_path_setups}"
                                )
                            )
                            break  # Success, exit loop
                        else:
                            if (
                                os.path.islink(destination_path_setups)
                                and os.readlink(destination_path_setups)
                                == source_path_setups
                            ):
                                logging.info(
                                    (
                                        "Symlink already exists "
                                        "and is correct: "
                                        f"{destination_path_setups} -> "
                                        f"{source_path_setups}"
                                    )
                                )
                                break  # Success, exit loop
                            else:
                                logging.warning(
                                    (
                                        "Destination path already exists "
                                        "and is not a symlink "
                                        "to the correct source, "
                                        "or is a broken symlink: "
                                        f"{destination_path_setups}. Skipping."
                                    )
                                )
                                break  # No point in retrying if it exists
                    else:
                        logging.warning(
                            (
                                "Source path for symlink does not exist: "
                                f"{source_path_setups}. Skipping."
                            )
                        )
                        break  # No point in retrying if source doesn't exist
                except OSError as e:
                    logging.error(
                        (
                            "Error creating symbolic link for "
                            f"{source_path_setups} to "
                            f"{destination_path_setups} "
                            f"(Attempt {attempt + 1}/{max_retries}): {e}"
                        )
                    )
                    if attempt < max_retries - 1:
                        time.sleep(retry_delay)
                    else:
                        logging.error(
                            (
                                "Failed to create symlink after "
                                f"{max_retries} attempts."
                            )
                        )
                except Exception as e:
                    logging.error(
                        (
                            "An unexpected error occurred "
                            "while creating symlink for "
                            f"{source_path_setups} to "
                            f"{destination_path_setups}: {e}"
                        )
                    )
                    break  # Unexpected error, no point in retrying


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
