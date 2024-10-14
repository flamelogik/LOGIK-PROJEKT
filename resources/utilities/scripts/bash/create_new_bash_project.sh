#!/bin/bash

set -ex

# ========================================================================== #
# This section locates the running script and the related directories.
# ========================================================================== #

# Get the directory of this script
path_to_here="$(dirname "$0")"

# Get the parent directory
parent_dir="$(dirname "$path_to_here")"

# Change directory to path_to_here
cd "$parent_dir" || exit

# -------------------------------------------------------------------------- #

# Function to sanitize project name
sanitize_name() {
    local name="$1"
    name=$(echo "$name" | tr '[:upper:]' '[:lower:]')
    name=$(echo "$name" | sed 's/[^a-z0-9_]/_/g')
    name=$(echo "$name" | sed 's/_+/_/g')
    name=$(echo "$name" | sed 's/^_//;s/_$//')
    echo "$name"
}

# Prompt user for project name
read -p "Enter the name of your new bash project: " USER_INPUT

# Sanitize the project name
PROJECT_NAME=$(sanitize_name "$USER_INPUT")

# Check if the sanitized name is empty
if [ -z "$PROJECT_NAME" ]; then
    echo "Error: Invalid project name. Please use at least one alphanumeric character."
    exit 1
fi

BASE_DIR="$path_to_here"
TEMPLATE_DIR="$BASE_DIR/bash_project_template"
PROJECT_DIR="$BASE_DIR/$PROJECT_NAME"

# Check if the template directory exists
if [ ! -d "$TEMPLATE_DIR" ]; then
    echo "Error: Template directory '$TEMPLATE_DIR' does not exist."
    exit 1
fi

# Check if the project already exists
if [ -d "$PROJECT_DIR" ]; then
    echo "Error: A project with the name '$PROJECT_NAME' already exists."
    exit 1
fi

# Copy the template directory to create the new project
cp -R "$TEMPLATE_DIR" "$PROJECT_DIR"

# Rename the main script file
mv "$PROJECT_DIR/scripts/bash_project_template.sh" "$PROJECT_DIR/scripts/$PROJECT_NAME.sh"

# Update the main script file
MAIN_SCRIPT="$PROJECT_DIR/scripts/$PROJECT_NAME.sh"
TODAY=$(date +%Y-%m-%d)

sed -i \
    -e "s/File Name:        bash_project_template\.sh/File Name:        $PROJECT_NAME.sh/" \
    -e "s/Version:          0\.0\.0/Version:          0.0.0/" \
    -e "s/Created:          2024-01-01/Created:          $TODAY/" \
    -e "s/Modified:         2024-12-31/Modified:         $TODAY/" \
    -e "s/Description:      This script is a template for bash projects\./Description:      This script is for the $PROJECT_NAME project./" \
    "$MAIN_SCRIPT"

# Update the version.json file
VERSION_FILE="$PROJECT_DIR/version/version.json"
if [ -f "$VERSION_FILE" ]; then
    sed -i \
        -e 's/"version": ".*"/"version": "1.0.0"/' \
        -e "s/\"last_updated\": \".*\"/\"last_updated\": \"$TODAY\"/" \
        "$VERSION_FILE"
fi

echo "New bash project '$PROJECT_NAME' has been created in $PROJECT_DIR"
echo "Main script file: $MAIN_SCRIPT"
echo "Remember to update the project description and other details in the script file."