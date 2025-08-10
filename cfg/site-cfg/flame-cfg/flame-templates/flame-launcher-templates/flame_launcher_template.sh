#!/bin/bash

# ========================================================================== #
# This section defines script info, job info & software details.
# ========================================================================== #

# Launcher Script Name:  %%LAUNCHER_SCRIPT_NAME%%
# Launcher Script for:   %%LAUNCHER_SCRIPT_PROJEKT%%
# Script Creation Date:  %%SCRIPT_CREATION_DATE%%

the_projekt_name="%%LOGIK_PROJEKT_NAME%%"

the_projekt_flame_name="%%FLAME_PROJEKT_NAME%%"

flame_workstation_name="%%CURRENT_WORKSTATION%%"

# ========================================================================== #
# This section creates a log for the flame first run.
# ========================================================================== #

# Define the the_flame_first_run_log
the_flame_first_run_log_dir="%%LOGIK_PROJEKT_PATH%%/cfg/log"
mkdir -p "$the_flame_first_run_log_dir"
the_flame_first_run_log_name="%%FLAME_FIRST_RUN_NAME%%"
the_flame_first_run_log="$the_flame_first_run_log_dir/$the_flame_first_run_log_name"

# Redirect stdout and stderr to the log file
exec > >(tee -a "$the_flame_first_run_log") 2>&1

# Function to execute the command
execute_command() {
    eval "$1"
}
# -------------------------------------------------------------------------- #

# Construct the flame launch command.
launch_opt_1="/opt/Autodesk/%%FLAME_SOFTWARE_CHOICE%%/bin/%%APPLICATION_STARTER%%"
launch_opt_2="-J %%FLAME_PROJEKT_NAME%%"
launch_opt_3="--start-workspace=\"%%CURRENT_WORKSTATION%%\" --create-workspace"
# logik_projekt_python_dir="/opt/Autodesk/shared/python/logik_projekt"
# projekt_tool_dir="projekt_tools/logik_projekt_layout/scripts"
# projekt_tool_path="$logik_projekt_python_dir/$projekt_tool_dir"
# launch_script="create_projekt_layout.py"
# launch_opt_4="--execute-python-script=$projekt_tool_path/$launch_script"

flame_startup_script_dir="%%FLAME_PROJEKT_SETUPS_DIR%%"
launch_script="%%FLAME_STARTUP_SCRIPT_PY%%"
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