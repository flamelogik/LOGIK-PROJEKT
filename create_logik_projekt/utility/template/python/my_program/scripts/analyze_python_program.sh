#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        analyze_python_program.sh
# Version:          1.0.0
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-05-11
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program analyzes a python program and lists python
#                   types, like classes and functions, to aid in refactoring
#                   and modularization.
#                   For every type found a new python file is created with 
#                   the name of the type and an import command is added to
#                   'import_commands.py' to aid in creating a new program.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# -------------------------------------------------------------------------- #

# To Do List:       Apart from classes and functions, there are several 
#                   other Python types that could benefit from refactoring 
#                   or modularization:
#                   
#                   Constants: Constants are values that remain constant 
#                   throughout the execution of a program. 
#                   Grouping related constants together in separate files or 
#                   modules can improve code organization and readability.
#                   
#                   Enums: Enumerations provide a way to create symbolic 
#                   names for unique values, making code more expressive 
#                   and easier to understand. 
#                   Enum definitions can be placed in separate files or 
#                   modules for better organization.
#                   
#                   Data Classes: Python's dataclass module provides a way 
#                   to automatically generate special methods such 
#                   as __init__, __repr__, and __eq__ for classes that 
#                   primarily store data. 
#                   Separating data classes from other classes can make code 
#                   more modular and maintainable.
#                   
#                   Utility Functions: Utility functions are helper functions 
#                   that perform common tasks or calculations. 
#                   Placing utility functions in separate modules or packages 
#                   can promote code reuse and maintainability.
#                   
#                   Custom Exceptions: Defining custom exception classes 
#                   for specific error conditions can improve error handling 
#                   and make code more robust. 
#                   These exception classes can be organized in separate 
#                   modules based on the type of errors they represent.
#                   
#                   Decorators: Decorators are functions that modify the 
#                   behavior of other functions. 
#                   Grouping related decorators in separate modules can 
#                   enhance code organization and make it easier to apply 
#                   them consistently across multiple functions.
#                   
#                   Interfaces/Abstract Base Classes (ABCs): Interfaces or 
#                   ABCs define a set of methods that a class must implement. 
#                   By separating interfaces or ABCs from concrete 
#                   implementations, you can enforce a clear separation 
#                   of concerns and make code more extensible.
#                   
#                   Configuration Files: Configuration files containing 
#                   settings, parameters, or options used by a program 
#                   can be organized and modularized to improve 
#                   maintainability and facilitate configuration management.

# -------------------------------------------------------------------------- #

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section creates a decorative separator for blocks of text.
# ========================================================================== #

# Define a variable called 'separator'.
separator=$(printf '+ %s +' "$(printf -- '-%.0s' {1..75})")

# ========================================================================== #
# This section creates a decorative separator for blocks of code.
# ========================================================================== #

# Define a variable called 'separator_hash'.
separator_hash=$(printf '# %s #' "$(printf -- '-%.0s' {1..74})")

# ========================================================================== #
# This section defines some date variables.
# ========================================================================== #

# Define 'today_underscore' (use underscores instead of hyphens)
today_underscore=$(date +%Y_%m_%d)

# Define 'now_underscore' (use underscores instead of hyphens)
now_underscore=$(date +%H_%M)

# ========================================================================== #
# This section locates the running script and the related directories.
# ========================================================================== #

# Get the path to this script
path_to_this_script="$(cd "$(dirname "$0")" && pwd)"

# Get the directory of the script
script_dir="$(dirname "$0")"

# Change directory to script_dir
cd "$script_dir" || exit

# -------------------------------------------------------------------------- #

# Get the parent directory
parent_dir="$(dirname "$script_dir")"

# Change directory to script_dir
cd "$parent_dir" || exit

# -------------------------------------------------------------------------- #

# Define the target script to analyze
target_script="create_projekt_layout.py"

# -------------------------------------------------------------------------- #

# Define other directories and subdirectories
config_dir="$parent_dir/config"
scripts_dir="$parent_dir/scripts"
modules_dir="$scripts_dir/modules"
classes_dir="$modules_dir/classes"
functions_dir="$modules_dir/functions"
version_dir="$parent_dir/version"
python_script="$scripts_dir/$target_script"
class_list_file="$classes_dir/class_list.txt"
function_list_file="$functions_dir/function_list.txt"
import_commands_txt="$scripts_dir/import_commands.txt"

# -------------------------------------------------------------------------- #

# Function to create directories if they don't exist
create_directories() {
    echo "Creating necessary directories..."
    mkdir -p "$modules_dir"
    mkdir -p "$classes_dir"
    mkdir -p "$functions_dir"
}

# ========================================================================== #
# This section echoes information to the shell.
# ========================================================================== #

# Print the paths for verification
echo "Path to this script: $(basename "$path_to_this_script")"
echo "Parent directory:    $(basename "$parent_dir")"
echo "Config directory:    $(basename "$config_dir")"
echo "Scripts directory:   $(basename "$scripts_dir")"
# echo "Classes and functions directory: $(basename "$modules_dir")"
echo "Classes directory:   $(basename "$classes_dir")"
echo "Functions directory: $(basename "$functions_dir")"
echo "Version directory:   $(basename "$version_dir")"

# ========================================================================== #
# This section searches for strings in the python program.
# ========================================================================== #

# Function to analyze Python file and list classes and functions
analyze_python_file() {
    echo "Classes and functions in $target_script:"

    # Analyze functions
    echo "Functions:"
    while IFS= read -r function_line; do
        function_name=$(echo "$function_line" | sed -E 's/def\s+([a-zA-Z_][a-zA-Z0-9_]*).*/\1/' | sed -E 's/\(.*\)//')
        echo "$function_line"
        function_filename="$functions_dir/${function_name}.py"
        echo "# Function: $function_name" > "$function_filename"
        echo "$function_line" >> "$function_filename"
    done < <(grep -E '^\s*def\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\(' "$python_script")

    # Analyze classes
    echo "Classes:"
    while IFS= read -r class_line; do
        class_name=$(echo "$class_line" | sed -E 's/class\s+([a-zA-Z_][a-zA-Z0-9_]*).*/\1/' | sed -E 's/\(.*\)//')
        echo "$class_line"
        class_filename="$classes_dir/${class_name}.py"
        echo "# Class: $class_name" > "$class_filename"
        echo "$class_line" >> "$class_filename"
    done < <(grep -E '^\s*class\s+[a-zA-Z_][a-zA-Z0-9_]*\s*[:\(]' "$python_script")
}

# ========================================================================== #
# This section creates import commands for the found python types.
# ========================================================================== #

# Function to create import commands for classes and functions
create_import_commands() {
    echo "Creating import commands in $import_commands_txt"
    echo "#!/usr/bin/env python3" > "$import_commands_txt"
    echo "# Automatically generated import commands for classes and functions" >> "$import_commands_txt"
    echo "" >> "$import_commands_txt"
    echo "import os" >> "$import_commands_txt"
    echo "" >> "$import_commands_txt"

    # Import commands for classes
    echo "# Import commands for classes" >> "$import_commands_txt"
    while IFS= read -r class_file; do
        class_name=$(basename "$class_file" .py)
        echo "from modules.classes.${class_name} import ${class_name}" >> "$import_commands_txt"
    done < <(find "$classes_dir" -name '*.py')
    echo "" >> "$import_commands_txt"

    # Import commands for functions
    echo "# Import commands for functions" >> "$import_commands_txt"
    while IFS= read -r function_file; do
        function_name=$(basename "$function_file" .py)
        echo "from modules.functions.${function_name} import ${function_name}" >> "$import_commands_txt"
    done < <(find "$functions_dir" -name '*.py')
}

# ========================================================================== #
# This section executes the main functions.
# ========================================================================== #

# Create necessary directories
create_directories

# Analyze Python file
analyze_python_file

# Create import commands
create_import_commands

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
