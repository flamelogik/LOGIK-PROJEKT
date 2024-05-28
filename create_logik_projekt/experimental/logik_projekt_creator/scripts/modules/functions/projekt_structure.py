import os
import logging

def create_directory(path):
    """Create a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f"Created directory: {path}")
    else:
        logging.warning(f"Directory already exists: {path}")

def create_logik_projekt_structure(base_path, projekt_name):
    """Create the directory structure for a new LOGIK-PROJEKT."""
    projekt_path = os.path.join(base_path, projekt_name)
    
    # Create main LOGIK-PROJEKT directory
    create_directory(projekt_path)
    
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
        create_directory(os.path.join(projekt_path, subdirectory))
