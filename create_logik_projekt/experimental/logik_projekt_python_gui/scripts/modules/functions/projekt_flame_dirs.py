# import os
# import json

# # Function to determine the app_dir based on the parent directory of the script
# def get_app_dir():
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     while True:
#         parent_dir = os.path.dirname(current_dir)
#         if parent_dir == current_dir or os.path.basename(parent_dir) == "logik_projekt_python_gui":
#             break
#         current_dir = parent_dir
#     return parent_dir

# # Define directory variables
# app_dir = get_app_dir()
# config_dir = os.path.join(app_dir, 'config')
# scripts_dir = os.path.join(app_dir, 'scripts')
# modules_dir = os.path.join(scripts_dir, 'modules')
# classes_dir = os.path.join(modules_dir, 'classes')
# functions_dir = os.path.join(modules_dir, 'functions')
# gui_components_dir = os.path.join(modules_dir, 'gui_components')
# version_dir = os.path.join(app_dir, 'version')

# # Define global variables
# flame_projekt_dir = ""

# # Define projekt flame projekt name
# projekt_name = "TEST"

# # Function to create the flame projekt directory
# def create_projekt_directory():
#     global flame_projekt_dir
#     # Set the umask to 0
#     os.umask(0)
    
#     # Create the flame projekt directory
#     # flame_projekt_dir = "/opt/Autodesk/projekt/" + name
#     flame_projekt_dir = "/JOBS/PYTHON_TESTING/projekt/" + projekt_name  # TESTING
#     print("  creating flame projekt directory:")
#     print("\n" + "=" * 70 + "\n")
    
#     if not os.path.exists(flame_projekt_dir):
#         os.makedirs(flame_projekt_dir, mode=0o2777, exist_ok=True)
#         print("  ", flame_projekt_dir)
    
#     print("\n" + "=" * 70 + "\n")
#     print("  flame projekt directory created.")
#     print("\n" + "=" * 70 + "\n")
#     print("  creating flame projekt setup directories:")
#     print("\n" + "=" * 70 + "\n")

# # Function to create the flame projekt setup directories
# def create_projekt_setup_directories():
#     try:
#         with open(os.path.join(config_dir, 'projekt_flame_dirs.json'), 'r') as file:
#             data = json.load(file)
#             flame_proj_setup_dirs = data['flame_proj_setup_dirs']
#     except FileNotFoundError:
#         print("Error: The file 'projekt_flame_dirs.json' was not found in the config directory.")
#         return

#     # Create the directories
#     for flame_proj_setup_dir in flame_proj_setup_dirs:
#         dir_path = os.path.join(flame_projekt_dir, flame_proj_setup_dir)
#         os.makedirs(dir_path, mode=0o2777, exist_ok=True)
#         print("  ", dir_path)
        
#     print("\n" + "=" * 70 + "\n")
#     print("  flame projekt setup directories created.")
#     print("\n" + "=" * 70 + "\n")

# # Function to create the flame projekt directories
# def create_flame_projekt_directories():
#     create_projekt_directory()
#     create_projekt_setup_directories()

# # Call the function to create the flame projekt directories
# if __name__ == "__main__":
#     name = ""  # Add your desired projekt name here
#     create_flame_projekt_directories()










# import os
# import json

# # Function to determine the app_dir based on the parent directory of the script
# def get_app_dir():
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     while True:
#         parent_dir = os.path.dirname(current_dir)
#         if parent_dir == current_dir or os.path.basename(parent_dir) == "logik_projekt_python_gui":
#             break
#         current_dir = parent_dir
#     return parent_dir

# # Define directory variables
# app_dir = get_app_dir()
# config_dir = os.path.join(app_dir, 'config')
# scripts_dir = os.path.join(app_dir, 'scripts')
# modules_dir = os.path.join(scripts_dir, 'modules')
# classes_dir = os.path.join(modules_dir, 'classes')
# functions_dir = os.path.join(modules_dir, 'functions')
# gui_components_dir = os.path.join(modules_dir, 'gui_components')
# version_dir = os.path.join(app_dir, 'version')

# # Define global variables
# flame_projekt_dir = ""
# jobs_dir = "/JOBS"

# # Define flame projekt name
# flame_projekt_name = "TEST"

# # Function to create the flame projekt directory
# def create_flame_projekt_directory():
#     global flame_projekt_dir
#     # Set the umask to 0
#     os.umask(0)
    
#     # Create the flame projekt directory
#     flame_projekt_dir = os.path.join(jobs_dir, "PYTHON_TESTING/projekt", flame_projekt_name)  # TESTING
#     print("  creating flame projekt directory:")
#     print("\n" + "=" * 70 + "\n")
    
#     if not os.path.exists(flame_projekt_dir):
#         os.makedirs(flame_projekt_dir, mode=0o2777, exist_ok=True)
#         print("  ", flame_projekt_dir)
    
#     print("\n" + "=" * 70 + "\n")
#     print("  flame projekt directory created.")
#     print("\n" + "=" * 70 + "\n")
#     print("  creating flame projekt setup directories:")
#     print("\n" + "=" * 70 + "\n")

# # Function to create the flame projekt setup directories
# def create_flame_setup_directories():
#     try:
#         with open(os.path.join(config_dir, 'projekt_flame_dirs.json'), 'r') as file:
#             data = json.load(file)
#             flame_proj_setup_dirs = data['flame_proj_setup_dirs']
#     except FileNotFoundError:
#         print("Error: The file 'projekt_flame_dirs.json' was not found in the config directory.")
#         return

#     # Create the directories
#     for flame_proj_setup_dir in flame_proj_setup_dirs:
#         dir_path = os.path.join(flame_projekt_dir, flame_proj_setup_dir)
#         os.makedirs(dir_path, mode=0o2777, exist_ok=True)
#         print("  ", dir_path)
        
#     print("\n" + "=" * 70 + "\n")
#     print("  flame projekt setup directories created.")
#     print("\n" + "=" * 70 + "\n")

# # Function to create the flame projekt directories
# def create_flame_projekt_directories():
#     create_flame_projekt_directory()
#     create_flame_setup_directories()

# # Call the function to create the flame projekt directories
# if __name__ == "__main__":
#     name = ""  # Add your desired projekt name here
#     create_flame_projekt_directories()




















# ========================================================================== #
# This section defines the import statements
# ========================================================================== #

import os
import json

# ========================================================================== #
# This function examines and defines the relative script environment
# ========================================================================== #

# Function to determine the app_dir based on the parent directory of the script
def get_app_dir():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while True:
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir or os.path.basename(parent_dir) == "logik_projekt_python_gui":
            break
        current_dir = parent_dir
    return parent_dir

# Define directory variables
app_dir = get_app_dir()
config_dir = os.path.join(app_dir, 'config')
scripts_dir = os.path.join(app_dir, 'scripts')
modules_dir = os.path.join(scripts_dir, 'modules')
classes_dir = os.path.join(modules_dir, 'classes')
functions_dir = os.path.join(modules_dir, 'functions')
gui_components_dir = os.path.join(modules_dir, 'gui_components')
version_dir = os.path.join(app_dir, 'version')

# -------------------------------------------------------------------------- #

# Define the jobs_dir
jobs_dir = "/JOBS"

# Define global variables
flame_projekt_dir = ""
logik_projekt_dir = ""

# Define flame projekt name
flame_projekt_name = "TEST"


# Function to create the flame projekt directory
def create_flame_projekt_directory():
    global flame_projekt_dir
    # Set the umask to 0
    os.umask(0)
    
    # Create the flame projekt directory
    flame_projekt_dir = os.path.join(jobs_dir, "PYTHON_TESTING/projekt", flame_projekt_name)  # TESTING
    print("  creating flame projekt directory:")
    print("\n" + "=" * 70 + "\n")
    
    if not os.path.exists(flame_projekt_dir):
        os.makedirs(flame_projekt_dir, mode=0o2777, exist_ok=True)
        print("  ", flame_projekt_dir)
    
    print("\n" + "=" * 70 + "\n")
    print("  flame projekt directory created.")
    print("\n" + "=" * 70 + "\n")
    print("  creating flame projekt setup directories:")
    print("\n" + "=" * 70 + "\n")

# Function to create the flame projekt setup directories
def create_flame_setup_directories():
    try:
        with open(os.path.join(config_dir, 'projekt_flame_dirs.json'), 'r') as file:
            data = json.load(file)
            flame_proj_setup_dirs = data['flame_proj_setup_dirs']
    except FileNotFoundError:
        print("Error: The file 'projekt_flame_dirs.json' was not found in the config directory.")
        return

    # Create the directories
    for flame_proj_setup_dir in flame_proj_setup_dirs:
        dir_path = os.path.join(flame_projekt_dir, flame_proj_setup_dir)
        os.makedirs(dir_path, mode=0o2777, exist_ok=True)
        print("  ", dir_path)
        
    print("\n" + "=" * 70 + "\n")
    print("  flame projekt setup directories created.")
    print("\n" + "=" * 70 + "\n")

# Function to create the logik projekt directory
def create_logik_projekt_directory():
    global logik_projekt_dir
    # Set the umask to 0
    os.umask(0)
    
    # Create the logik projekt directory
    logik_proj_dir = os.path.join(jobs_dir, "PYTHON_TESTING/projekt", logik_projekt_dir)  # TESTING
    print("  creating logik projekt directory:")
    print("\n" + "=" * 70 + "\n")
    
    if not os.path.exists(logik_proj_dir):
        os.makedirs(logik_proj_dir, mode=0o2777, exist_ok=True)
        print("  ", logik_proj_dir)
    
    print("\n" + "=" * 70 + "\n")
    print("  logik projekt directory created.")
    print("\n" + "=" * 70 + "\n")
    print("  creating logik projekt setup directories:")
    print("\n" + "=" * 70 + "\n")

# Function to create the logik projekt setup directories
def create_logik_projekt_subdirectories():
    try:
        with open(os.path.join(config_dir, 'projekt_dirs.json'), 'r') as file:
            data = json.load(file)
            logik_proj_setup_dirs = data['logik_proj_setup_dirs']
    except FileNotFoundError:
        print("Error: The file 'projekt_dirs.json' was not found in the config directory.")
        return

    # Create the directories
    for logik_proj_setup_dir in logik_proj_setup_dirs:
        dir_path = os.path.join(logik_proj_dir, logik_proj_setup_dir)
        os.makedirs(dir_path, mode=0o2777, exist_ok=True)
        print("  ", dir_path)
        
    print("\n" + "=" * 70 + "\n")
    print("  logik projekt setup directories created.")
    print("\n" + "=" * 70 + "\n")

# Function to create the flame projekt directories
def create_flame_projekt_directories():
    create_flame_projekt_directory()
    create_flame_setup_directories()

# Function to create the logik projekt directories
def create_logik_projekt_directories():
    create_logik_projekt_directory()
    create_logik_projekt_subdirectories()

# Call the function to create the flame projekt directories
if __name__ == "__main__":
    name = ""  # Add your desired projekt name here
    create_flame_projekt_directories()
    create_logik_projekt_directories()
