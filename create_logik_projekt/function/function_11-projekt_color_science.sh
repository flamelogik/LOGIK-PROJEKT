#!/bin/bash

# -------------------------------------------------------------------------- #

# filename: "function_11-projekt_color_science.sh"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines global variables.
# ========================================================================== #

# Declare global variables
declare -g proj_color_science=""

# -------------------------------------------------------------------------- #

# Function to validate user input for color science
validate_color_choice() {
    local choice=$1
    if [[ $choice =~ ^[1-9]|^1[0-2]$ ]]; then
        return 0  # Valid choice
    else
        echo -e "Invalid input. Please enter a number between 1 and 12."
        echo -e "\n$separator\n"
        return 1  # Invalid choice
    fi
}

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to gather projekt color science information
gather_projekt_color_science() {
    # local proj_color_science

    # Check if $has_projekt_setup_template is true
    if [ "$has_projekt_setup_template" = "True" ]; then
        # Read $projekt_setup_template
        if [ -f "$projekt_setup_template" ]; then
            # Read the value from projekt_setup_template
            proj_color_science=$(sed -n '6s/^.*: //p' "$projekt_setup_template")
        else
            echo "Error: $projekt_setup_template not found."
            exit 1
        fi
    else
        while true; do
            # Display menu for projekt color science
            echo -e "  select projekt color policy:\n"
            echo -e "   1. Autodesk ACES 1.0"
            echo -e "   2. Autodesk ACES 1.1"
            echo -e "   3. Autodesk Legacy Workflow"
            echo -e "   4. Autodesk Simple Linear Workflow"
            echo -e "   5. ARRI Alexa LogC V3 (K1S1)"
            echo -e "   6. ARRI Alexa LogC v4"
            echo -e "   7. R3D Log3g10 Red Wide Gamut RGB (Do Not Use)"
            echo -e "   8. Sony Cine+ 709"
            echo -e "   9. Sony Low Contrast 709"
            echo -e "  10. Sony Low Contrast 709 Type A (Alexa Emulation)"
            echo -e "  11. Sony SLog2 709"
            echo -e "  12. Apple Log (ADSK ACES 1.1)"
            echo -e "\n$separator\n"

            # Read user's choice
            read -p "  enter your choice (1 to 12): " color_choice
            echo -e "\n$separator\n"

            # Validate user's choice
            if validate_color_choice "$color_choice"; then
                break  # Break out of the loop if the choice is valid
            fi
        done

        # Handle user's choice
        case $color_choice in
            1)
                proj_color_science="adsk_aces_1"
                ;;
            2)
                proj_color_science="adsk_aces_11"
                ;;
            3)
                proj_color_science="adsk_legacy"
                ;;
            4)
                proj_color_science="adsk_linear"
                ;;
            5)
                proj_color_science="arri_logc_v3"
                ;;
            6)
                proj_color_science="arri_logc_v4"
                ;;
            7)
                proj_color_science="aces_11_sdr"
                ;;
            8)
                proj_color_science="sony_cine_709"
                ;;
            9)
                proj_color_science="sony_lc_709"
                ;;
            10)
                proj_color_science="sony_lca_709"
                ;;
            11)
                proj_color_science="sony_slog2_709"
                ;;
            12)
                proj_color_science="adsk_aces_11"
                ;;
        esac
    fi

    # ---------------------------------------------------------------------- #

    # Display the projekt color science
    echo -e "  color policy:        $proj_color_science"
    echo -e "\n$separator\n"

    # ---------------------------------------------------------------------- #

    # Write the projekt information into the projekt_setup_file
    echo "projekt color science: $proj_color_science" >> "$projekt_setup_file"

    # ---------------------------------------------------------------------- #

    # Write the information into the projekt_setup_template
    echo "projekt color science: $proj_color_science" >> "$projekt_setup_template"

}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Call the function to gather projekt color science information
# gather_projekt_color_science

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    gather_projekt_framerate
fi

# Now the global variables can be accessed wherever needed
# echo -e "  color policy:     $proj_color_science"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #
