#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_02-date.sh
# Version:          2.0.3
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-05-03
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program contains function(s) that are used to
#                   create new logik projekts.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines variables based on the date.
# ========================================================================== #

# Current Date & Time Options
current_datetime=$(date "+%Y-%m-%d %H:%M:%S")
today=$(date "+%Y-%m-%d")
yesterday=$(date -v -1d "+%Y-%m-%d" 2>/dev/null \
    || date -d "yesterday" "+%Y-%m-%d")
tomorrow=$(date -v +1d "+%Y-%m-%d" 2>/dev/null \
    || date -d "tomorrow" "+%Y-%m-%d")

# -------------------------------------------------------------------------- #

# Current Date and Time Options
now_h_m_s=$(date "+%H:%M:%S")
now_h_m=$(date "+%H-%M")
today_now=$(date "+%F_%H-%M")
TODAY="$today"
NOW="$now_h_m_s"

# NOW_DATE=$(date "+%F")
# NOW_TIME=$(date "+%H-%M")
# NOW_NOW="$NOW_DATE-$NOW_TIME"

# -------------------------------------------------------------------------- #

# Year Options
year_with_century=$(date "+%Y")
year_without_century=$(date "+%y")
YYYY=$year_with_century

# -------------------------------------------------------------------------- #

# Month Options
month=$(date "+%m")
month_full=$(date "+%B")
month_abbrev=$(date "+%b")
MM=$month

# -------------------------------------------------------------------------- #

# Day Options
day=$(date "+%d")
day_of_year=$(date "+%j")
day_of_week=$(date "+%w")
DD=$day

# -------------------------------------------------------------------------- #

# Time Options
hour_24=$(date "+%H")
hour_12=$(date "+%I")
minute=$(date "+%M")
second=$(date "+%S")

# -------------------------------------------------------------------------- #

# Other Options
weekday_full=$(date "+%A")
weekday_abbrev=$(date "+%a")
week_number_sunday=$(date "+%U")
week_number_monday=$(date "+%W")
timezone_name=$(date "+%Z")
timezone_offset=$(date "+%z")
unix_timestamp=$(date "+%s")
nanoseconds=$(date "+%N")

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #

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
