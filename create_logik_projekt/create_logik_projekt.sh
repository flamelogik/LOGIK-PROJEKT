#!/bin/bash

# -------------------------------------------------------------------------- #

# Program Name:     create_logik_projekts.sh
# Version:          2.0.1
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-04-30
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program determines system information and collects
#                   user input to create new logik projekts.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section identifies and locates this script when executed.
# ========================================================================== #

# Get the base name of the script
script_name=$(basename "$0")

# Get the full path to the script using realpath
script_path=$(dirname "$(realpath "$0")")

# Change directory to $script_path
cd $script_path

# Construct the full path to the script
alias_path="$script_path/$script_name"

# -------------------------------------------------------------------------- #

# Define functions_dir
functions_dir="$script_path/function"

# ========================================================================== #
# This section sources functions to create text separators.
# ========================================================================== #

source "$functions_dir/function_01-separators.sh"

# ========================================================================== #
# This section sources date functions and variables.
# ========================================================================== #

source "$functions_dir/function_02-date.sh"

# ========================================================================== #
# This section sources title and banner functions.
# ========================================================================== #

source "$functions_dir/function_03-banners.sh"

# ========================================================================== #
# This section sources projekt setup and logging functions.
# ========================================================================== #

source "$functions_dir/function_04-setup.sh"

# ========================================================================== #
# This section sources user, group and environment information.
# ========================================================================== #

source "$functions_dir/function_05-environment.sh"

# ========================================================================== #
# This section analyzes the flame family software installations.
# ========================================================================== #

source "$functions_dir/function_06-adsk_info.sh"

# ========================================================================== #
# This section gathers logik projekt name info.
# ========================================================================== #

source "$functions_dir/function_07-projekt_name.sh"

# ========================================================================== #
# This section gathers logik projekt resolution info.
# ========================================================================== #

source "$functions_dir/function_08-projekt_resolution.sh"

# ========================================================================== #
# This section gathers logik projekt bit-depth info.
# ========================================================================== #

source "$functions_dir/function_09-projekt_depth.sh"

# ========================================================================== #
# This section gathers logik projekt framerate info.
# ========================================================================== #

source "$functions_dir/function_10-projekt_framerate.sh"

# ========================================================================== #
# This section gathers logik projekt color science info.
# ========================================================================== #

source "$functions_dir/function_11-projekt_color_science.sh"

# ========================================================================== #
# This section gathers logik projekt start frame info.
# ========================================================================== #

source "$functions_dir/function_12-projekt_start_frame.sh"

# ========================================================================== #
# This section gathers logik projekt metadata into an xml file.
# ========================================================================== #

source "$functions_dir/function_13-projekt_summary.sh"

# ========================================================================== #
# This section sets commonly used options for rsync.
# ========================================================================== #

source "$functions_dir/function_14-rsync_options.sh"

# ========================================================================== #
# This section uses wiretap_create_node to create a flame projekt.
# ========================================================================== #

source "$functions_dir/function_15-projekt_flame.sh"

# ========================================================================== #
# This section creates directories in a new logik projekt.
# ========================================================================== #

source "$functions_dir/function_16-projekt_flame_dirs.sh"

# ========================================================================== #
# This section creates logik projekt job directories.
# ========================================================================== #

source "$functions_dir/function_17-job_dirs.sh"

# ========================================================================== #
# This section synchronizes flame presets to the logik projekt.
# ========================================================================== #

source "$functions_dir/function_18-sync_batch.sh"

source "$functions_dir/function_19-sync_mediaimport.sh"

source "$functions_dir/function_20-sync_bookmarks.sh"

source "$functions_dir/function_21-sync_overlays.sh"

source "$functions_dir/function_22-sync_python.sh"

source "$functions_dir/function_23-sync_io.sh"

source "$functions_dir/function_24-sync_col_policies.sh"

source "$functions_dir/function_25-sync_col_transforms.sh"

# ========================================================================== #
# This section adds a color management policy to the new logik projekt.
# ========================================================================== #

source "$functions_dir/function_26-add_color_policy.sh"

# ========================================================================== #
# This section creates links to the logik projekt setup directories.
# ========================================================================== #

source "$functions_dir/function_27-link_setup_dirs.sh"

# ========================================================================== #
# This section backs up the logs and metadata files and templates.
# ========================================================================== #

source "$functions_dir/function_28-backup_logs.sh"

# ========================================================================== #
# This section creates a flame archiving script for the logik projekt.
# ========================================================================== #

source "$functions_dir/function_29-create_archive_script.sh"

# ========================================================================== #
# This section creates a backup script for the logik projekt.
# ========================================================================== #

source "$functions_dir/function_30-create_backup_script.sh"

# ========================================================================== #
# This section utilizes all previous functions.
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Function to create directories, files and logs for logik projekt setup
setup_logik_projekt

# -------------------------------------------------------------------------- #

# Redirect stdout and stderr to the log file
exec > >(tee -a "$projekt_creation_log_file") 2>&1

# -------------------------------------------------------------------------- #

# Display banner_01 and a separator.
echo -e "\n$(generate_title_line "$banner_01")\n"
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

get_environment

# -------------------------------------------------------------------------- #

echo -e "  from template:       $has_projekt_setup_template"
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

echo -e "  current date:        $today"
echo -e "  current time:          $now_h_m_s"
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

echo -e "  current user:        $current_user"
echo -e "  primary group:       $primary_group"
# echo -e "  all groups:          $all_groups"
echo -e "  other groups:        $other_groups"
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

echo -e "  user home:           $user_home"
echo -e "  shell type:          $shell_type"
# echo -e "  .rc filename:        $rc_filename"
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

# Display a separator
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section displays operating system & flame installation information.
# ========================================================================== #

# Display banner_02 and a separator.
echo -e "\n$(generate_title_line "$banner_02")\n"
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

echo -e "  workstation name:    $workstation_name"
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

echo -e "  operating system:    $operating_system"
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

# Initialize flame family software variables.
initialize_adsk_variables

# Check for flame family software.
check_adsk_installations

# Process the flame family software installations.
process_adsk_installations

# Display sorted flame directories.
display_sorted_dir_names

# Display maximum flame values.
display_calculated_flame_info

# -------------------------------------------------------------------------- #

# Display a separator
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section displays logik projekt information.
# ========================================================================== #

# Display banner_03 and a separator.
echo -e "\n$(generate_title_line "$banner_03")\n"
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

echo -e "  script name:         $script_name"
# echo -e "  script path:         $script_path"
# echo -e "  alias path:          $alias_path"
# echo -e "  functions dir:       $functions_dir"
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

echo -e "  creation log:        $(basename "$projekt_creation_log_file")"
echo -e "  setup file:          $(basename "$projekt_setup_file")"
echo -e "  setup template:      $(basename "$projekt_setup_template")"
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

gather_projekt_name
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

gather_projekt_resolution
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

gather_projekt_depth
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

gather_projekt_framerate
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

gather_projekt_color_science
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

gather_projekt_start_frame
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

# # Create directories
# create_metadata_directories

# Set metadata
set_projekt_metadata

# # Summarize metadata
summarize_projekt_metadata

# Write metadata to file
write_projekt_metadata
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

echo -e "  rsync options:       $sync_opts"
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

create_wiretap_projekt
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

create_flame_projekt_directories
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

create_projekt_job_directories
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

umask 0

sync_batch_project_bins
sync_mediaImport_rules
sync_bookmarks
sync_overlays
sync_python_scripts
sync_io_presets
sync_color_policies
sync_color_transforms

# -------------------------------------------------------------------------- #

add_syncolor_policy

# -------------------------------------------------------------------------- #

remove_old_links

echo -e "  older symbolic links removed."
echo -e "\n$separator\n"

# Call the function to create symbolic links
create_links

echo -e "  Symbolic links created."
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #

backup_creation_log
backup_projekt_xml
backup_projekt_setup_file
backup_projekt_setup_template

# -------------------------------------------------------------------------- #

create_archive_script

# -------------------------------------------------------------------------- #

create_backup_script

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section echoes end_banner03.
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Display the end_title line.
echo -e "$end_banner_03\n"
echo -e "\n\n$separator\n$separator\n$separator\n\n"

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
