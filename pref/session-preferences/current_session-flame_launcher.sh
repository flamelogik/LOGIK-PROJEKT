#!/bin/bash

# ========================================================================== #
# This section defines script info, job info & software details.
# ========================================================================== #

# Launcher Script Name:  %%LAUNCHER_SCRIPT_NAME%%
# Launcher Script for:   baseer_film_2026_1_rome
# Script Creation Date:  2025-10-13 13:37:09

the_projekt_name="baseer_film"

the_projekt_flame_name="baseer_film_2026_1_rome"

flame_workstation_name="rome"

# ========================================================================== #
# This section creates a log for the flame first run.
# ========================================================================== #

# Define the the_flame_first_run_log
the_flame_first_run_log_dir="/PROJEKTS/baseer_film/cfg/log"
mkdir -p "$the_flame_first_run_log_dir"
the_flame_first_run_log_name="current_session-flame_launcher.log"
the_flame_first_run_log="$the_flame_first_run_log_dir/$the_flame_first_run_log_name"

# Redirect stdout and stderr to the log file
exec > >(tee -a "$the_flame_first_run_log") 2>&1

# Function to execute the command
execute_command() {
    eval "$1"
}
# -------------------------------------------------------------------------- #

# Construct the flame launch command.
launch_opt_1="/opt/Autodesk/flame_2026.1/bin/startFlame"
launch_opt_2="-J baseer_film_2026_1_rome"
launch_opt_3="--start-workspace=\"rome\" --create-workspace"
# logik_projekt_python_dir="/opt/Autodesk/shared/python/logik_projekt"
# projekt_tool_dir="projekt_tools/logik_projekt_layout/scripts"
# projekt_tool_path="$logik_projekt_python_dir/$projekt_tool_dir"
# launch_script="create_projekt_layout.py"
# launch_opt_4="--execute-python-script=$projekt_tool_path/$launch_script"

flame_startup_script_dir="/Volumes/flame_projekts/baseer_film_2026_1_rome/setups"
launch_script="scripts/startup/flame_startup_script.py"
launch_opt_4="--execute-python-script=$flame_startup_script_dir/$launch_script"
launch_opt_5="--debug"
launch_cmd="$launch_opt_1 $launch_opt_2 $launch_opt_3 $launch_opt_4"

# -------------------------------------------------------------------------- #

# Echo the commands to the shell
echo -e "  Flame can now be launched with the following options:"
echo -e "\n$separator\n"
echo -e "  $launch_opt_1"
echo -e "   $launch_opt_2"
echo -e "   $launch_opt_3"
echo -e "   $launch_script"
# echo -e "   $launch_opt_5"
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

# # Prompt the user for confirmation.
# read -rsn1 -p "  Press 'Enter' to LAUNCH FLAME | Press 'Esc' to CANCEL" key
# if [ "$key" ==

echo -e "\n\n$separator\n$separator\n$separator\n\n"

# -------------------------------------------------------------------------- #

execute_command "$launch_cmd"

echo -e "\n\n$separator\n$separator\n$separator\n\n"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:
# -------------------------------------------------------------------------- #