#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     create_projekt_pgsql_db.py
# Purpose:      Initializes a PostgreSQL database for the project.
# Description:  This script provides a placeholder for creating or connecting
#               to a PostgreSQL database for project-specific data storage.

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

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')


def create_projekt_pgsql_db(
        logik_projekt_name: str,
        logik_projekt_path: str
    ):
    """
    Initializes a PostgreSQL database for the project.

    Args:
        logik_projekt_name (str): The name of the project, to be used as 
        the database name.
        logik_projekt_path (str): The path to the LOGIK-PROJEKT directory 
        where the DB data could be stored.
    """
    logging.info(
        f"""Attempting to create PostgreSQL database
        for project '{logik_projekt_name}'...""")

    # This is a placeholder for the database creation logic.
    # PostgreSQL typically runs as a system-wide service, and creating 
    # a new database
    # requires connecting to that service with appropriate credentials.
    # An alternative for a self-contained project is to initialize 
    # a new database cluster
    # within the project path, but this is less common and more complex.

    # --- Example 1: Connecting to an existing PostgreSQL service (most common) ---
    # import psycopg2
    # from psycopg2 import sql
    # from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

    # try:
    #     # IMPORTANT: Connection details should be securely managed, not hardcoded.
    #     conn = psycopg2.connect(
    #         dbname="postgres",  # Connect to the default 'postgres' db to create a new one
    #         user="your_db_user",
    #         password="your_db_password",
    #         host="localhost",
    #         port="5432"
    #     )
    #     conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    #     cursor = conn.cursor()
    #
    #     # Use sql.Identifier to safely quote the new database name
    #     db_name = sql.Identifier(logik_projekt_name.lower()) # PGSQL names are often lowercased
    #     cursor.execute(sql.SQL("CREATE DATABASE {}").format(db_name))
    #
    #     logging.info(f"Successfully created database: {logik_projekt_name}")
    #
    # except psycopg2.errors.DuplicateDatabase:
    #     logging.warning(f"Database '{logik_projekt_name}' already exists. Skipping creation.")
    # except psycopg2.OperationalError as e:
    #     logging.error(f"Could not connect to PostgreSQL. Please ensure the service is running and credentials are correct. Error: {e}")
    # except Exception as e:
    #     logging.error(f"An unexpected error occurred during database creation: {e}")
    # finally:
    #     if 'conn' in locals() and conn:
    #         conn.close()

    # --- Example 2: Initializing a new DB cluster in the project path (advanced) ---
    # import subprocess
    #
    # db_data_path = os.path.join(logik_projekt_path, 'db_data')
    # if not os.path.exists(db_data_path):
    #     try:
    #         os.makedirs(db_data_path)
    #         # The 'initdb' command must be in the system's PATH.
    #         subprocess.run(['initdb', '-D', db_data_path], check=True, capture_output=True, text=True)
    #         logging.info(f"Successfully initialized new PostgreSQL cluster at: {db_data_path}")
    #     except FileNotFoundError:
    #         logging.error("'initdb' command not found. Is PostgreSQL installed and in your PATH?")
    #     except subprocess.CalledProcessError as e:
    #         logging.error(f"Failed to initialize database cluster. Error: {e.stderr}")
    #     except Exception as e:
    #         logging.error(f"An unexpected error occurred: {e}")
    # else:
    #     logging.warning(f"Database cluster path already exists: {db_data_path}. Skipping initialization.")

    logging.info(
        "Database creation step is currently a placeholder "
        "and has been skipped."
    )


if __name__ == "__main__":
    # Example usage for direct script execution and testing
    if len(sys.argv) != 3:
        print(
            "Usage: python create_projekt_pgsql_db.py "
            "<logik_projekt_name> <logik_projekt_path>"
        )
        sys.exit(1)

    projekt_name = sys.argv[1]
    projekt_path = sys.argv[2]

    create_projekt_pgsql_db(projekt_name, projekt_path)


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
