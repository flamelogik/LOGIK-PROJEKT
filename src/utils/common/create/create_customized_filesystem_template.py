#!/usr/bin/env python3
# -------------------------------------------------------------------------- #
# Filename:     create_customized_filesystem_template.py
# Purpose:      Analyzes directory structure and generates configuration files.
# Description:  This script analyzes a given directory structure template and
#               generates corresponding JSON configuration files and Flame
#               bookmarks, updating site preferences accordingly.

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

import sys
import os
import json
from pathlib import Path
import logging
import platform
import shutil
import tempfile

from src.core.utils.path_utils import get_repository_root_dir

# Determine repo_dir and add to sys.path for module discovery
repo_dir = get_repository_root_dir()
sys.path.insert(0, str(repo_dir))
sys.path.insert(0, str(repo_dir.joinpath('app')))
os.environ["repo_dir"] = str(repo_dir)


# Import Qt components with error handling
try:
    from PySide6.QtWidgets import QApplication, QFileDialog
    QT_AVAILABLE = True
except ImportError:
    print("Warning: PySide6 not available. GUI file dialog will not work.")
    QT_AVAILABLE = False

# Import custom modules with error handling
try:
    from src.ui.themes.modular_dark_theme import (
        LogikProjektModularTheme
    )
    from src.utils.common.create.create_banners import (
        generate_banner_line_start
    )
    from src.utils.common.create.create_logs import (
        log_shell_script_activity
    )
    from src.utils.common.create.create_separators import (
        separator_plus
    )
    from src.utils.common.create.create_timestamp import (
        get_timestamp_variables
    )
    from src.utils.common.create.directory_structure_analysis import (
        directory_structure_analysis
    )
    from src.utils.common.create.directory_structure_to_json import (
        directory_structure_to_json
    )
    from src.utils.common.create.directory_structure_to_bookmarks import (
        directory_structure_to_bookmarks
    )
    CUSTOM_MODULES_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Custom modules not available: {e}")
    CUSTOM_MODULES_AVAILABLE = False

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Constants
CFG_DIR = "cfg"
SITE_CFG_DIR = "site-cfg"
LOGIK_PROJEKT_CFG_DIR = "logik-projekt-cfg"
LOGIK_PROJEKT_TEMPLATES_DIR = "logik-projekt-templates"
FILESYSTEM_CFG_DIR = "filesystem-templates"
PREF_DIR = "pref"
SITE_PREFS_DIR = "site-prefs"
LOGIK_PROJEKT_PREFS_DIR = "logik-projekt-prefs"
JSON_DIR_NAME = "json"
JSON_BAK_DIR_NAME = "json-bak"

# Fallback functions for when custom modules aren't available
def fallback_separator():
    """Returns a fallback separator string."""
    return "=" * 80

def fallback_banner(text):
    """Prints a fallback banner."""
    separator = fallback_separator()
    print(f"\n{separator}")
    print(f"  {text.upper()}")
    print(f"{separator}\n")

def fallback_timestamp():
    """Returns fallback timestamp variables."""
    from datetime import datetime
    now = datetime.now()
    return now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), now.strftime("%Y%m%d_%H%M%S")

def fallback_log_activity(program_name):
    """Logs fallback activity."""
    print(f"Starting {program_name}")

def initialize_environment():
    """Initializes environment variables and returns program info."""
    operating_system = platform.system()
    this_script = os.path.basename(__file__)
    program_name = os.path.splitext(this_script)[0]
    program_name_uc = program_name.upper()
  
    return operating_system, program_name, program_name_uc, repo_dir


def get_directory_via_gui(default_path):
    """Get directory using GUI file dialog with fallback to command line input."""
    if not QT_AVAILABLE:
        print(f"Default template path: {default_path}")
        chosen_folder = input("Enter the full path to your project directory template: ").strip()
        return chosen_folder if chosen_folder else None
  
    try:
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
      
        # Apply theme if available
        if CUSTOM_MODULES_AVAILABLE:
            try:
                app.setStyleSheet(LogikProjektModularTheme.get_stylesheet())
            except Exception as e:
                logging.warning(f"Could not apply theme: {e}")
      
        chosen_folder = QFileDialog.getExistingDirectory(
            None,
            "Choose a project directory template",
            default_path
        )
        return chosen_folder
    except Exception as e:
        logging.error(f"GUI dialog failed: {e}")
        print(f"Default template path: {default_path}")
        chosen_folder = input("Enter the full path to your project directory template: ").strip()
        return chosen_folder if chosen_folder else None

def _update_site_preferences(repo_dir, template_name, new_filesystem_tree_path, new_flame_workspace_path, new_flame_bookmarks_path):
    """Updates the site preferences JSON file with new project configuration."""
    site_prefs_file = Path(repo_dir) / PREF_DIR / SITE_PREFS_DIR / "logik-projekt-site-prefs.json"
    if not site_prefs_file.exists():
        logging.error(f"Error: Site preferences file not found at {site_prefs_file}")
        sys.exit(1)

    try:
        with open(site_prefs_file, 'r', encoding='utf-8') as f:
            site_prefs_data = json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON from {site_prefs_file}: {e}")
        sys.exit(1)
    except IOError as e:
        logging.error(f"Error reading file {site_prefs_file}: {e}")
        sys.exit(1)

    projekt_configurations = site_prefs_data.get("PROJEKT Configurations", [])
  
    found_entry = False
    for config in projekt_configurations:
        if config.get("PROJEKT Configuration Name") == template_name:
            config["PROJEKT Filesystem Tree"] = new_filesystem_tree_path
            config["PROJEKT Flame Workspace"] = new_flame_workspace_path
            config["PROJEKT Flame Bookmarks"] = new_flame_bookmarks_path
            found_entry = True
            break

    if not found_entry:
        new_entry = {
            "PROJEKT Configuration Name": template_name,
            "PROJEKT Filesystem Tree": new_filesystem_tree_path,
            "PROJEKT Flame Workspace": new_flame_workspace_path,
            "PROJEKT Flame Bookmarks": new_flame_bookmarks_path
        }
        projekt_configurations.append(new_entry)

    site_prefs_data["PROJEKT Configurations"] = projekt_configurations

    try:
        with open(site_prefs_file, 'w', encoding='utf-8') as f:
            json.dump(site_prefs_data, f, indent=2, ensure_ascii=False)
        logging.info(f"Updated {site_prefs_file} with configuration for '{template_name}'.")
    except IOError as e:
        logging.error(f"Error writing to {site_prefs_file}: {e}")
        sys.exit(1)

def _print_separator_line():
    """Prints a separator line to the log."""
    if CUSTOM_MODULES_AVAILABLE:
        try:
            logging.info(f"\n{separator_plus}\n")
        except Exception:
            logging.info(f"\n{fallback_separator()}\n")
    else:
        logging.info(f"\n{fallback_separator()}\n")

def _log_initial_info(program_name_uc, projekt_date, projekt_time, projekt_now):
    """Logs initial program information including banners and timestamps."""
    if CUSTOM_MODULES_AVAILABLE:
        try:
            _print_separator_line()
            generate_banner_line_start(program_name_uc)
            _print_separator_line()
        except Exception:
            fallback_banner(program_name_uc)
    else:
        fallback_banner(program_name_uc)

    logging.info(f"  date: {projekt_date}")
    logging.info(f"  time: {projekt_time}")
    logging.info(f"  now:  {projekt_now}")
  
    _print_separator_line()

def _handle_file_backups(json_file, json_file_bak, bookmarks_file, bookmarks_file_bak):
    """Handles backing up existing JSON and bookmarks files."""
    try:
        os.makedirs(os.path.dirname(json_file_bak), exist_ok=True)
        os.makedirs(os.path.dirname(bookmarks_file_bak), exist_ok=True)
    except OSError as e:
        logging.error(f"Error creating backup directories: {e}")
        return

    if os.path.isfile(json_file):
        logging.info("  json file already exists.\n")
        logging.info("  creating a backup of the existing file at:\n")
        logging.info(f"  {json_file_bak}\n")
        try:
            shutil.copy2(json_file, json_file_bak)
            logging.info("  processing a new json file.")
        except (OSError, IOError) as e:
            logging.error(f"Error backing up JSON file: {e}")
            return
      
        _print_separator_line()

    if os.path.isfile(bookmarks_file):
        logging.info("  bookmarks file already exists.\n")
        logging.info("  creating a backup of the existing file at:\n")
        logging.info(f"  {bookmarks_file_bak}\n")
        try:
            shutil.copy2(bookmarks_file, bookmarks_file_bak)
            logging.info("  processing a new bookmarks file.")
        except (OSError, IOError) as e:
            logging.error(f"Error backing up bookmarks file: {e}")
            return
      
        _print_separator_line()

def _process_directory_structure(chosen_folder, json_file, bookmarks_file):
    """Processes the chosen directory structure to generate JSON and bookmarks files."""
    if not CUSTOM_MODULES_AVAILABLE:
        logging.error("Custom modules required for directory structure processing are not available.")
        sys.exit(1)
  
    json_data_file = None
    try:
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as tmp:
            json_data_file = tmp.name

        try:
            generate_banner_line_start("analyzing directory structure")
            logging.info(f"\n{separator_plus}\n")
        except Exception:
            fallback_banner("analyzing directory structure")

        directory_structure_analysis(chosen_folder, json_data_file)
      
        try:
            logging.info(f"\n{separator_plus}\n")
            generate_banner_line_start("creating directory structure json")
            logging.info(f"\n{separator_plus}\n")
        except Exception:
            fallback_banner("creating directory structure json")

        try:
            with open(json_data_file, 'r', encoding='utf-8') as f:
                logging.info(f.read())
        except (IOError, UnicodeDecodeError) as e:
            logging.warning(f"Could not read temporary file for display: {e}")
      
        try:
            logging.info(f"\n{separator_plus}\n")
        except Exception:
            logging.info(f"\n{fallback_separator()}\n")

        directory_structure_to_json(json_data_file, json_file, chosen_folder)
        directory_structure_to_bookmarks(json_data_file, bookmarks_file, chosen_folder)

    except Exception as e:
        logging.error(f"Error processing directory structure: {e}")
        sys.exit(1)
    finally:
        if json_data_file and os.path.exists(json_data_file):
            try:
                os.unlink(json_data_file)
            except OSError as e:
                logging.warning(f"Could not delete temporary file {json_data_file}: {e}")

def _setup_output_paths_and_backups(repo_dir, new_filesystem_tree_path, new_flame_bookmarks_path, projekt_now):
    """Sets up output paths and handles backups for JSON and bookmarks files."""
    relative_json_path = new_filesystem_tree_path
    relative_bookmarks_path = new_flame_bookmarks_path

    json_file = Path(repo_dir) / relative_json_path
    bookmarks_file = Path(repo_dir) / relative_bookmarks_path

    # Ensure parent directories exist for the output files
    try:
        os.makedirs(json_file.parent, exist_ok=True)
        os.makedirs(bookmarks_file.parent, exist_ok=True)
    except OSError as e:
        logging.error(f"Error creating directories: {e}")
        sys.exit(1)

    # Construct backup paths
    json_file_bak = json_file.parent / JSON_BAK_DIR_NAME / f"{projekt_now}.{json_file.name}.bak"
    bookmarks_file_bak = bookmarks_file.parent / JSON_BAK_DIR_NAME / f"{projekt_now}.{bookmarks_file.name}.bak"

    _handle_file_backups(json_file, json_file_bak, bookmarks_file, bookmarks_file_bak)
    return json_file, bookmarks_file, json_file_bak, bookmarks_file_bak

def _copy_workspace_template(repo_dir, new_flame_workspace_path, projekt_now):
    """Copies the flame workspace template to the target directory."""
    source_file = Path(repo_dir) / "cfg/site-cfg/flame-cfg/flame-templates/flame-workspace-templates/flame-workspace-template.json"
    # Construct destination path using the directory from new_flame_workspace_path
    dest_dir = (Path(repo_dir) / new_flame_workspace_path).parent
    dest_file = dest_dir / "flame-workspace.json"

    if not source_file.is_file():
        logging.error(f"Source workspace template not found: {source_file}")
        return

    try:
        dest_dir.mkdir(parents=True, exist_ok=True)

        if dest_file.is_file():
            backup_dir = dest_dir / JSON_BAK_DIR_NAME
            backup_dir.mkdir(exist_ok=True)
            backup_file = backup_dir / f"{projekt_now}.{dest_file.name}.bak"
            logging.info(f"Backing up existing workspace file to {backup_file}")
            shutil.copy2(dest_file, backup_file)

        shutil.copy2(source_file, dest_file)
        logging.info(f"Copied workspace template to {dest_file}")

    except (IOError, OSError) as e:
        logging.error(f"Could not copy workspace template: {e}")

def main():
    """Main function to run the script."""
    operating_system, program_name, program_name_uc, repo_dir = initialize_environment()

    # Get timestamp variables with fallback
    if CUSTOM_MODULES_AVAILABLE:
        try:
            projekt_date, projekt_time, projekt_now = get_timestamp_variables()
        except Exception as e:
            logging.warning(f"Custom timestamp function failed: {e}")
            projekt_date, projekt_time, projekt_now = fallback_timestamp()
    else:
        projekt_date, projekt_time, projekt_now = fallback_timestamp()

    # Log shell script activity with fallback
    if CUSTOM_MODULES_AVAILABLE:
        try:
            log_shell_script_activity(program_name)
        except Exception as e:
            logging.warning(f"Could not log shell script activity: {e}")
            fallback_log_activity(program_name)
    else:
        fallback_log_activity(program_name)

    _log_initial_info(program_name_uc, projekt_date, projekt_time, projekt_now)

    default_template_path = os.path.join(
        repo_dir,
        CFG_DIR,
        SITE_CFG_DIR,
        LOGIK_PROJEKT_CFG_DIR,
        LOGIK_PROJEKT_TEMPLATES_DIR,
        FILESYSTEM_CFG_DIR,
    )

    chosen_folder = get_directory_via_gui(default_template_path)

    if not chosen_folder:
        logging.error("  no folder selected. exiting.")
        sys.exit(1)
    elif not os.path.isdir(chosen_folder):
        logging.error("  invalid folder selected. exiting.")
        sys.exit(1)

    chosen_folder_basename = os.path.basename(chosen_folder)
    logging.info(f"  directory structure template: {chosen_folder_basename}")
  
    _print_separator_line()

    template_name = chosen_folder_basename
    new_filesystem_tree_path = f"pref/site-prefs/custom-prefs/{template_name}/filesystem-tree.json"
    new_flame_workspace_path = f"pref/site-prefs/custom-prefs/{template_name}/flame-workspace.json"
    new_flame_bookmarks_path = f"pref/site-prefs/custom-prefs/{template_name}/cf_bookmarks.json"

    _update_site_preferences(repo_dir, template_name, new_filesystem_tree_path, new_flame_workspace_path, new_flame_bookmarks_path)


    json_file, bookmarks_file, json_file_bak, bookmarks_file_bak = _setup_output_paths_and_backups(
        repo_dir, new_filesystem_tree_path, new_flame_bookmarks_path, projekt_now
    )

    _process_directory_structure(chosen_folder, json_file, bookmarks_file)

    _copy_workspace_template(repo_dir, new_flame_workspace_path, projekt_now)

    _print_separator_line()
    logging.info("  directory structure analysis complete.")
    _print_separator_line()
  
    logging.info("  directory structure json file created at:\n")
    logging.info(f"  {json_file}")
  
    _print_separator_line()
  
    logging.info("  adsk flame bookmarks json file created at:\n")
    logging.info(f"  {bookmarks_file}")

    _print_separator_line()

    logging.info("  adsk flame workspace json file created at:\n")
    logging.info(f"  {Path(repo_dir) / new_flame_workspace_path}")
  
    _print_separator_line()


if __name__ == "__main__":
    main()


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
# C2 A9 32 30 32 35 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 #
# -------------------------------------------------------------------------- #
# Changelog:
# -------------------------------------------------------------------------- #
# Version:      0.0.1
# Modification: 2025-07-28
# Changelist: 
#   - Fixed duplicate header blocks
#   - Added error handling for missing dependencies (PySide6, custom modules)
#   - Added fallback functions for when custom modules aren't available
#   - Fixed repo_dir variable scope issues by moving logic to function
#   - Added proper exception handling for file operations
#   - Added encoding='utf-8' to file operations
#   - Fixed constant naming (uppercase)
#   - Added graceful GUI fallback to command-line input
#   - Improved error messages and logging
#   - Added QApplication instance checking
#   - Added proper cleanup for temporary files
# -------------------------------------------------------------------------- #
