#!/bin/bash

# -------------------------------------------------------------------------- #

# filename: "function_28-backup_logs.sh"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to backup creation log
backup_creation_log() {
    # Copy $projekt_creation_log_file to $flame_proj_dir/cfg.
    cp "${projekt_creation_log_file}" "${flame_proj_dir}/cfg"
    # Move $projekt_creation_log_file to $tgt_configs_workstation_dir.
    mv "${projekt_creation_log_file}" "${tgt_configs_workstation_dir}"
    echo -e "  logik projekt creation log backed up to config directory:\n"
    echo -e "  $(basename "$projekt_creation_log_file")"
    echo -e "\n$separator\n"
}

# -------------------------------------------------------------------------- #

# Function to backup logik projekt metadata XML
backup_projekt_xml() {
    # Copy $projekt_metadata_xml_file to $flame_proj_dir/cfg.
    cp "${projekt_metadata_xml_file}" "${flame_proj_dir}/cfg"
    # Move $projekt_metadata_xml_file to $tgt_configs_workstation_dir.
    mv "${projekt_metadata_xml_file}" "${tgt_configs_workstation_dir}"
    echo -e "  logik projekt metadata xml backed up to config directory:\n"
    echo -e "  $(basename "$projekt_metadata_xml_file")"
    echo -e "\n$separator\n"
}

# -------------------------------------------------------------------------- #

# Function to backup logik projekt setup file
backup_projekt_setup_file() {
    # Copy logik projekt_setup files to $flame_proj_dir/cfg.
    cp "${projekt_setup_file}" "${flame_proj_dir}/cfg"
    # Move logik projekt_setup file to $tgt_configs_workstation_dir.
    mv "${projekt_setup_file}" "${tgt_configs_workstation_dir}"
    echo -e "  logik projekt setup file backed up to config directory:\n"
    echo -e "  $(basename "$projekt_setup_file")"
    echo -e "\n$separator\n"
}

# -------------------------------------------------------------------------- #

# Function to backup logik projekt setup template
backup_projekt_setup_template() {
    # Copy logik projekt_setup template to $flame_proj_dir/cfg.
    cp "${projekt_setup_template}" "${flame_proj_dir}/cfg"
    # Move logik projekt_setup template to $tgt_configs_dir.
    mv "${projekt_setup_template}" "${tgt_configs_dir}"
    echo -e "  logik projekt setup template backed up to config directory:\n"
    echo -e "  $(basename "$projekt_setup_template")"
    echo -e "\n$separator\n"
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    backup_creation_log
    backup_projekt_xml
    backup_projekt_setup_file
    backup_projekt_setup_template
fi

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #
