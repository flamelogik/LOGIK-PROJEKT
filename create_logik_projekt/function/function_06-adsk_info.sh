#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_06-adsk_info.sh
# Version:          2.0.0
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-04-29
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program contains function(s) that are used to
#                   create new logik projekts.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines global variables.
# ========================================================================== #

# Define dir_names as a global array
declare -a dir_names=()

# Define adsk_dir
adsk_dir="/opt/Autodesk"

# ========================================================================== #
# This section initializes miscellaneous variables.
# ========================================================================== #

# Define function to initialize variables
initialize_adsk_variables() {
    sorted_dir_names=()
    max_dir_val="0000000000000000"
    max_dir_name=""
    max_dir_ver=""
    max_sw_val=""
    max_sw_ver=""
    max_sanitized_sw_ver=""
    beta_sw=false
}

# ========================================================================== #
# This section defines how to handle release or beta sw installations.
# ========================================================================== #

# Define function for processing beta_sw condition
process_beta_sw() {

    # Processing for beta_sw condition
    if [ "$beta_sw" = true ]; then
        # Set app_maj to the first part
        app_maj="${app_ver_long_parts[0]}"

        # Set app_min to the second part, padded to two zeroes
        if [[ "${app_ver_long_parts[1]}" == *"pr"* ]]; then
            app_min="00"
            app_pr_ver="${app_ver_long_parts[1]}"
        else
            app_min=$(printf "%02d" "${app_ver_long_parts[1]}")
        fi

        # Set app_dot to the third part, padded to two zeroes
        if [[ "${app_ver_long_parts[2]}" == *"pr"* ]]; then
            app_dot="00"
            app_pr_ver="${app_ver_long_parts[2]}"
        else
            if [[ "${app_ver_long_parts[1]}" == *"pr"* ]]; then
                app_dot="00"
            else
                app_dot=$(printf "%02d" "${app_ver_long_parts[2]}")
            fi
        fi

        # Set app_dot_dot to the fourth part, padded to two zeroes
        if [[ "${app_ver_long_parts[3]}" == *"pr"* ]]; then
            app_dot_dot="00"
            app_pr_ver="${app_ver_long_parts[3]}"
        else
            app_dot_dot=$(printf "%02d" "${app_ver_long_parts[3]}")
        fi

        # Set app_pr_dot_ver based on the position of 'pr'
        if [[ "$app_pr_ver" == *"pr"* ]]; then
            pr_index=$(expr "${#app_ver_long_parts[@]}" - 1)
            if [[ "${app_ver_long_parts[$pr_index]}" == *"pr"* ]]; then
                app_pr_dot_ver="00"
            elif [[ "${app_ver_long_parts[$pr_index - 1]}" == *"pr"* ]]; then
                app_pr_dot_ver=$(printf "%02d" "${app_ver_long_parts[$pr_index]}")
            fi
        fi

        # Set app_pr_val to the numeric value of $app_pr_ver (strip off the 'pr' prefix)
        app_pr_val="${app_pr_ver//pr/}"

        # Calculate calc_app_ver
        calc_app_ver="$app_maj"

        if [[ "$app_min" != "00" ]]; then
            calc_app_ver+=".$((10#${app_min}))"
        fi

        if [[ "$app_dot" != "00" ]]; then
            calc_app_ver+=".$((10#${app_dot}))"
        fi

        if [[ "$app_dot_dot" != "00" ]]; then
            calc_app_ver+=".$((10#${app_dot_dot}))"
        fi

        # Calculate calc_app_ver_pr
        calc_app_ver_pr="$calc_app_ver.$app_pr_ver"

        if [[ "$app_pr_dot_ver" != "00" ]]; then
            calc_app_ver_pr+=".$((10#${app_pr_dot_ver}))"
        fi

        # Calculate sanitized_app_ver
        sanitized_app_ver=$(echo "$calc_app_ver" | sed 's/\./_/g')

        # Calculate sanitized_app_ver_pr
        sanitized_app_ver_pr=$(echo "$calc_app_ver_pr" | sed 's/\./_/g')

        # Calculate calc_app_val_1
        calc_app_val_1="$app_maj$app_min$app_dot$app_dot_dot$app_val"

        # Calculate calc_app_val_2
        calc_app_val_2="$app_pr_val$app_pr_dot_ver"

        # Calculate calc_app_val
        calc_app_val="$calc_app_val_1$calc_app_val_2"

        # Check if calc_app_val is greater than max_sw_val or if max_sw_val is empty
        if [[ -z "$max_sw_val" || "$calc_app_val" -gt "$max_sw_val" ]]; then
            max_sw_val="$calc_app_val"
        fi
    fi
}

# -------------------------------------------------------------------------- #

# Define function for processing release_sw condition
process_release_sw() {

    # Processing for release_sw condition
    if [ "$release_sw" = true ]; then
        # Set app_maj to the first part
        app_maj="${app_ver_long_parts[0]}"

        # Assess the parts for app_min, app_dot, and app_dot_dot
        if [ -n "${app_ver_long_parts[1]}" ]; then
            app_min=$(printf "%02d" "${app_ver_long_parts[1]}")
        else
            app_min="00"
        fi

        if [ -n "${app_ver_long_parts[2]}" ]; then
            app_dot=$(printf "%02d" "${app_ver_long_parts[2]}")
        else
            app_dot="00"
        fi

        if [ -n "${app_ver_long_parts[3]}" ]; then
            app_dot_dot=$(printf "%02d" "${app_ver_long_parts[3]}")
        else
            app_dot_dot="00"
        fi

        # Set app_pr_ver and app_pr_dot_ver
        app_pr_ver="pr999"
        app_pr_dot_ver="99"

        # Set app_pr_val to the numeric value of $app_pr_ver (strip off the 'pr' prefix)
        app_pr_val="${app_pr_ver//pr/}"

        # Calculate calc_app_ver
        calc_app_ver="$app_maj"

        if [[ "$app_min" != "00" ]]; then
            calc_app_ver+=".$((10#${app_min}))"
        fi

        if [[ "$app_dot" != "00" ]]; then
            calc_app_ver+=".$((10#${app_dot}))"
        fi

        if [[ "$app_dot_dot" != "00" ]]; then
            calc_app_ver+=".$((10#${app_dot_dot}))"
        fi

        # Calculate sanitized_app_ver
        sanitized_app_ver=$(echo "$calc_app_ver" | sed 's/\./_/g')

        # # Calculate calc_app_ver_pr
        # calc_app_ver_pr="$calc_app_ver.$app_pr_ver"
        calc_app_ver_pr="$calc_app_ver"

        # if [[ "$app_pr_dot_ver" != "00" ]]; then
        #     calc_app_ver_pr+=".$((10#${app_pr_dot_ver}))"
        # fi

        # Calculate sanitized_app_ver_pr
        sanitized_app_ver_pr=$(echo "$calc_app_ver_pr" | sed 's/\./_/g')

        # Calculate calc_app_val_1
        calc_app_val_1="$app_maj$app_min$app_dot$app_dot_dot$app_val"

        # Calculate calc_app_val_2
        calc_app_val_2="$app_pr_val$app_pr_dot_ver"

        # Calculate calc_app_val
        calc_app_val="$calc_app_val_1$calc_app_val_2"

        # Check if calc_app_val is greater than max_sw_val or if max_sw_val is empty
        if [[ -z "$max_sw_val" || "$calc_app_val" -gt "$max_sw_val" ]]; then
            max_sw_val="$calc_app_val"
        fi
    fi
}

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Define function to check '/opt/Autodesk' for flame family software.
check_adsk_installations() {
    # local adsk_dir="/opt/Autodesk"
    # local separator=$(printf '+ %s +' "$(printf -- '-%.0s' {1..75})")

    # Check if the directory exists
    if [ ! -d "$adsk_dir" ]; then
        echo -e "\n$separator\n"
        echo -e "  '$adsk_dir' does not exist."
        echo -e "\n$separator\n"
        return 1
    fi

    # Get directory names and symbolic links matching multiple patterns
    while IFS= read -r -d '' dir; do
        dir_names+=("$dir")
    done < <(find "$adsk_dir" -maxdepth 1 \
            \( -name "fla*" \
            -o -name "lustre*" \
            -o -name "projectserver*" \
            -o -name "smoke*" \) -print0)

    # Validate if dir_names is not empty
    if [ ${#dir_names[@]} -eq 0 ]; then
        echo -e "\n$separator\n"
        echo -e "  No directories found in $adsk_dir starting with 'fla'."
        echo -e "\n$separator\n"
        return 1
    fi

    # Output the directory names
    echo -e "  The following installations have been found on this system:\n"
    printf "%s\n" "${dir_names[@]}" | sed 's/^/                    /'
    echo -e "\n$separator\n"
}

# Define function to display information derived from flame family software
display_software_information() {
    echo -e "  Directory:           $dir_name\n"
    echo -e "  Base name:           $dir_basename\n"
    echo -e "  App name:            $app_name"
    echo -e "  App val:             $app_val"
    echo -e "  Beta:                $beta_sw"
    echo -e "  Release:             $release_sw\n"
    echo -e "  App ver long:        $app_ver_long"
    echo -e "  Count parts:         $count_app_ver_long_parts\n"
    echo -e "  App maj:             $app_maj"
    echo -e "  App min:             $app_min"
    echo -e "  App dot:             $app_dot"
    echo -e "  App dot dot:         $app_dot_dot\n"
    echo -e "  App pr ver:          $app_pr_ver"
    echo -e "  App pr dot ver:      $app_pr_dot_ver"
    echo -e "  App pr val:          $app_pr_val\n"
    echo -e "  Calc app ver:        $calc_app_ver"
    echo -e "  Sanitized ver:       $sanitized_app_ver\n"
    echo -e "  Calc app ver pr:     $calc_app_ver_pr"
    echo -e "  Sanitized ver pr:    $sanitized_app_ver_pr"
    echo -e "  Calc app 1:          $calc_app_val_1"
    echo -e "  Calc app 2:          $calc_app_val_2"
    echo -e "  Calc app val:        $calc_app_val\n"
    echo -e "  Max sw val:          $max_sw_val"
    echo -e "\n$separator\n"
}

# -------------------------------------------------------------------------- #

# Define function to display sorted directories
display_sorted_dir_names() {
    # Sort sorted_dir_names in descending order by calc_app_val
    IFS=$'\n' sorted_dir_names=($(sort -r -t ':' -k2 <<<"${sorted_dir_names[*]}"))

    # Echo the sorted list
    echo -e "  Sorted Directory Names (Descending Order):\n"

    # Initialize a counter for numbering entries
    count=0

    # Iterate through the sorted directory names
    for sorted_dir in "${sorted_dir_names[@]}"; do
        count=$((count + 1))  # Increment the counter
        echo -n "            $count.    "  # Print the entry number
        # Extract and print the directory name
        echo -e "${sorted_dir%%:*}"

        # Limit the output to a maximum of 99 entries
        if [ "$count" -eq 99 ]; then
            break
        fi
    done

    # Display a separator
    echo -e "\n$separator\n"

}

# -------------------------------------------------------------------------- #

# Define function to display calculated information
display_calculated_flame_info() {

    # Print the highest directory value outside the loop
    # echo -e "  max dir val:      $max_dir_val"

    # Print the highest directory version outside the loop
    # echo -e "  max dir ver:      $max_dir_ver"

    # Print the highest directory name outside the loop
    echo -e "  max flame ver:       $max_dir_name"

    # Print the highest software app_ver outside the loop
    echo -e "  max sw ver:          $max_sw_ver"

    # Print the highest software app_ver outside the loop
    echo -e "  sanitized sw ver:    $max_sanitized_sw_ver"

    # Display a separator
    echo -e "\n$separator\n"

}

# -------------------------------------------------------------------------- #

process_adsk_installations() {
    # Loop through directory names
    for dir_name in "${dir_names[@]}"; do
        # Get basename of directory
        dir_basename=$(basename "$dir_name")

        # Check if basename contains 'pr'
        if [[ $dir_basename == *"pr"* ]]; then
            beta_sw=true
            release_sw=false
        else
            beta_sw=false
            release_sw=true
        fi

        # Split basename into parts
        IFS='_' read -ra dir_basename_parts <<< "$dir_basename"

        # Set app_name to the first part
        app_name="${dir_basename_parts[0]}"

        # Set app_ver_long to the second part
        app_ver_long="${dir_basename_parts[1]}"

        # Split app_ver_long into parts by period
        IFS='.' read -ra app_ver_long_parts <<< "$app_ver_long"

        # Count the number of parts
        count_app_ver_long_parts=${#app_ver_long_parts[@]}

        # Initialize variables
        app_maj=""
        app_min=""
        app_dot=""
        app_dot_dot=""
        app_pr_ver=""
        app_pr_dot_ver=""
        app_pr_val=""
        calc_app_ver=""
        calc_app_val_1=""
        calc_app_val_2=""
        calc_app_val=""

        # Set app_val based on the app_name
        case $app_name in
            "projectserver") app_val="6" ;;
            "flame") app_val="5" ;;
            "flare") app_val="4" ;;
            "flameassist") app_val="3" ;;
            "lustre") app_val="2" ;;
            "smoke") app_val="1" ;;
            *) app_val="0" ;;
        esac

        # ------------------------------------------------------------------ #

        # Process beta_sw condition
        process_beta_sw

        # ------------------------------------------------------------------ #

        # Process release_sw condition
        process_release_sw

        # ------------------------------------------------------------------ #

        # Append current dir_basename & calc_app_val to sorted_dir_names
        sorted_dir_names+=("$dir_basename:$calc_app_val")

        # ------------------------------------------------------------------ #

        # Update max_dir_val if the current calc_app_val is higher
        if [[ "$calc_app_val" > "$max_dir_val" ]]; then
            max_dir_val="$calc_app_val"
            max_dir_ver="$calc_app_ver"
            max_dir_name="$dir_basename"
            max_sw_ver="$calc_app_ver"
            max_sanitized_sw_ver="$sanitized_app_ver"
        fi

        # ------------------------------------------------------------------ #

        # Display software information
        # display_software_information

        # ------------------------------------------------------------------ #

    done
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Call the function to initialize the global variables
# process_adsk_installations
# display_calculated_flame_info
# display_sorted_dir_names

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    initialize_adsk_variables
    check_adsk_installations
    process_adsk_installations
    display_sorted_dir_names
    display_calculated_flame_info
fi

# Now the global variables can be accessed wherever needed
# echo -e "  $dir_names"

# Call the function to initialize the global variables
# initialize_adsk_variables
# check_adsk_installations
# process_adsk_installations
# display_calculated_flame_info
# display_sorted_dir_names

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
