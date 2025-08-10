#!/bin/bash

# ========================================================================== #
# This section defines script info, job info & software details.
# ========================================================================== #

# Launcher Script Name:  000_abc_def-flame_first_run-juliet.sh
# Launcher Script for:   000_abc_def_2026_juliet
# Script Creation Date:  2025-05-05 21:42:43

the_projekt_name="000_abc_def"

the_projekt_flame_name="000_abc_def_2026_juliet"

flame_workstation_name="juliet"

# ========================================================================== #
# This section creates a log for the flame first run.
# ========================================================================== #

# Define the the_flame_first_run_log
the_flame_first_run_log_dir="/PROJEKTS/000_abc_def/cfg/log"
the_flame_first_run_log_name="000_abc_def-flame_first_run-juliet.log"
the_flame_first_run_log="$the_flame_first_run_log_dir/$the_flame_first_run_log_name"

# Redirect stdout and stderr to the log file
exec > >(tee -a "$the_flame_first_run_log") 2>&1

# Function to execute the command
execute_command() {
    eval "$1"
}
# -------------------------------------------------------------------------- #

# Construct the flame launch command.
launch_opt_1="/opt/Autodesk/flame_2026.pr219/bin/startFlame"
launch_opt_2="-J 000_abc_def_2026_juliet"
launch_opt_3="--start-workspace=\"$flame_workstation_name\" --create-workspace"
logik_projekt_python_dir="/opt/Autodesk/shared/python/logik_projekt"
projekt_tool_dir="projekt_tools/logik_projekt_layout/scripts"
projekt_tool_path="$logik_projekt_python_dir/$projekt_tool_dir"
launch_script="create_projekt_layout.py"
launch_opt_4="--execute-python-script=$projekt_tool_path/$launch_script"
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

# Prompt the user for confirmation.
read -rsn1 -p "  Press 'Enter' to LAUNCH FLAME | Press 'Esc' to CANCEL" key
if [ "$key" == $'\x1b' ]; then
    echo "Operation cancelled."
elif [ "$key" == $'\0a' ]; then
    execute_command "$launch_cmd"
else
    echo "Invalid key pressed. Operation cancelled."
fi

echo -e "\n\n$separator\n$separator\n$separator\n\n"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 C2 A9 32 30 32 35 #
# ========================================================================== #

# Changelist:
# -------------------------------------------------------------------------- #