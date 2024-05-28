#!/usr/bin/env python3

# -------------------------------------------------------------------------- #
'''
# Program Name:     create_logik_projekts.py
# Version:          2.1.5
# Language:         Python 3
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-05-18
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program determines system information and collects
#                   user input to create new logik projekts.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.
'''
# -------------------------------------------------------------------------- #

import os
import sys
import logging

from datetime import datetime

from PySide6.QtWidgets import (
    QApplication, 
    QComboBox, 
    QFileDialog, 
    QLabel, 
    QLineEdit, 
    QMessageBox,
    QPushButton, 
    QTextEdit,
    QVBoxLayout, 
    QWidget, 
)

from PySide6.QtGui import (
    QFont, 
    QScreen,
)

# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Define functions_dir
functions_dir = os.path.join(current_dir, "modules", "functions")

# Add the functions directory to the Python path
sys.path.append(functions_dir)

# ========================================================================== #
# This section enables debugging.
# ========================================================================== #

# Initiate script logging for debugging
def setup_logging(*args, **kwargs):
    script_name = os.path.basename(__file__)
    script_path = os.path.dirname(os.path.realpath(__file__))
    
    script_name_without_extension = os.path.splitext(script_name)[0]
    script_directory = os.path.dirname(script_path)
    log_directory = os.path.join(script_directory, 'log')

    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_filename = f"{datetime.now().strftime('%Y-%m-%d-%H-%M')}_{script_name}.debug.log"
    log_filepath = os.path.join(log_directory, log_filename)
    print("Log filepath:", log_filepath)  # Add this line for debugging
    
    # Configure logging to output to both console and file
    logging.basicConfig(filename=log_filepath, level=logging.DEBUG, *args, **kwargs)

    # Create a handler for stdout and stderr
    stdout_handler = logging.StreamHandler(sys.stdout)
    stderr_handler = logging.StreamHandler(sys.stderr)

    # Add handlers to root logger
    logging.getLogger().addHandler(stdout_handler)
    logging.getLogger().addHandler(stderr_handler)

    # Log messages
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

# ========================================================================== #
# This section identifies and locates this script when executed.
# ========================================================================== #

# Get the base name of the script
script_name = os.path.basename(__file__)

# Get the full path to the script
script_path = os.path.dirname(os.path.realpath(__file__))

# Change directory to script_path
os.chdir(script_path)

# Construct the full path to the script
alias_path = os.path.join(script_path, script_name)

# Call setup_logging to initiate logging
setup_logging()

# ========================================================================== #
# This section sources functions to create text separators.
# ========================================================================== #

from modules.functions.function_01_separators import (
    separator,
    separator_hash,
    repeat_char,
    make_line_79_chars,
    generate_title_line,
    generate_end_title_line,
)

# ========================================================================== #
# This section sources date functions and variables.
# ========================================================================== #

from modules.functions.function_02_date import *

# ========================================================================== #
# This section sources title and banner functions.
# ========================================================================== #

from modules.functions.function_03_banners import *

# ========================================================================== #
# This section sources projekt setup and logging functions.
# ========================================================================== #

from modules.functions.function_04_setup import (
    setup_logik_projekt
)

# ========================================================================== #
# This section sources user, group and environment information.
# ========================================================================== #

from modules.functions.function_05_environment import *

# ========================================================================== #
# This section analyzes the flame family software installations.
# ========================================================================== #

from modules.functions.function_06_adsk_info import *

# ========================================================================== #
# This section gathers logik projekt name info.
# ========================================================================== #

from modules.functions.function_07_projekt_name import *

# ========================================================================== #
# This section gathers logik projekt resolution info.
# ========================================================================== #

from modules.functions.function_08_projekt_resolution import *

# ========================================================================== #
# This section gathers logik projekt bit-depth info.
# ========================================================================== #

from modules.functions.function_09_projekt_depth import *

# ========================================================================== #
# This section gathers logik projekt framerate info.
# ========================================================================== #

from modules.functions.function_10_projekt_framerate import *

# ========================================================================== #
# This section gathers logik projekt color science info.
# ========================================================================== #

from modules.functions.function_11_projekt_color_science import *

# ========================================================================== #
# This section gathers logik projekt start frame info.
# ========================================================================== #

from modules.functions.function_12_projekt_start_frame import *

# ========================================================================== #
# This section gathers logik projekt metadata into an xml file.
# ========================================================================== #

from modules.functions.function_13_projekt_summary import *

# ========================================================================== #
# This section sets commonly used options for rsync.
# ========================================================================== #

from modules.functions.function_14_rsync_options import *

# ========================================================================== #
# This section uses wiretap_create_node to create a flame projekt.
# ========================================================================== #

from modules.functions.function_15_projekt_flame import *

# ========================================================================== #
# This section creates directories in a new logik projekt.
# ========================================================================== #

from modules.functions.function_16_projekt_flame_dirs import *

# ========================================================================== #
# This section creates logik projekt job directories.
# ========================================================================== #

from modules.functions.function_17_job_dirs import *

# ========================================================================== #
# This section synchronizes flame presets to the logik projekt.
# ========================================================================== #

from modules.functions.function_18_sync_batch import *

from modules.functions.function_19_sync_mediaimport import *

from modules.functions.function_20_sync_bookmarks import *

from modules.functions.function_21_sync_overlays import *

from modules.functions.function_22_sync_python import *

from modules.functions.function_23_sync_io import *

from modules.functions.function_24_sync_col_policies import *

from modules.functions.function_25_sync_col_transforms import *

# ========================================================================== #
# This section adds a color management policy to the new logik projekt.
# ========================================================================== #

from modules.functions.function_26_add_color_policy import *

# ========================================================================== #
# This section creates links to the logik projekt setup directories.
# ========================================================================== #

from modules.functions.function_27_link_setup_dirs import *

# ========================================================================== #
# This section backs up the logs and metadata files and templates.
# ========================================================================== #

from modules.functions.function_28_backup_logs import *

# ========================================================================== #
# This section creates a flame archiving script for the logik projekt.
# ========================================================================== #

from modules.functions.function_29_create_archive_script import *

# ========================================================================== #
# This section creates a backup script for the logik projekt.
# ========================================================================== #

from modules.functions.function_30_create_backup_script import *

# ========================================================================== #
# This section utilizes all previous functions.
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Function to create directories, files and logs for logik projekt setup
setup_logik_projekt(script_path, operating_system)

# # -------------------------------------------------------------------------- #

# # Redirect stdout and stderr to the log file
# import sys
# log_file = open(projekt_creation_log_file, 'a')
# sys.stdout = sys.stderr = log_file

# # -------------------------------------------------------------------------- #

# # Display banner_01 and a separator.
# print(f"\n{generate_title_line(banner_01)}\n")
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# get_environment()

# # -------------------------------------------------------------------------- #

# print(f"  from template:       {has_projekt_setup_template}")
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# print(f"  current date:        {today}")
# print(f"  current time:          {now_h_m_s}")
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# print(f"  current user:        {current_user}")
# print(f"  primary group:       {primary_group}")
# # print(f"  all groups:          {all_groups}")
# print(f"  other groups:        {other_groups}")
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# print(f"  user home:           {user_home}")
# print(f"  shell type:          {shell_type}")
# # print(f"  .rc filename:        {rc_filename}")
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# # Display a separator
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# # ========================================================================== #
# # This section displays operating system & flame installation information.
# # ========================================================================== #

# # Display banner_02 and a separator.
# print(f"\n{generate_title_line(banner_02)}\n")
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# print(f"  workstation name:    {workstation_name}")
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# print(f"  operating system:    {operating_system}")
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# # Initialize flame family software variables.
# initialize_adsk_variables()

# # Check for flame family software.
# check_adsk_installations()

# # Process the flame family software installations.
# process_adsk_installations()

# # Display sorted flame directories.
# display_sorted_dir_names()

# # Display maximum flame values.
# display_calculated_flame_info()

# # -------------------------------------------------------------------------- #

# # Display a separator
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #
# # ========================================================================== #
# # This section displays logik projekt information.
# # ========================================================================== #

# # Display banner_03 and a separator.
# print(f"\n{generate_title_line(banner_03)}\n")
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# print(f"  script name:         {script_name}")
# # print(f"  script path:         {script_path}")
# # print(f"  alias path:          {alias_path}")
# # print(f"  functions dir:       {functions_dir}")
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# print(f"  creation log:        {os.path.basename(projekt_creation_log_file)}")
# print(f"  setup file:          {os.path.basename(projekt_setup_file)}")
# print(f"  setup template:      {os.path.basename(projekt_setup_template)}")
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# gather_projekt_name()
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# gather_projekt_resolution()
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# gather_projekt_depth()
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# gather_projekt_framerate()
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# gather_projekt_color_science()
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# gather_projekt_start_frame()
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# # # Create directories
# # create_metadata_directories()

# # Set metadata
# set_projekt_metadata()

# # # Summarize metadata
# summarize_projekt_metadata()

# # Write metadata to file
# write_projekt_metadata()
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# print(f"  rsync options:       {sync_opts}")
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# create_wiretap_projekt()
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# create_flame_projekt_directories()
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# create_projekt_job_directories()
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# sync_batch_project_bins()

# sync_mediaImport_rules()

# sync_bookmarks()

# sync_overlays()

# sync_python_scripts()

# sync_io_presets()

# sync_color_policies()

# sync_color_transforms()

# # -------------------------------------------------------------------------- #

# add_syncolor_policy()

# # -------------------------------------------------------------------------- #

# remove_old_links()

# print("  older symbolic links removed.")
# print(f"\n{separator}\n")

# # Call the function to create symbolic links
# create_links()

# print("  Symbolic links created.")
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# create_archive_script()

# # -------------------------------------------------------------------------- #

# create_backup_script()

# # -------------------------------------------------------------------------- #

# backup_projekt_xml()
# backup_projekt_setup_file()
# backup_projekt_setup_template()

# # ========================================================================== #
# # This section echoes end_banner03.
# # ========================================================================== #

# # -------------------------------------------------------------------------- #

# # Display the end_title line.
# print(f"{end_banner_03}\n")
# print(f"\n\n{separator}\n{separator}\n{separator}\n\n")

# # -------------------------------------------------------------------------- #

# # Backup creation log
# backup_creation_log()

# # -------------------------------------------------------------------------- #

# # ========================================================================== #
# # This section starts flame with the new project and a new workspace.
# # ========================================================================== #

# # Define the flame_log
# flame_log_dir = tgt_configs_workstation_dir
# flame_log_name = f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-flame_first_run_{workstation_name}.log"
# flame_log = os.path.join(flame_log_dir, flame_log_name)

# # Redirect stdout and stderr to the log file
# flame_log_file = open(flame_log, 'a')
# sys.stdout = sys.stderr = flame_log_file

# # Function to execute the command
# def execute_command(command):
#     os.system(command)

# # -------------------------------------------------------------------------- #

# # Construct the flame launch command.
# launch_opt_1 = f"/opt/Autodesk/{max_dir_name}/bin/startFlame"
# launch_opt_2 = f"-J {name}"
# launch_opt_3 = f"--start-workspace={workstation_name} --create-workspace"
# logik_projekt_python_dir = "/opt/Autodesk/shared/python/logik_projekt"
# projekt_tool_dir = "projekt_tools/logik_projekt_layout/scripts"
# projekt_tool_path = os.path.join(logik_projekt_python_dir, projekt_tool_dir)
# launch_script = "create_projekt_layout.py"
# launch_opt_4 = f"--execute-python-script={os.path.join(projekt_tool_path, launch_script)}"
# launch_opt_5 = "--debug"
# launch_cmd = f"{launch_opt_1} {launch_opt_2} {launch_opt_3} {launch_opt_4}"

# # -------------------------------------------------------------------------- #

# # Echo the commands to the shell
# print("  Flame can now be launched with the following options:")
# print(f"\n{separator}\n")
# print(f"  {launch_opt_1}")
# print(f"   {launch_opt_2}")
# print(f"   {launch_opt_3}")
# print(f"   {launch_script}")
# # print(f"   {launch_opt_5}")
# print(f"\n{separator}\n")

# # -------------------------------------------------------------------------- #

# # Prompt the user for confirmation.
# key = input("  Press 'Enter' to LAUNCH FLAME | Press 'Esc' to CANCEL")
# if key == "":
#     execute_command(launch_cmd)
# else:
#     print("Operation cancelled.")

# print(f"\n\n{separator}\n{separator}\n{separator}\n\n")
