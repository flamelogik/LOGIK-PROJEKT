#

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

# resources/utilities/add_scripts_to_crontab.py

# ========================================================================== #
# This section defines the import statements and path setup.
# ========================================================================== #

# Standard library imports
import os
import subprocess
import sys

# -------------------------------------------------------------------------- #

from tkinter import Tk
from tkinter.filedialog import askopenfilename

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

def get_shell_script(script_name):
    """Get the path to the shell script to be executed by cron.

    Args:
        script_name (str): The name of the shell script.

    Returns:
        str: The path to the shell script.
    """
    root = Tk()
    root.withdraw()  # Hide the root window
    script_path = askopenfilename(title=f"Select the {script_name} shell script")
    root.destroy()
    if not script_path:
        print("No file selected. Exiting.")
        sys.exit(0)
    if not os.path.isfile(script_path):
        print("Invalid file path. Please try again.")
        return get_shell_script(script_name)
    return script_path

# -------------------------------------------------------------------------- #

def get_cron_time(script_name):
    """Gets the cron time to execute the given script from the user.

    Args:
        script_name: The name of the script to be executed.

    Returns:
        The cron time in the format: "Minute Hour Day of Month Month Day of Week".
    """
    print(f"Enter the time to execute the {script_name} script in the following format:")
    print("Minute (0-59), Hour (0-23), Day of Month (1-31), Month (1-12), Day of Week (0-6, 0 is Sunday)")
    minute = input("Minute: ")
    hour = input("Hour: ")
    day_of_month = input("Day of Month: ")
    month = input("Month: ")
    day_of_week = input("Day of Week: ")
    return f"{minute} {hour} {day_of_month} {month} {day_of_week}"

# -------------------------------------------------------------------------- #

def create_crontab_entry(script_path, cron_time):
    """Adds a crontab entry to run the specified script at the specified time.

    Args:
        script_path (str): The path to the script to be run.
        cron_time (str): The cron time expression at which the script should be run.

    Returns:
        None

    Raises:
        subprocess.CalledProcessError: If the crontab command fails.

    Example:
        create_crontab_entry("/path/to/script.sh", "0 0 * * *")
    """
    cron_command = f"{cron_time} {script_path}"
    subprocess.run(f'(crontab -l; echo "{cron_command}") | crontab -', shell=True, check=True)
    print(f"Crontab entry for {script_path} created successfully.")
    user = os.getlogin()
    cron_file_location = f"/var/spool/cron/crontabs/{user}" if os.name != 'darwin' else f"/var/cron/tabs/{user}"
    print(f"Crontab file location: {cron_file_location}")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

if __name__ == "__main__":
    flame_archive_script = get_shell_script("flame_archive")
    flame_archive_time = get_cron_time("flame_archive")
    create_crontab_entry(flame_archive_script, flame_archive_time)

    projekt_backup_script = get_shell_script("projekt_backup")
    projekt_backup_time = get_cron_time("projekt_backup")
    create_crontab_entry(projekt_backup_script, projekt_backup_time)


'''
import os
import subprocess
import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def get_shell_script(script_name):
    root = Tk()
    root.withdraw()  # Hide the root window
    script_path = askopenfilename(title=f"Select the {script_name} shell script")
    root.destroy()
    if not script_path:
        print("No file selected. Exiting.")
        sys.exit(0)
    if not os.path.isfile(script_path):
        print("Invalid file path. Please try again.")
        return get_shell_script(script_name)
    return script_path

def get_cron_time(script_name):
    print(f"Enter the time to execute the {script_name} script in the following format:")
    print("Minute (0-59), Hour (0-23), Day of Month (1-31), Month (1-12), Day of Week (0-6, 0 is Sunday)")
    minute = input("Minute: ")
    hour = input("Hour: ")
    day_of_month = input("Day of Month: ")
    month = input("Month: ")
    day_of_week = input("Day of Week: ")
    return f"{minute} {hour} {day_of_month} {month} {day_of_week}"

def create_crontab_entry(script_path, cron_time):
    cron_command = f"{cron_time} {script_path}"
    subprocess.run(f'(crontab -l; echo "{cron_command}") | crontab -', shell=True, check=True)
    print(f"Crontab entry for {script_path} created successfully.")
    user = os.getlogin()
    cron_file_location = f"/var/spool/cron/crontabs/{user}" if os.name != 'darwin' else f"/var/cron/tabs/{user}"
    print(f"Crontab file location: {cron_file_location}")

if __name__ == "__main__":
    flame_archive_script = get_shell_script("flame_archive")
    flame_archive_time = get_cron_time("flame_archive")
    create_crontab_entry(flame_archive_script, flame_archive_time)

    projekt_backup_script = get_shell_script("projekt_backup")
    projekt_backup_time = get_cron_time("projekt_backup")
    create_crontab_entry(projekt_backup_script, projekt_backup_time)

'''


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
