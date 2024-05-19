#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_03-banners.sh
# Version:          2.1.4
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-05-18
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program contains function(s) that are used to
#                   create new logik projekts.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines title_01 and banner_01.
# ========================================================================== #

# Define variables for the decorative lines that get printed to the shell.
title_01="LOGIK PROJEKT CONFIGURATION"
banner_01="$title_01 STARTED"
end_title_01="$title_01 COMPLETED"
end_banner_01=$(generate_end_title_line "$end_title_01")

# ========================================================================== #
# This section defines title_02 and banner_02.
# ========================================================================== #

# Define variables for the decorative lines that get printed to the shell.
title_02="OS & FLAME INSTALLATIONS"
banner_02="CHECK $title_02"
end_title_02="$title_02 CHECK COMPLETED"
end_banner_02=$(generate_end_title_line "$end_title_02")

# ========================================================================== #
# This section defines title_03 and banner_03.
# ========================================================================== #

# Define variables for the decorative lines that get printed to the shell.
title_03="NEW LOGIK FLAME PROJEKT"
banner_03="CREATE A $title_03"
end_title_03="$title_03 CREATION COMPLETED"
end_banner_03=$(generate_end_title_line "$end_title_03")

# ========================================================================== #
# This section defines title_04 and banner_04.
# ========================================================================== #

# Define variables for the decorative lines that get printed to the shell.
title_04="JOBS DIRECTORY"
banner_04="CONFIRM THE $title_04"
end_title_04="$title_04 CONFIRMED"
end_banner_04=$(generate_end_title_line "$end_title_04")

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

# -------------------------------------------------------------------------- #

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
