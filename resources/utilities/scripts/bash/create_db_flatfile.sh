#!/bin/bash

# Set the project directory (main directory)
PROJECT_DIR="$(pwd)"

# Set the database file
DB_FILE="$PROJECT_DIR/project_db.txt"

# Function to initialize the database with the current directory structure
initialize_db() {
    echo "Initializing database..."
    find "$PROJECT_DIR" -type d -or -type f > "$DB_FILE"
    echo "Database initialized at $DB_FILE"
}

# Function to update the database on file system changes
update_db() {
    EVENT_TYPE=$1
    FILE_PATH=$2

    echo "Filesystem event detected: $EVENT_TYPE on $FILE_PATH"

    if [ "$EVENT_TYPE" == "DELETE" ]; then
        # Remove deleted files from the database
        grep -v "^$FILE_PATH$" "$DB_FILE" > "$DB_FILE.tmp" && mv "$DB_FILE.tmp" "$DB_FILE"
    else
        # Add new or modified files to the database
        if ! grep -q "^$FILE_PATH$" "$DB_FILE"; then
            echo "$FILE_PATH" >> "$DB_FILE"
        fi
    fi
}

# Function to monitor the project directory for changes
monitor_changes() {
    echo "Monitoring $PROJECT_DIR for changes..."
    inotifywait -m -r -e create -e delete -e modify --format '%e %w%f' "$PROJECT_DIR" | while read event fullpath
    do
        update_db "$event" "$fullpath"
    done
}

# Initialize the database if it doesn't exist
if [ ! -f "$DB_FILE" ]; then
    initialize_db
fi

# Monitor the directory for changes
monitor_changes
