#!/bin/bash

# ========================================================================== #
# This section defines script info, job info & software details.
# ========================================================================== #

# Launcher Script Name:  LauncherScriptName
# Launcher Script for:   LauncherScriptProjekt
# Script Creation Date:  ScriptCreationDate

the_projekt_name="LogikProjektName"

the_projekt_flame_name="LogikProjektFlameName"

flame_workstation_name="FlameWorkstationName"

# ========================================================================== #
# This section creates a log for the flame first run.
# ========================================================================== #

# Define the the_flame_first_run_log
the_flame_first_run_log_dir="LogikProjektDirectory/cfg/log"
the_flame_first_run_log_name="FlameFirstRunName"
the_flame_first_run_log="$the_flame_first_run_log_dir/$the_flame_first_run_log_name"

# Redirect stdout and stderr to the log file
exec > >(tee -a "$the_flame_first_run_log") 2>&1

# Function to execute the command
execute_command() {
    eval "$1"
}
# -------------------------------------------------------------------------- #

# Construct the flame launch command.
launch_opt_1="/opt/Autodesk/FlameSoftwareVersion/bin/startFlame"
launch_opt_2="-J LogikProjektFlameName"
launch_opt_3="--start-workspace=\"$flame_workstation_name\" --create-workspace"
# logik_projekt_python_dir="/opt/Autodesk/shared/python/logik_projekt"
# projekt_tool_dir="projekt_tools/logik_projekt_layout/scripts"
# projekt_tool_path="$logik_projekt_python_dir/$projekt_tool_dir"
# launch_script="create_projekt_layout.py"
uppercut_python_dir="/opt/Autodesk/shared/python"
projekt_tool_dir="uc_project_starter"
projekt_tool_path="$uppercut_python_dir/$projekt_tool_dir"
launch_script="uc_projekt_starter.py"
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
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:
# -------------------------------------------------------------------------- #