#!/usr/bin/env python3

'''
File Name:        function_05_environment.py
Version:          2.1.5
Language:         Python script
Flame Version:    2025.x
Author:           Phil MAN - phil_man@mac.com
Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
Modified:         2024-05-18
Modifier:         Phil MAN - phil_man@mac.com

Description:      This program contains function(s) that are used to
                  create new logik projekts.

Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
                  e.g. '/home/$USER/workspace/GitHub'

Changelist:       The full changelist is at the end of this document.
'''

import os
import platform
import pwd
import grp
import subprocess
import getpass

# ========================================================================== #
# This section defines global variables.
# ========================================================================== #

operating_system = ""
workstation_name = ""
current_user = ""
primary_group = ""
all_groups = ""
other_groups = ""
user_home = ""

shell_type = ""
rc_filename = ""
rc_filepath = ""

# ========================================================================== #
# This section defines functions to gather environment information.
# ========================================================================== #

def get_operating_system():
    global operating_system
    operating_system = platform.system()

# -------------------------------------------------------------------------- #

def get_workstation_name():
    global workstation_name
    if operating_system == "Linux":
        workstation_name = subprocess.getoutput("hostname -s")
    elif operating_system == "Darwin":
        workstation_name = subprocess.getoutput("scutil --get ComputerName")

# -------------------------------------------------------------------------- #

def get_current_user():
    global current_user
    current_user = getpass.getuser()

# -------------------------------------------------------------------------- #

def get_primary_group():
    global primary_group
    primary_group = grp.getgrgid(os.getgid()).gr_name

# -------------------------------------------------------------------------- #

def get_all_groups():
    global all_groups
    all_groups = ','.join(grp.getgrgid(g).gr_name for g in os.getgroups())

# -------------------------------------------------------------------------- #

def get_other_groups():
    global other_groups
    other_groups = ','.join(group for group in all_groups.split(',') if group != primary_group)

# -------------------------------------------------------------------------- #

def get_user_home():
    global user_home
    user_home = os.path.expanduser("~")

# -------------------------------------------------------------------------- #

def get_shell_type():
    global shell_type
    shell = os.environ.get('SHELL', '')
    if 'bash' in shell:
        shell_type = 'bash'
    elif 'zsh' in shell:
        shell_type = 'zsh'
    else:
        shell_type = 'unknown'

# -------------------------------------------------------------------------- #

def get_rc_filename():
    global rc_filename
    if operating_system == "Linux" and shell_type == "bash":
        rc_filename = ".bashrc"
    elif operating_system == "Darwin" and shell_type == "zsh":
        rc_filename = ".zprofile"
    else:
        rc_filename = ".rc"

# -------------------------------------------------------------------------- #

def get_rc_filepath():
    global rc_filepath
    rc_filepath = os.path.join(user_home, rc_filename)

# ========================================================================== #
# This section defines functions to parse environment information.
# ========================================================================== #

def get_base_name(file):
    return os.path.basename(file)

# -------------------------------------------------------------------------- #

def get_full_path(file):
    return os.path.realpath(file)

# -------------------------------------------------------------------------- #

def get_directory_name(file):
    return os.path.dirname(os.path.realpath(file))

# -------------------------------------------------------------------------- #

def create_alias(alias_name, alias_path):
    if not os.path.isfile(rc_filepath):
        with open(rc_filepath, 'w') as f:
            pass
    with open(rc_filepath, 'r+') as f:
        content = f.read()
        if f"alias {alias_name}=" not in content:
            f.write(f"\n# Alias for {alias_name}\nalias {alias_name}=\"{alias_path}\"\n")

# -------------------------------------------------------------------------- #

def set_permissions(file):
    os.chmod(file, 0o600)

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

def initialize_environment():
    get_user_home()
    get_shell_type()
    get_rc_filename()
    get_rc_filepath()

    if not os.path.isfile(rc_filepath):
        with open(rc_filepath, 'w') as f:
            pass
        set_permissions(rc_filepath)

    create_alias("projekt", "/path/to/projekt")

# -------------------------------------------------------------------------- #

def gather_system_info():
    get_operating_system()
    get_workstation_name()
    get_current_user()
    get_primary_group()
    get_all_groups()
    get_other_groups()

# -------------------------------------------------------------------------- #

def print_system_info():
    separator = "=" * 50
    print(f"  current user:        {current_user}")
    print(f"  primary group:       {primary_group}")
    print(f"  all groups:          {all_groups}")
    print(f"  other groups:        {other_groups}\n{separator}\n")
    print(f"  operating system:    {operating_system}\n{separator}\n")
    print(f"  workstation name:    {workstation_name}\n{separator}\n")
    print(f"  user home:           {user_home}")
    print(f"  shell type:          {shell_type}")
    print(f"  .rc filename:        {rc_filename}\n{separator}\n")

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

def main():
    initialize_environment()
    gather_system_info()
    print_system_info()

if __name__ == "__main__":
    main()

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

# -------------------------------------------------------------------------- #
'''
# Disclaimer:       This program is part of LOGIK-PROJEKT.
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
'''
# -------------------------------------------------------------------------- #
# Changelist:       
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-04-20 - 16:20:00
# comments:              refactored monolithic program into separate functions
# -------------------------------------------------------------------------- #
# version:               2.0.0
# modified:              2024-04-29 - 11:29:27
# comments:              testing production readiness
# -------------------------------------------------------------------------- #
# version:               2.0.1
# modified:              2024-04-30 - 07:06:00
# comments:              Removed 'declare -g' statements for macOS compatibility
# -------------------------------------------------------------------------- #
# version:               2.0.2
# modified:              2024-04-30 - 12:29:07
# comments:              added 'umask 0' statements for rsync commands
# -------------------------------------------------------------------------- #
# version:               2.0.3
# modified:              2024-05-03 - 10:16:09
# comments:              Restored CamelCase keys for projekt_metadata_xml_file
# -------------------------------------------------------------------------- #
# version:               2.0.4
# modified:              2024-05-03 - 10:56:34
# comments:              Restore 'jobs_dir' to /JOBS
# -------------------------------------------------------------------------- #
# version:               2.1.4
# modified:              2024-05-18 - 18:00:11
# comments:              Added GNU GPLv3 Disclaimer.
# -------------------------------------------------------------------------- #
# version:               2.1.5
# modified:              2024-05-18 - 18:45:00
# comments:              Minor modification to Disclaimer.
