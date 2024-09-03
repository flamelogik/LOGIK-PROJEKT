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

# File Name:        validate_downloads.sh
# Version:          0.9.9
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section defines paths for the script.
# ========================================================================== #

# Sets xtrace mode, which causes each command to be echoed before it is executed.
# Exits the script with an error code of 1 if any command fails.
# set -ex

# -------------------------------------------------------------------------- #

# Define the path to the current script in a variable called 'path_to_here'
path_to_here=$(cd $(dirname "$0") && pwd)

# change directory to path_to_here
cd $path_to_here

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# ========================================================================== #
# Decorative Separator
# ========================================================================== #

separator=$(printf '+ %s +' "$(printf -- '-%.0s' {1..75})")

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# ========================================================================== #
# This section creates decorative separators for titles and banners.
# ========================================================================== #

# Function to repeat a character n times
repeat_char() {
    local char=$1
    local count=$2
    printf "%0.s$char" $(seq 1 "$count")
}

# -------------------------------------------------------------------------- #

# Function to ensure a line is exactly 79 characters
make_line_79_chars() {
    local line=$1
    local current_length=${#line}

    # Calculate the number of additional "=" characters needed
    local pad=$((79 - current_length))

    # Add the required pad before the " #" at the end
    line="${line% #}$(repeat_char "=" "$pad") #"

    echo -e "$line"
}

# -------------------------------------------------------------------------- #

# Function to generate title line
generate_title_line() {
    local title=$1
    local total_length=79

    # Calculate pad on each side of the title
    local title_pad_length=$(( (total_length - ${#title} - 8) / 2 ))

    # Generate the title_line
    local title_line=$(printf "# %s %s %s #\n" \
        "$(repeat_char "=" "$title_pad_length")" \
        "$title" \
        "$(repeat_char "=" "$title_pad_length")")

    # Ensure title_line is exactly 79 characters
    title_line=$(make_line_79_chars "$title_line")

    echo -e "$title_line"
}

# -------------------------------------------------------------------------- #

# Function to generate end of title line
generate_end_title_line() {
    local end_title=$1
    local total_length=79

    # Calculate pad on each side of the end_title
    local end_title_pad_length=$(( (total_length - ${#end_title} - 8) / 2 ))

    # Generate the end_title_line
    local end_title_line=$(printf "# %s %s %s #\n" \
        "$(repeat_char "=" "$end_title_pad_length")" \
        "$end_title" \
        "$(repeat_char "=" "$end_title_pad_length")")

    # Ensure end_title_line is exactly 79 characters
    end_title_line=$(make_line_79_chars "$end_title_line")

    echo -e "$end_title_line"
}

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# ========================================================================== #
# This section collects username, group memberships, & system info.
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Get username, primary group and group memberships.
current_user="$USER"
primary_group="$(id -gn)"
all_groups="$(groups | tr ' ' ',' | sed 's/,/, /g')"

# -------------------------------------------------------------------------- #

# Determine the operating system
if [[ "$(uname)" == "Darwin" ]]; then
    # macOS
    operating_system="macOS"

elif [[ "$(uname)" == "Linux" ]]; then
    # Linux
    operating_system="Linux"

else
    # Default to a common directory if the OS is not recognized
    echo -e "\n$separator\n"
    echo -e "  Unsupported operating system."
    echo -e "\n$separator\n"
    exit 1
fi

# -------------------------------------------------------------------------- #

# Get the workstation name
if [[ "$operating_system" == "macOS" ]]; then
    # For macOS
    workstation_name=$(scutil --get ComputerName)
elif [[ "$operating_system" == "Linux" ]]; then
    # For Linux
    workstation_name=$(hostname)
else
    # Default to a generic name if the OS is not recognized
    workstation_name="UnknownWorkstation"
fi

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# ========================================================================== #
# This section defines variables based on the date.
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Current Date & Time Options
current_datetime=$(date "+%Y-%m-%d %H:%M:%S")
today=$(date "+%Y-%m-%d")
yesterday=$(date -v -1d "+%Y-%m-%d" 2>/dev/null \
    || date -d "yesterday" "+%Y-%m-%d")
tomorrow=$(date -v +1d "+%Y-%m-%d" 2>/dev/null \
    || date -d "tomorrow" "+%Y-%m-%d")

# -------------------------------------------------------------------------- #

# Custom Date & Time Options
now_h_m_s=$(date "+%H:%M:%S")
now_h_m=$(date "+%H-%M")
today_now=$(date "+%F_%H-%M")
TODAY="$today"
NOW="$now_h_m_s"

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
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# ========================================================================== #
# This section defines title_01 and banner_01.
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Define variables for the decorative lines that get printed to the shell.
title_01="VALIDATION OF DOWNLOADED FILES"
banner_01="$title_01 STARTED"
end_title_01="$title_01 COMPLETED"
end_banner_01=$(generate_end_title_line "$end_title_01")

# -------------------------------------------------------------------------- #

# Display banner_01 and a separator.
echo -e "\n\n$(generate_title_line "$banner_01")\n"
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# ========================================================================== #
# Prompt User to Choose the Downloads Directory
# ========================================================================== #

# -------------------------------------------------------------------------- #

if [[ "$operating_system" == "Linux" ]]; then
    if ! command -v zenity &> /dev/null; then
        echo -e "  Error: 'zenity' is not installed."
        echo -e "  Please install it to use this script on Linux."
        exit 1
    fi

    downloads_dir=$(zenity \
    --file-selection \
    --directory \
    --title="Select Downloads Directory")

    if [ $? -eq 1 ]; then
        echo "Operation canceled by the user."
        exit 0
    fi

    # For Linux
    # calculated_md5=$(md5sum "$file_path" | awk '{print $1}')

elif [[ "$operating_system" == "macOS" ]]; then
    
    downloads_dir=$(
        osascript -e 'POSIX path of (choose folder with prompt "Select Downloads Directory")')

    if [ -z "$downloads_dir" ]; then
        echo "Operation canceled by the user."
        exit 0
    fi

    # For macOS
    # calculated_md5=$(md5 -r "$file_path" | awk '{print $1}')

else
    echo "Unsupported operating system."
    exit 1
fi

echo -e "\n$separator\n"
echo -e "  Chosen Downloads Directory: $downloads_dir"
echo -e "\n$separator\n"

if [ ! -d "$downloads_dir" ]; then
    echo "  Error: Downloads directory does not exist. Exiting."
    exit 1
fi

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# ========================================================================== #
# This section defines paths for activity logging.
# ========================================================================== #

# -------------------------------------------------------------------------- #

# # Make dated folders if necessary
# mkdir -p "logs/$YYYY"
# mkdir -p "logs/$YYYY/$MM"
# mkdir -p "logs/$YYYY/$MM/$DD"

# -------------------------------------------------------------------------- #

# Make a download validation log
download_validation_log_file=\
"$downloads_dir/$YYYY-$MM-$DD-$now_h_m-download_validation_log"

# Redirect stdout and stderr to the log file
exec > >(tee -a "$download_validation_log_file") 2>&1

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# ========================================================================== #
# Populate the File List
# ========================================================================== #

# -------------------------------------------------------------------------- #

file_list=()

while IFS= read -r -d '' file_path; do
    if [[ ! "$file_path" == *.md5 ]]; then
        file_list+=("$file_path")
    fi
done < <(find "$downloads_dir" -type f -print0)

# -------------------------------------------------------------------------- #

# Set the list_count
list_count=1

# Print the entire file list
echo -e "  The list of files is:"
for file_path in "${file_list[@]}"; do
    file_basename=$(basename "$file_path")
    # echo -e "    $file_basename\n"
    echo -e "\n    $list_count. $file_basename"
    list_count=$((list_count + 1))
done

echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# ========================================================================== #
# Process the File List
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Set the file_count
file_count=1

# Process the entire file list
for file_path in "${file_list[@]}"; do
    file_basename=$(basename "$file_path")
    echo -e "  $file_count. $file_basename"
    file_count=$((file_count + 1))

    # Calculate MD5 checksum for each file
    if [[ "$operating_system" == "Linux" ]]; then
        calculated_md5=$(md5sum "$file_path" | awk '{print $1}')
    else
        calculated_md5=$(md5 -r "$file_path" | awk '{print $1}')
    fi

    md5_file="$file_path.md5"
    if [ ! -e "$md5_file" ]; then
        echo -e "\n  Skipping $file_basename:"
        echo -e "\n  No corresponding .md5 file found."
        echo -e "\n$separator\n"
       continue
    fi

    expected_md5=$(cut -d' ' -f1 "$md5_file")

    # echo -e "  $expected_md5 - Expected MD5 for $file_basename"
    echo -e "\n  Expected Checksum: $expected_md5"

    # echo -e "  $calculated_md5 - Checksum for $file_basename"
    echo -e "  Actual Checksum:   $calculated_md5"

    if [ "$calculated_md5" == "$expected_md5" ]; then
        echo -e "\n  Checksums match for $file_basename"
        echo -e "\n  The file is valid."
        echo -e "\n$separator\n"
    else
        echo -e "\n  Checksums do not match for $file_basename"
        echo -e "The file may be corrupted."
        echo -e "\n$separator\n"
    fi
done

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# ========================================================================== #
# This section echoes end_banner01.
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Display the end_title line.
echo -e ""
echo -e "$end_banner_01\n"
echo -e "\n\n$separator\n$separator\n$separator\n\n"

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
# modified:         2024-08-31 - 16:51:09
# comments:         prep for release - code appears to be functional
# -------------------------------------------------------------------------- #
