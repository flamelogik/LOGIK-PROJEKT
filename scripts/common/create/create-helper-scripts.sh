#!/bin/bash
# create-helper-scripts.sh
# Creates helper scripts for working with the virtual environment

# -------------------------------------------------------------------------- #
# Script Execution Options
# -------------------------------------------------------------------------- #

# Uncomment these settings for stricter bash execution
set -e     # Exit on any errors
# set -u     # Exit if any variable is used without being defined
# set -o pipefail  # Exit if any command in a pipeline fails
# set -x     # Print each command before execution

# -------------------------------------------------------------------------- #
# Script Generator Functions
# -------------------------------------------------------------------------- #

function create_helper_scripts() {
    # Generate symlinks script
    create_python_symlinks_script

    # Generate activation script
    create_py_venv_activation_script
}

function create_py_venv_activation_script() {
    echo "Creating activation script at: $activate_venv_script"

    cat > "$activate_venv_script" << EOF
#!/bin/bash
# Script to activate the virtual environment based on Autodesk Python

# Display Autodesk Python information
echo "Autodesk Python: $adsk_python_path"
echo "Python Version: $python_version_full"

# Activate the virtual environment
source "$venv_dir/bin/activate"
echo "Virtual environment activated: \$virtual_env"

# Add helpful aliases
alias list_adsk_packages="cat $pip_list_file"
alias view_adsk_modules="less $site_modules_file"
alias view_package_details="less $package_info_file"

# Display available commands
echo ""
echo "Available commands:"
echo "  list_adsk_packages    - List all packages from Autodesk Python"
echo "  view_adsk_modules     - View modules in Autodesk site-packages"
echo "  view_package_details  - View detailed package information"
echo ""

# Check Python path
python -c "import sys; print('Python path:'); [print(f'  {p}') for p in sys.path]"
EOF

    chmod +x "$activate_venv_script"
}

# -------------------------------------------------------------------------- #
# Changelist:
# -------------------------------------------------------------------------- #