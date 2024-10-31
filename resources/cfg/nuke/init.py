import nuke
import os



print("# -------------------------------------------------------------------------- #")

# ========================================================================== #
# This section sets the color management knob to OCIO.
# ========================================================================== #

nuke.knobDefault('Root.colorManagement', 'OCIO')


# ========================================================================== #
# This section imports projekt_core
# ========================================================================== #

nuke.pluginAddPath('./repo/projekt_core_v0.0.1',addToSysPath=True)

# -------------------------------------------------------------------------- #
try:
    import projekt_core
    print("projekt_core imported successfully.")
except ImportError as e:
    print(f"Error importing core: {e}")

from projekt_core import settings


# ========================================================================== #
# This section loads the gizmoUtilities module
# ========================================================================== #
#  loading in init.py allows gizmos to be available in render/terminal mode.

try:
    import projekt_core.gizmoUtilities
    print("projekt_core.gizmoUtilities imported successfully.")
except ImportError as e:
    print(f"Error importing gizmoUtilities: {e}")

projekt_core.gizmoUtilities.main()



# ========================================================================== #
# This section adds the repo folder to the plugin path.
# ========================================================================== #

# - to download 3rd party tools run - python ./software/nuke/repo/download_tools.py
# -------------------------------------------------------------------------- #

# read the init.py file in repo folder to load additinoal tools:
nuke.pluginAddPath('./repo')


# ========================================================================== #
# This section defines third party imports.
# ========================================================================== #

# -------------------------------------------------------------------------- #


# ========================================================================== #
# This section defines ofx and plugin imports.
# ========================================================================== #

# -------------------------------------------------------------------------- #


# ========================================================================== #
# This section defines environment variable checking and printing.
# ========================================================================== #

# Function to check and print environment variables
def check_and_print_env_vars(var_names):
    print("# -------------------------------------------------------------------------- #")
    for var_name in var_names:
        var_value = os.environ.get(var_name)

        print(f"{var_name}: {var_value}")
    print("# -------------------------------------------------------------------------- #")

# List of environment variable names
env_vars = [
    "PROJEKT_ROOT",
    "PROJEKT_NAME",
    "PROJEKT_PATH",
    "PROJEKT_OS",
    "PROJEKT_PIPELINE_ROOT",
    "PROJEKT_PIPE_TEMPLATES",

]

# Call the function to check and print environment variables
check_and_print_env_vars(env_vars)
