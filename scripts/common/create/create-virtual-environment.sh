#!/bin/bash
# create-virtual-environment.sh
# Creates and initializes a virtual environment

# -------------------------------------------------------------------------- #
# Script Execution Options
# -------------------------------------------------------------------------- #

# Uncomment these settings for stricter bash execution
set -e           # Exit on any errors
# set -u           # Exit if any variable is used without being defined
# set -o pipefail  # Exit if any command in a pipeline fails
# set -x           # Print each command before execution

# -------------------------------------------------------------------------- #
# Virtual Environment Functions
# -------------------------------------------------------------------------- #

function check_system_dependencies() {
    echo "Checking system dependencies..."

    # Initialize arrays for different package managers
    local dnf_packages=("python3-devel" "gobject-introspection-devel" "cairo-devel" "pkg-config")
    local apt_packages=("python3-dev" "libgirepository1.0-dev" "libcairo2-dev" "pkg-config")
    local missing_packages=()

    # Check if we're on a system that uses dnf (Fedora/RHEL/CentOS)
    if command -v dnf >/dev/null 2>&1; then
        echo "Detected DNF package manager"

        # Check for required packages
        for pkg in "${dnf_packages[@]}"; do
            if ! dnf list installed "$pkg" >/dev/null 2>&1; then
                missing_packages+=("$pkg")
            fi
        done

        if [ ${#missing_packages[@]} -gt 0 ]; then
            echo "The following packages are missing and may be required for compilation:"
            for pkg in "${missing_packages[@]}"; do
                echo "  - $pkg"
            done
            echo "Consider installing them with: sudo dnf install ${missing_packages[*]}"

            # Ask user if they want to install these packages
            read -p "Do you want to install these packages now? (y/n): " install_deps
            if [ "$install_deps" = "y" ] || [ "$install_deps" = "Y" ]; then
                echo "Running: sudo dnf install ${missing_packages[*]}"
                sudo dnf install -y "${missing_packages[@]}"
            else
                echo "Continuing without installing system dependencies..."
            fi
        else
            echo "All required system packages are already installed."
        fi
    # Check if we're on a system that uses apt (Debian/Ubuntu)
    elif command -v apt-get >/dev/null 2>&1; then
        echo "Detected APT package manager"

        # Check for required packages
        for pkg in "${apt_packages[@]}"; do
            if ! dpkg -l "$pkg" >/dev/null 2>&1; then
                missing_packages+=("$pkg")
            fi
        done

        if [ ${#missing_packages[@]} -gt 0 ]; then
            echo "The following packages are missing and may be required for compilation:"
            for pkg in "${missing_packages[@]}"; do
                echo "  - $pkg"
            done
            echo "Consider installing them with: sudo apt-get install ${missing_packages[*]}"

            # Ask user if they want to install these packages
            read -p "Do you want to install these packages now? (y/n): " install_deps
            if [ "$install_deps" = "y" ] || [ "$install_deps" = "Y" ]; then
                echo "Running: sudo apt-get install ${missing_packages[*]}"
                sudo apt-get update
                sudo apt-get install -y "${missing_packages[@]}"
            else
                echo "Continuing without installing system dependencies..."
            fi
        else
            echo "All required system packages are already installed."
        fi
    else
        echo "Unknown package manager. Please install the following dependencies manually:"
        echo "  - Python development headers"
        echo "  - GObject Introspection development headers"
        echo "  - Cairo development headers"
        echo "  - pkg-config"
    fi
}

function create_virtual_environment() {
    display_section_header "Virtual Environment Setup"

    # Check system dependencies before creating the virtual environment
    check_system_dependencies

    # Check if virtual environment exists
    if [ -d "$venv_dir" ]; then
        echo "Virtual environment already exists at: $venv_dir"
        read -p "Do you want to remove and recreate it? (y/n): " recreate_venv
        if [ "$recreate_venv" = "y" ] || [ "$recreate_venv" = "Y" ]; then
            echo "Removing existing virtual environment..."
            rm -rf "$venv_dir"
        else
            echo "Keeping existing virtual environment. Exiting."
            exit 0
        fi
    fi

    # Create the virtual environment
    echo "Creating virtual environment at: $venv_dir"
    "$adsk_python_path" -m venv "$venv_dir"

    # Activate the virtual environment
    source "$venv_dir/bin/activate"

    # Check if virtual environment activation was successful
    if [[ "$virtual_env" != "$venv_dir" ]]; then
        echo "ERROR: Failed to activate virtual environment."
        exit 1
    fi

    echo "Virtual environment activated: $virtual_env"

    # Upgrade pip in the virtual environment
    echo "Upgrading pip in virtual environment..."
    python -m pip install --upgrade pip

    # Install basic requirements
    echo "Installing basic requirements..."
    python -m pip install wheel setuptools
}

function handle_package_installation() {
    display_section_header "Package Installation"

    # Prompt user for installation method
    echo "How would you like to include Autodesk Python packages in your virtual environment?"
    echo "1. Install from requirements.txt (recommended for most cases)"
    echo "2. Create symlinks to Autodesk packages (faster but may cause issues)"
    echo "3. Skip package installation"
    read -p "Choose an option (1-3): " install_option

    case $install_option in
        1)
            install_from_requirements
            ;;
        2)
            create_package_symlinks
            ;;
        3)
            echo "Skipping package installation. You can install them later with:"
            echo "pip install -r $requirements_file"
            ;;
        *)
            echo "Invalid option. Skipping package installation."
            echo "You can install packages later with: pip install -r $requirements_file"
            ;;
    esac

    # Install non-standard packages if available
    install_non_standard_packages

    # Deactivate the virtual environment
    deactivate
}

function install_from_requirements() {
    echo "Installing packages from requirements.txt..."

    # First try to install all packages at once
    if ! python -m pip install -r "$requirements_file"; then
        echo "Some packages failed to install. Trying to install each package individually..."

        # Create a file to track packages that failed to install
failed_packages="$tmp_dir/adsk_packages_info/failed_packages.txt"
        > "$failed_packages"

        # Read requirements file line by line
        while read -r req; do
            # Skip empty lines and comments
            [[ -z "$req" || "$req" == \#* ]] && continue

            echo "Attempting to install: $req"
            if ! python -m pip install "$req"; then
                echo "Failed to install $req - skipping"
                echo "$req" >> "$failed_packages"
            fi
        done < "$requirements_file"

        echo "The following packages failed to install:"
        cat "$failed_packages"
        echo "You may need to install system dependencies or build them manually."
    fi
}

function create_package_symlinks() {
    echo "Creating symlinks to Autodesk packages..."

    # Get virtual environment site-packages
venv_site_packages=$(python -c "import site; print(site.getsitepackages()[0])")

    echo "Running symlinks script..."
    python "$symlinks_script" "$adsk_site_packages" "$venv_site_packages"

    # Create .pth file to add Autodesk site-packages to Python path
adsk_pth_file="$venv_site_packages/autodesk.pth"
    echo "Creating .pth file at: $adsk_pth_file"
    echo "$adsk_site_packages" > "$adsk_pth_file"
}

function install_non_standard_packages() {
    # Check if non-standard packages list exists
    if [ -f "$non_standard_packages_list" ]; then
        echo "Installing non-standard packages from: $non_standard_packages_list"

        # Ask user if they want to install non-standard packages
        read -p "Do you want to install non-standard packages found in your system? (y/n): " install_non_std
        if [ "$install_non_std" != "y" ] && [ "$install_non_std" != "Y" ]; then
            echo "Skipping non-standard package installation."
            return
        fi

        # Create a file to track packages that failed to install
failed_non_std_packages="$tmp_dir/adsk_packages_info/failed_non_std_packages.txt"
        > "$failed_non_std_packages"

        # Read each line from the non-standard packages list
        while read -r pkg; do
            # Skip empty lines and comments
            [[ -z "$pkg" || "$pkg" == \#* ]] && continue

            echo "Attempting to install non-standard package: $pkg"
            if ! python -m pip install "$pkg"; then
                echo "Failed to install $pkg - skipping"
                echo "$pkg" >> "$failed_non_std_packages"
            fi
        done < "$non_standard_packages_list"

        if [ -s "$failed_non_std_packages" ]; then
            echo "The following non-standard packages failed to install:"
            cat "$failed_non_std_packages"
        else
            echo "All non-standard packages were installed successfully."
        fi
    else
        echo "No non-standard packages list found. Skipping non-standard package installation."
    fi
}

# -------------------------------------------------------------------------- #
# Changelist:
# -------------------------------------------------------------------------- #