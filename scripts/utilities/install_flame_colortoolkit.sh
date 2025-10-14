#!/bin/bash
#
# Flame ColorToolKit Installer
#
# This script runs the necessary components in order to
# generate and install the OCIO-based Flame ColorToolKit.
#

# --- Configuration ---
# Get the directory where the script is located, which is the project root
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
PREF_FILE="$SCRIPT_DIR/install/current_adsk_python_version.pref"

SCRIPTS_TO_RUN=(
    "src/utils/common/create/create_ocio_config_json_file.py"
    "src/utils/common/create/create_ocio_conversion_tasks.py"
    "src/utils/common/create/create_ocio_flame_colortoolkit.py"
)
# ---------------------

echo "--- Starting Flame ColorToolKit Installation ---"

# Check for and read the python path preference file
if [ ! -f "$PREF_FILE" ]; then
    echo "Error: Autodesk Python preference file not found at: $PREF_FILE"
    exit 1
fi

ADSK_PYTHON_PATH=$(cat "$PREF_FILE")

if [ ! -x "$ADSK_PYTHON_PATH" ]; then
    echo "Error: Autodesk Python executable not found or is not executable at: $ADSK_PYTHON_PATH"
    exit 1
fi

echo "Using Python interpreter: $ADSK_PYTHON_PATH"

# Change to the project root directory to ensure relative paths work
cd "$SCRIPT_DIR" || exit

# Run the scripts
for script in "${SCRIPTS_TO_RUN[@]}"; do
    echo ""
    echo "--- Running ${script} ---"
    "$ADSK_PYTHON_PATH" "$script"
    
    if [ $? -ne 0 ]; then
        echo "--- Error running ${script} ---"
        echo "Stopping installation."
        exit 1
    fi
    echo "--- Successfully finished ${script} ---"
done

echo ""
echo "*** Flame ColorToolKit installation completed successfully! ***"

exit 0
