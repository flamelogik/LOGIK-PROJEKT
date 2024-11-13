#!/bin/bash

# Set the project directory (main directory)
PROJECT_DIR="$(pwd)"

# Set the SQLite database file
DB_FILE="$PROJECT_DIR/project_db.sqlite"

# Function to initialize the SQLite database
initialize_db() {
    echo "Initializing SQLite database..."

    # Remove existing database file if it exists
    if [ -f "$DB_FILE" ]; then
        rm "$DB_FILE"
    fi

    # Create a new SQLite database and table
    sqlite3 "$DB_FILE" "
    CREATE TABLE files (
        id INTEGER PRIMARY KEY,
        path TEXT UNIQUE,
        type TEXT,
        size INTEGER,
        permissions TEXT,
        last_modified TIMESTAMP
    );
    "

    # Populate the database with the current directory structure
    while IFS= read -r file; do
        FILE_TYPE=$( [ -d "$file" ] && echo "directory" || echo "file" )
        LAST_MODIFIED=$(stat -c %Y "$file")
        # sqlite3 "$DB_FILE" "INSERT INTO files (path, type, last_modified) VALUES ('$file', '$FILE_TYPE', $LAST_MODIFIED);"
        # Inside the while loop
        FILE_SIZE=$(stat -c %s "$file")
        PERMISSIONS=$(stat -c %A "$file")
        sqlite3 "$DB_FILE" "INSERT INTO files (path, type, size, permissions, last_modified) VALUES ('$file', '$FILE_TYPE', $FILE_SIZE, '$PERMISSIONS', $LAST_MODIFIED);"
    done < <(find "$PROJECT_DIR" -type f -o -type d)

    echo "Database initialized at $DB_FILE"
}

# Function to update the database on file system changes
update_db() {
    EVENT=$1
    FILE_PATH=$2

    # Normalize the event (e.g., CREATE, DELETE, MODIFY)
    EVENT_TYPE=$(echo "$EVENT" | awk '{print $1}')

    # Get the last modified time
    LAST_MODIFIED=$(stat -c %Y "$FILE_PATH" 2>/dev/null || echo 0)

    case "$EVENT_TYPE" in
        CREATE|MOVED_TO)
            FILE_TYPE=$( [ -d "$FILE_PATH" ] && echo "directory" || echo "file" )
            sqlite3 "$DB_FILE" "
            INSERT OR REPLACE INTO files (path, type, last_modified) VALUES ('$FILE_PATH', '$FILE_TYPE', $LAST_MODIFIED);
            "
            echo "Added $FILE_PATH to database."
            ;;
        MODIFY)
            FILE_SIZE=$(stat -c %s "$FILE_PATH")
            PERMISSIONS=$(stat -c %A "$FILE_PATH")
            sqlite3 "$DB_FILE" "
            UPDATE files SET last_modified=$LAST_MODIFIED, size=$FILE_SIZE, permissions='$PERMISSIONS' WHERE path='$FILE_PATH';
            "

            echo "Updated $FILE_PATH in database."
            ;;
        DELETE|MOVED_FROM)
            sqlite3 "$DB_FILE" "
            DELETE FROM files WHERE path='$FILE_PATH';
            "
            echo "Removed $FILE_PATH from database."
            ;;
        *)
            echo "Unhandled event: $EVENT_TYPE"
            ;;
    esac
}

# Function to monitor the project directory for changes
monitor_changes() {
    echo "Monitoring $PROJECT_DIR for changes..."
    inotifywait -m -r -e create -e delete -e modify -e moved_from -e moved_to --format '%e %w%f' "$PROJECT_DIR" | while read event fullpath
    do
        update_db "$event" "$fullpath"
    done
}

# Initialize the database
initialize_db

# Monitor the directory for changes
monitor_changes
