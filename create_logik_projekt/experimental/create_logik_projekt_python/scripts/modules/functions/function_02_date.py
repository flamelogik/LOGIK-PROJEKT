#!/usr/bin/env python3

'''
File Name:        function_02-date.py
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

from datetime import datetime, timedelta

# ========================================================================== #
# This section defines variables based on the date.
# ========================================================================== #

# Current Date & Time Options
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
today = datetime.now().strftime("%Y-%m-%d")
yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

# -------------------------------------------------------------------------- #

# Current Date and Time Options
now_h_m_s = datetime.now().strftime("%H:%M:%S")
now_h_m = datetime.now().strftime("%H-%M")
today_now = datetime.now().strftime("%F_%H-%M")
TODAY = today
NOW = now_h_m_s

# NOW_DATE = datetime.now().strftime("%F")
# NOW_TIME = datetime.now().strftime("%H-%M")
# NOW_NOW = f"{NOW_DATE}-{NOW_TIME}"

# -------------------------------------------------------------------------- #

# Year Options
year_with_century = datetime.now().strftime("%Y")
year_without_century = datetime.now().strftime("%y")
YYYY = year_with_century

# -------------------------------------------------------------------------- #

# Month Options
month = datetime.now().strftime("%m")
month_full = datetime.now().strftime("%B")
month_abbrev = datetime.now().strftime("%b")
MM = month

# -------------------------------------------------------------------------- #

# Day Options
day = datetime.now().strftime("%d")
day_of_year = datetime.now().strftime("%j")
day_of_week = datetime.now().strftime("%w")
DD = day

# -------------------------------------------------------------------------- #

# Time Options
hour_24 = datetime.now().strftime("%H")
hour_12 = datetime.now().strftime("%I")
minute = datetime.now().strftime("%M")
second = datetime.now().strftime("%S")

# -------------------------------------------------------------------------- #

# Other Options
weekday_full = datetime.now().strftime("%A")
weekday_abbrev = datetime.now().strftime("%a")
week_number_sunday = datetime.now().strftime("%U")
week_number_monday = datetime.now().strftime("%W")
timezone_name = datetime.now().strftime("%Z")
timezone_offset = datetime.now().strftime("%z")
unix_timestamp = datetime.now().strftime("%s")
nanoseconds = datetime.now().strftime("%f") + "000"  # Adding three zeros to match nanosecond precision

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
