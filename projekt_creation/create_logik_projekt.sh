#!/bin/bash

# -------------------------------------------------------------------------- #

# Program Name:     create_logik_projekt.sh
# Version:          1.0
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-04-22
# Modifier:         Phil MAN - phil_man@mac.com

# Changelist:       Rebranded flame project toolset to LOGIK-PROJEKT.
#                   Modularized monolithic bash script to aid maintenance.

# -------------------------------------------------------------------------- #

# Description:      This program determines system information and collects
#                   user input to create new logik projekts.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your home directory.
#                   Assuming the initial run is successful:
#                   Type 'projekt' in a shell.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section identifies and locates this script when executed.
# ========================================================================== #

# -------------------------------------------------------------------------- #

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
functions_dir="$script_path/sub_functions"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section sources functions and subprograms to be used in this program.
# ========================================================================== #

# -------------------------------------------------------------------------- #
source "$functions_dir/sub_function_00-docstring.sh"
# -------------------------------------------------------------------------- #
source "$functions_dir/sub_function_01-separators.sh"
# -------------------------------------------------------------------------- #
source "$functions_dir/sub_function_02-environment.sh"
# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section creates a shell alias called 'projekt' for future use.
# ========================================================================== #

# Set the variable 'rc_filepath' for the 'run control' file
rc_filepath="${user_home}/${rc_filename}"

# Create rc_filepath if it does not exist
if [ ! -f "$rc_filepath" ]; then
    touch "$rc_filepath"
    # Set the correct permissions for rc_filepath to 600
    chmod 600 "$rc_filepath"
fi

# Check if the alias exists
if ! grep -q "alias projekt=" "$rc_filepath"; then
    # Add aliases to the appropriate rc file
    echo "" >> "$rc_filepath"
    echo "# projekt creates logik projekts on your workstation" \
        >> "$rc_filepath"
    echo "alias projekt=\"$alias_path\"" >> "$rc_filepath"
    echo "" >> "$rc_filepath"
fi

# -------------------------------------------------------------------------- #
source "$functions_dir/sub_function_03-date_functions.sh"
# -------------------------------------------------------------------------- #
source "$functions_dir/sub_function_04-titles_and_banners.sh"
# -------------------------------------------------------------------------- #
source "$functions_dir/sub_function_05-logging.sh"
# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section initiates logging.
# ========================================================================== #

# Set has_projekt_setup_template to False
initialize_template_state

# Create the logging directories and files
create_logik_projekt_directories_and_files

# Redirect stdout and stderr to the log file
exec > >(tee -a "$projekt_creation_log_file") 2>&1

# ========================================================================== #
# This section displays banner_01.
# ========================================================================== #

# Display banner_01 and a separator.
echo -e "\n$(generate_title_line "$banner_01")\n"
echo -e "\n$separator\n"

# ========================================================================== #
# This section prints relevant info to the shell and the log.
# ========================================================================== #

echo -e "  script name:      $script_name"
echo -e "  script path:      $script_path"
echo -e "  alias path:       $alias_path"
echo -e "  functions dir:    $functions_dir"
echo -e "\n$separator\n"

echo -e "  current date:     $today"
echo -e "  current time:     $now_h_m_s"
echo -e "\n$separator\n"

echo -e "  user name:        $current_user"
echo -e "  primary group:    $primary_group"
echo -e "  other groups:     $other_groups"
echo -e "\n$separator\n"

# -------------------------------------------------------------------------- #
source "$functions_dir/sub_function_06-init_vars.sh"
# -------------------------------------------------------------------------- #
source "$functions_dir/sub_function_07-flame_info.sh"
# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section displays banner_02.
# ========================================================================== #

# Display banner_02 and a separator.
echo -e "\n$(generate_title_line "$banner_02")\n"
echo -e "\n$separator\n"

echo -e "  operating system: $operating_system"
# echo -e "  hostname long:    $hostname"
# echo -e "  hostname short:   $hostname_short"
echo -e "  workstation name: $workstation_name"
echo -e "\n$separator\n"

# ========================================================================== #
# This section echoes flame family software installation info to the shell.
# ========================================================================== #

# Print the list of flame family installations
list_flame_installations
echo -e "\n$separator\n"

# ========================================================================== #
# This section displays end_banner_02.
# ========================================================================== #

# Display the end_title line.
echo -e "\n$end_banner_02\n"
echo -e "\n$separator\n$separator\n$separator\n"

# ========================================================================== #
# This section displays banner_03.
# ========================================================================== #

# Display banner_03 and a separator.
echo -e "\n$(generate_title_line "$banner_03")\n"
echo -e "\n$separator\n"

# ========================================================================== #
# This section prompts the user to locate the projekt setup template.
# ========================================================================== #

# Prompt for logik projekt template
# prompt_for_logik_projekt_template
echo -e "\n$separator\n"

# ========================================================================== #
# Function to prompt the user for a logik projekt template.
# ========================================================================== #

pwd

# Prompt the user to confirm if they have a project setup file
read -p "Do you have a project setup template? Y/N [Y]: " answer

# Default to 'Y' if no input
answer="${answer:-Y}"

# Convert the answer to uppercase for comparison
answer=$(echo "$answer" | tr '[:lower:]' '[:upper:]')

if [ "$answer" = "Y" ]; then

    # Set variable to True
    has_projekt_setup_template=True

fi

# -------------------------------------------------------------------------- #

if [ "$has_projekt_setup_template" = "True" ]; then

    # ---------------------------------------------------------------------- #

    # Browse for a project setup file
    if [[ "$operating_system" == "macOS" ]]; then

        # macOS
        chosen_projekt_setup_template=$(osascript \
        -e "tell application \"System Events\" to activate" \
        -e "POSIX path of \
        (choose file with prompt \
        \"Select Project Setup File\")\
        ")

    else

        # Linux
        chosen_projekt_setup_template=$(zenity \
        --file-selection \
        --title="Select Project Setup File"
        )

    fi

        # Check if user canceled the operation
    if [ $? -ne 0 ]; then
        echo "File selection canceled."
        exit 1
    fi

    # ---------------------------------------------------------------------- #

    # # Check if the template project setup file exists
    # if [ ! -f "$projekt_setup_template" ]; then

    #     Copy the chosen project setup file to template location
    #     cp "$chosen_projekt_setup_template" "$projekt_setup_template"
        
    #     echo -e "Chosen project setup file backed up."
    # fi

    # ---------------------------------------------------------------------- #

else

    # ---------------------------------------------------------------------- #

    # Name the logik projekt setup directory
    projekt_setup_dir="$script_path/logs/$YYYY/$MM/$DD/"

    # Name the logik projekt setup filename
    projekt_setup_filename="$YYYY-$MM-$DD-$now_h_m-projekt_setup_file"

    # Name the logik projekt setup file
    projekt_setup_file="$projekt_setup_dir/$projekt_setup_filename"

    # Create the logik projekt setup file
    touch "$projekt_setup_file"

    # ---------------------------------------------------------------------- #

fi

# -------------------------------------------------------------------------- #


# ========================================================================== #
# This section echoes the initial variables to the creation log.
# ========================================================================== #

echo -e "  creation log:     $projekt_creation_log_file"
echo -e "  projekt setup:    $projekt_setup_file"
echo -e "  projekt template: $projekt_setup_template"
echo -e "\n$separator\n"

# Create the metadata directories and files
create_logik_projekt_metadata_directories_and_files

# -------------------------------------------------------------------------- #

# -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_08-banner_01.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_09-display_users_groups_os.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_10-banner_02.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_11-check_adsk.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_12-init_vars.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_13-list_flame_dirs.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_14-print_flame_dirs.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_15-echo_flame_versions.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_16-end_banner_02.sh"
# -------------------------------------------------------------------------- #
source "$functions_dir/sub_function_17-validate_input.sh"
# -------------------------------------------------------------------------- #
source "$functions_dir/sub_function_18-rsync_vars.sh"
# -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_19-banner_03.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_20-validate_JOBS.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_21-end_banner_03.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_22-banner_04.sh"
# -------------------------------------------------------------------------- #
source "$functions_dir/sub_function_23-get_name_info.sh"

# Call the function to gather name information
gather_name_info
# display_client_info
# display_campaign_info
write_client_info
write_campaign_info

# -------------------------------------------------------------------------- #
source "$functions_dir/sub_function_24-get_resolution_info.sh"

# Call the function to gather resolution information
gather_resolution_info

write_depth_info

# -------------------------------------------------------------------------- #
source "$functions_dir/sub_function_25-get_depth_info.sh"

# Call the function to gather bit depth information
gather_depth_info

write_resolution_info

# -------------------------------------------------------------------------- #
source "$functions_dir/sub_function_26-get_framerate_info.sh"

# Call the function to gather framerate information
gather_framerate_info

write_framerate_info

# -------------------------------------------------------------------------- #
source "$functions_dir/sub_function_27-get_color_science_info.sh"

# Call the function to gather color science information
gather_color_science_info

write_color_science_info

# -------------------------------------------------------------------------- #
source "$functions_dir/sub_function_28-set_start_frame.sh"

# Call the function to get the start frame info
get_start_frame_info

write_start_frame_info

# -------------------------------------------------------------------------- #
source "$functions_dir/sub_function_29-set_and_summarize_metadata.sh"

# Call functions to display summary, create directories, and add metadata
display_summary
create_directories # XML directories

# # add_metadata    echo -e "  Logik Projekt Summary\n"
# echo -e "  Projekt Name:        $name"
# echo -e "  Projekt NickName:    $nickname"
# echo -e "  Projekt Description: $description"
# echo -e "  Shotgrid Name:       $shotgun_name"
# echo -e "  Setup Directory:     $setup_dir"
# echo -e "  Flame Framestore:    $partition"
# echo -e "  Software Version:    $version"
# echo -e "  Frame Width:         $frame_width"
# echo -e "  Frame Height:        $frame_height"
# echo -e "  Color Depth:         $frame_depth"
# echo -e "  Aspect Ratio:        $aspect_ratio"
# echo -e "  Field Dominance:     $field_dominance"
# echo -e "  Frame Rate:          $frame_rate"
# echo -e "  Start Frame:         $default_start_frame"
# echo -e "  Color Policy:        $proj_color_science"
# echo -e "\n$separator\n"

# create_or_truncate_file
# add_metadata_to_file
# -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_30-create_project.sh"
# -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_31-create_project_dirs.sh"

# # Call the functions
# create_flame_project_dir
# create_setup_directories
# -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_32-create_job_dirs.sh"

# # Call the function
# create_job_directories
# -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_33-create_batch_project_bins.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_34-create_mediaImport_rules.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_35-create_bookmarks.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_36-create_burn_metadata_overlays.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_37-add_mmm_python.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_38-add_io_presets.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_39-validate_color_policies.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_40-validate_color_transforms.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_41-add_color_policy.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_42-link_setup_dirs.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_43-backup_logs.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_44-create_archive_script.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_45-create_backup_script.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_46-end_banner_04.sh"
# # -------------------------------------------------------------------------- #
# source "$functions_dir/sub_function_47-end_banner_02.sh"
# # -------------------------------------------------------------------------- #






