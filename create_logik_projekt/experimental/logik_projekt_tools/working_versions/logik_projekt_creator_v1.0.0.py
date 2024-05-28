'''
# -------------------------------------------------------------------------- #

# File Name:        projekt_creator.py
# Version:          1.0.0
# Language:         python script
# Author:           [Your Name] - [Your Email]
# Created:          2024-05-23
# Modified:         2024-05-23

# Description:      This program creates a project directory structure
#                   based on user input.

# -------------------------------------------------------------------------- #
'''

import os
import platform
import logging
from datetime import datetime

# ========================================================================== #
# Import logging setup from debug_and_log.py
# ========================================================================== #

from modules.functions.debug_and_log import setup_logging

# ========================================================================== #
# Set up logging
# ========================================================================== #

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
log_directory = os.path.join(script_directory, 'log')

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_filename = f"{datetime.now():%Y-%m-%d-%H-%M}_projekt_creator.debug.log"
log_filepath = os.path.join(log_directory, log_filename)

setup_logging(filename=log_filepath)

# ========================================================================== #
# Define functions for checking the operating system
# ========================================================================== #

def check_operating_system():
    """Check if the operating system is Linux or macOS."""
    os_name = platform.system()
    if os_name == 'Linux':
        logging.info("Operating system is Linux.")
        return 'Linux'
    elif os_name == 'Darwin':
        logging.info("Operating system is macOS.")
        return 'macOS'
    else:
        logging.error(f"Unsupported operating system: {os_name}")
        raise EnvironmentError(f"Unsupported operating system: {os_name}")

# ========================================================================== #
# Define functions to create the project structure
# ========================================================================== #

def create_directory(path):
    """Create a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f"Created directory: {path}")
    else:
        logging.warning(f"Directory already exists: {path}")

def create_project_structure(base_path, project_name):
    """Create the directory structure for a new project."""
    project_path = os.path.join(base_path, project_name)
    
    # Create main project directory
    create_directory(project_path)
    
    # Define subdirectories
    subdirectories = [
        'build',
        'config',
        'doc',
        'experimental',
        'log',
        'pref',
        'script',
        'temp',
        'www',
        'version'
    ]
    
    for subdirectory in subdirectories:
        create_directory(os.path.join(project_path, subdirectory))
    
    # Optionally, create README and .gitignore files
    create_readme(project_path)
    create_gitignore(project_path)

def create_readme(project_path):
    """Create a README.md file in the project directory."""
    readme_path = os.path.join(project_path, 'README.md')
    with open(readme_path, 'w') as readme_file:
        readme_file.write(f"# {os.path.basename(project_path)}\n\n")
        readme_file.write("Project description goes here.\n")
    logging.info(f"Created README.md: {readme_path}")

def create_gitignore(project_path):
    """Create a .gitignore file in the project directory."""
    gitignore_path = os.path.join(project_path, '.gitignore')
    with open(gitignore_path, 'w') as gitignore_file:
        gitignore_file.write("*.pyc\n")
        gitignore_file.write("__pycache__/\n")
        gitignore_file.write("*.pyo\n")
        gitignore_file.write("*.pyd\n")
        gitignore_file.write("*.swp\n")
        gitignore_file.write("*.bak\n")
        gitignore_file.write("*.log\n")
    logging.info(f"Created .gitignore: {gitignore_path}")

# ========================================================================== #
# Main execution
# ========================================================================== #

if __name__ == "__main__":
    try:
        os_type = check_operating_system()
        logging.info(f"Operating System: {os_type}")

        base_path = input("Enter the base path for the project: ")
        project_name = input("Enter the project name: ")

        create_project_structure(base_path, project_name)

        print("Project structure created successfully.")
        logging.info("Project structure created successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
