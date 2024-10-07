#!/bin/bash

# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 man-made-mekanyzms
                
#                   LOGIK-PROJEKT creates directories, files, scripts & tools
#                   for use with Autodesk Flame and other software.

#                   LOGIK-PROJEKT is free software.

#                   You can redistribute it and/or modify it under the terms
#                   of the GNU General Public License as published by the
#                   Free Software Foundation, either version 3 of the License,
#                   or any later version.
 
#                   This program is distributed in the hope that it will be
#                   useful, but WITHOUT ANY WARRANTY; without even the
#                   implied warranty of MERCHANTABILITY or FITNESS FOR A
#                   PARTICULAR PURPOSE.

#                   See the GNU General Public License for more details.

#                   You should have received a copy of the GNU General
#                   Public License along with this program.

#                   If not, see <https://www.gnu.org/licenses/>.
                
#                   Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #
# File Name:        backup_crontab_template.sh
# Version:          1.0.2
# Created:          2024-01-19
# Modified:         2024-10-07
# -------------------------------------------------------------------------- #

# Archive Script Details
the_projekt_name="LogikProjektName"
the_projekt_flame_name="LogikProjektFlameName"
flame_workstation_name="FlameWorkstationName"

# Define paths
backup_script_path="LogikProjektDirectories/LogikProjektDirectory/backup/backup_scripts/FlameWorkstationName/BackupScriptName" 
backup_script_cron_log_dir="LogikProjektDirectories/LogikProjektDirectory/backup/backup_scripts/FlameWorkstationName/cron_log"

# Inform the user about the shell script and log path
echo -e "\n  Shell script to be scheduled:\n\n  $backup_script_path\n\n"
echo -e "# ---------------------------------------------------------------- #\n"
echo -e "  Cron activity will be logged to a new log file each time.\n"
echo -e "# ---------------------------------------------------------------- #\n"

# Function to check if the script is already running
check_if_running() {
    if pgrep -f "$backup_script_path" > /dev/null; then
        echo "Script $backup_script_path is already running. Exiting."
        exit 1
    fi
}

# Display explanatory text about cron format
echo -e "  Cron is a utility that allows you to schedule tasks.\n"
echo -e "  It is useful for automating repetitive tasks, such as backups,\n"
echo -e "  maintenance, and other system tasks.\n\n"
echo -e "  Crontab defines the schedule using five fields:\n"
echo -e "  minute, hour, day of the month, month, and day of the week.\n"
echo -e "  Each field can be a value, a range of values, or a wildcard (*).\n"
echo -e "# ---------------------------------------------------------------- #\n"

echo -e "  Here is the format of a crontab entry:\n"
echo -e "  *     *     *     *     *      command/script.sh >> logfile.log"
echo -e "  │     │     │     │     │"
echo -e "  │     │     │     │     └────  Day of the Week (0-6)"
echo -e "  │     │     │     │"
echo -e "  │     │     │     └──────────  Month of the Year (1-12)"
echo -e "  │     │     │"
echo -e "  │     │     └────────────────  Day of the Month (1-31)"
echo -e "  │     │"
echo -e "  │     └──────────────────────  Hour (0-23)"
echo -e "  │"
echo -e "  └────────────────────────────  Minute (0-59)\n"

echo -e "# ---------------------------------------------------------------- #\n"

# Display example cron values and examples
echo -e "  Here are some example values:\n"
echo -e "  Field                    Value         Description"
echo -e "# ---------------------------------------------------------------- #"
echo -e "  Day of the Week          0,6           Sunday, Saturday"
echo -e "  Month of the Year        */2           Every even numbered month"
echo -e "  Day of the Month         1-31          Every day of the month"
echo -e "  Hour                     3-6           3 AM to 6 AM"
echo -e "  Minute                   */5           Every 5 minutes\n"
echo -e "# ---------------------------------------------------------------- #\n"

echo -e "  Examples:\n"
echo -e "   */5 * * * *  - Every 5 minutes"
echo -e "  */30 * * * *  - Every 30 minutes"
echo -e "     0 * * * *  - Once per hour"
echo -e "     0 0 * * *  - Every day at midnight"
echo -e "     0 6 * * 0  - Every Sunday at 06:00\n\n"

echo -e "# ---------------------------------------------------------------- #\n\n"
echo -e "  Enter your values separated by spaces:\n"

# Prompt the user for the cron schedule
read -p "  Enter your cron schedule (e.g., */5 * * * *): " cron_time

# Function to create crontab entry
create_crontab_entry() {
    local cron_time=$1
    local script_path=$2
    local log_dir=$3

    # Generate a new log file name with the format: YYYY_MM_DD-HH_MM_LogikProjektName_cron_log.log
    cron_command="$cron_time $script_path >> $log_dir/$(date +'%Y_%m_%d-%H_%M')_${the_projekt_name}_cron_log.log 2>&1"
    
    # Get existing crontab entries, append the new one, and apply it
    (crontab -l 2>/dev/null; echo "$cron_command") | crontab -
    
    echo -e "\nCrontab entry for $script_path created successfully."
    echo -e "Each cron activity will be logged to a new file in: $log_dir"
}

# Call the function to add the cron job if a valid input is provided
if [[ -n "$cron_time" ]]; then
    mkdir -p "$backup_script_cron_log_dir"
    create_crontab_entry "$cron_time" "$backup_script_path" "$backup_script_cron_log_dir"
else
    echo "Please enter a valid cron schedule."
fi

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:       

# -------------------------------------------------------------------------- #
# version:          0.0.1
# created:          2024-01-19 - 12:34:56
# comments:         scripts to create flame projekts, presets & templates.
# -------------------------------------------------------------------------- #
# version:          0.1.0
# modified:         2024-04-20 - 16:20:00
# comments:         refactored monolithic program into separate functions.
# -------------------------------------------------------------------------- #
# version:          0.5.0
# modified:         2024-05-24 - 20:24:00
# comments:         merged flame_colortoolkit with projekt.
# -------------------------------------------------------------------------- #
# version:          0.6.0
# modified:         2024-05-25 - 15:00:03
# comments:         started conversion to python3.
# -------------------------------------------------------------------------- #
# version:          0.7.0
# modified:         2024-06-21 - 18:21:03
# comments:         started gui design with pyside6.
# -------------------------------------------------------------------------- #
# version:          0.9.9
# created:          2024-09-09 - 10:38:56
# comments:         added launchd option and removal script.
# -------------------------------------------------------------------------- #
# version:          1.0.0
# created:          2024-09-09 - 18:38:56
# comments:         created GUI and reverted to cron.
# -------------------------------------------------------------------------- #
# version:          1.0.1
# created:          2024-10-06 - 09:08:00
# comments:         fixed bug to create_log_dir.
# -------------------------------------------------------------------------- #
# version:          1.0.2
# created:          2024-10-07 - 10:26:00
# comments:         changed log to a dated log to prevent file ballooning.
# -------------------------------------------------------------------------- #
