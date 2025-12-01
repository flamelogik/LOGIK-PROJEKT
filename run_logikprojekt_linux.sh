#!/bin/bash
# Get the directory where the script is located, which is the project root
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

# Change to the project root directory
cd "$SCRIPT__DIR" || exit

# Set PYTHONPATH to the project root
export PYTHONPATH="$SCRIPT_DIR"

# Run the python application as a module
/opt/Autodesk/python/2026.1/bin/python -m src.app
