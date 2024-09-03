#!/bin/bash

# Define the virtual environment directory
PROJEKT_Virtual_Env_Dir=~/projekt_python_virtual_env

# Define the log file with the current date prepended
LOG_FILE="$(dirname "$0")/$(date '+%Y-%m-%d')_activity_log.txt"

# Function to log messages
log_message() {
    local message="$1"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $message" >> "$LOG_FILE"
}

# Redirect all output to the log file
exec > >(tee -a "$LOG_FILE") 2>&1

# Create the virtual environment
python3.11 -m venv "$PROJEKT_Virtual_Env_Dir"
if [ -d "$PROJEKT_Virtual_Env_Dir" ]; then
    log_message "Virtual environment created successfully at $PROJEKT_Virtual_Env_Dir"
else
    log_message "Failed to create virtual environment at $PROJEKT_Virtual_Env_Dir"
    exit 1
fi

# Activate the virtual environment
source "$PROJEKT_Virtual_Env_Dir/bin/activate"
if [ "$VIRTUAL_ENV" == "$PROJEKT_Virtual_Env_Dir" ]; then
    log_message "Virtual environment activated successfully"
else
    log_message "Failed to activate virtual environment"
    exit 1
fi

# Install PySide6
if pip install PySide6; then
    log_message "PySide6 installed successfully"
else
    log_message "Failed to install PySide6"
    exit 1
fi

# Install OpenColorIO
if pip install opencolorio; then
    log_message "OpenColorIO installed successfully"
else
    log_message "Failed to install OpenColorIO"
    exit 1
fi