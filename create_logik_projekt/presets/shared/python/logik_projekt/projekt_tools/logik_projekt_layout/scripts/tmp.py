import os

# ========================================================================== #
# This section locates the running script and the related directories.
# ========================================================================== #

# Get the path to this script
path_to_this_script = os.path.dirname(os.path.abspath(__file__))

# Get the directory of the script
script_dir = os.path.dirname(__file__)

# Change directory to script_dir
os.chdir(script_dir)

# -------------------------------------------------------------------------- #

# Get the parent directory
parent_dir = os.path.dirname(script_dir)

# Change directory to script_dir
os.chdir(parent_dir)

# -------------------------------------------------------------------------- #

# Define the target script to analyze
target_script = "create_projekt_layout.py"

# -------------------------------------------------------------------------- #

# Define other directories and subdirectories
config_dir = os.path.join(parent_dir, "config")
scripts_dir = os.path.join(parent_dir, "scripts")
classes_and_functions_dir = os.path.join(scripts_dir, "classes_and_functions")
classes_dir = os.path.join(classes_and_functions_dir, "classes")
functions_dir = os.path.join(classes_and_functions_dir, "functions")
version_dir = os.path.join(parent_dir, "version")
python_script = os.path.join(scripts_dir, target_script)
class_list_file = os.path.join(classes_dir, "class_list.txt")
function_list_file = os.path.join(functions_dir, "function_list.txt")
import_commands_txt = os.path.join(scripts_dir, "import_commands.txt")

# -------------------------------------------------------------------------- #

# Function to create directories if they don't exist
def create_directories():
    print("Creating necessary directories...")
    os.makedirs(classes_and_functions_dir, exist_ok=True)
    os.makedirs(classes_dir, exist_ok=True)
    os.makedirs(functions_dir, exist_ok=True)

# ========================================================================== #
# This section echoes information to the shell.
# ========================================================================== #

# Print the paths for verification
print("Path to this script:", os.path.basename(path_to_this_script))
print("Parent directory:   ", os.path.basename(parent_dir))
print("Config directory:   ", os.path.basename(config_dir))
print("Scripts directory:  ", os.path.basename(scripts_dir))
# print("Classes and functions directory:", os.path.basename(classes_and_functions_dir))
print("Classes directory:  ", os.path.basename(classes_dir))
print("Functions directory:", os.path.basename(functions_dir))
print("Version directory:  ", os.path.basename(version_dir))
# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-12 - 15:37:50
# comments:              Added function to read directories from JSON files.
# -------------------------------------------------------------------------- #
# version:               0.0.6
# modified:              2024-05-12 - 18:16:05
# comments:              Added a 'separators' function and tested in flame 2025.
