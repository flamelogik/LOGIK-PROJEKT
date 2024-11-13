#!/bin/bash

set -ex

# Define the path to the .env file relative to the script's location
ENV_FILE="$(dirname "$0")/../../.env"

# Load environment variables from .env file
if [ -f "$ENV_FILE" ]; then
    source "$ENV_FILE"
else
    echo ".env file not found!"
    exit 1
fi

NAME='123_ABC_DEF'
SUBDOMAIN='TRANSCODES'
MESSAGE="Welcome to the $NAME:$SUBDOMAIN portal"
R1_EMAIL="randy.mcentee@1986studios.com"
ACCESS_CODE="$SUBDOMAIN"
DOWNLOAD_PASSWORD="$NAME"
CUSTOM_EXPIRY_DAYS=5
TEAM_ID="1986-PROJEKT-USERS"

curl -d '{
    "name": "'"$NAME"'",
    "message": "'"$MESSAGE"'",
    "subdomain": "'"$SUBDOMAIN"'",
    "recipients": ["'"$R1_EMAIL"'"],
    "access_code": "'"$ACCESS_CODE"'",
    "has_access_code": true,
    "download_password": "'"$DOWNLOAD_PASSWORD"'",
    "has_download_password": true,
    "custom_expiry_days": '"$CUSTOM_EXPIRY_DAYS"'
}' \
-H "X-API-KEY: $MASV_IO_API_KEY" \
-H "Content-Type: application/json" \
-X POST "https://api.massive.app/v1/teams/$TEAM_ID/portals"

# # Name                                Type                          Required                  Description

# # --------------------------------------------------------------------------- #

# # REQUIRED PARAMETERS
# NAME=String                                             # Name of the Portal to create.
# SUBDOMAIN=String                                        # Subdomain of the Portal to create.

# # --------------------------------------------------------------------------- #

# # OPTIONAL PARAMETERS
# MESSAGE="Welcome to the $NAME:$SUBDOMAIN portal"        # Message displayed on the Portal upload page.

# HAS_ACCESS_CODE=true                                    # Enable/disable access code for Portal page.

# ACCESS_CODE="$SUBDOMAIN"                                # Access code to be able to access Portal upload page.
#                                                         # Must be set if has_access_code is true.

# ACTIVE=false                                            # Enable/disable Portal page.
#                                                         # Default is false.

# LOGO_URL=String                                         # URL for logo to be displayed on Portal page.

# BACKGROUND_URL=String                                   # URL for background image of the Portal page.

# PRIMARY_COLOR=String                                    # HTML hex code for primary color used on Portal page.

# RECIPIENTS=Array of Strings                             # Email(s) that will receive notifications for Portal uploads.

# HAS_DOWNLOAD_PASSWORD=true                              # Enable/disable download password for Portal packages.
#                                                         # Default is false.

# DOWNLOAD_PASSWORD="$NAME"                               # Password to protect download access on any package uploaded to this Portal.
#                                                         # Must be set if has_download_password is true.

# CUSTOM_EXPIRY_DAYS=5                                    # Length of storage days for packages that belong to the Portal.
#                                                         # Must be from -1 to 65535.

# CLOUD_CONNECTIONS=Array of cloud connections            # Cloud connections attached to the Portal.
#                                                         # Must be set if configure_cloud_connections is true. See Cloud connect.

# DISABLE_UPLOAD_RECEIPT=false                            # Enable/disable the sending of a confirmation email to the uploader
#                                                         # Default is false.

# CUSTOM_WEBHOOKS=Array of custom webhooks                # Custom webhooks attached to the Portal.
#                                                         # See Custom webhooks.

# TAG=Tag                                                 # An optional tag object used to assign a tag to the new Portal.
#                                                         # When a Portal has a tag, all packages created on the Portal are assigned the Portal's tag.
#                                                         # See Tags.

# ACCESS_LEVEL=String                                     # Portal access level, regular or private. Default is regular.

# ACCESS_LIST=Array of Strings                            # User membership IDs with access to the private Portal and its received packages.
#                                                         # Leave it empty for regular Portals.

# TEAMSPACE_ID=String                                     # ID of the Teamspace that the Portal should be bound to.
#                                                         # To attach the Portal to a Team and not a Teamspace, either use the empty string or omit this object.

# TERMS_OF_SERVICE_ENABLED=false                          # Enable/disable the display of the Terms of Service checkbox.
#                                                         # Default is false.

# TERMS_OF_SERVICE=Terms of service                       # Custom terms of service required to start collecting files.
#                                                         # If terms_of_service_enabled set to true this object cannot be empty or omitted.

# PACKAGE_SIZE_RESTRICTION_ENABLED=false                  # Enable/disable restrictions on the package size, as well as the number and size of files included in the Package.
#                                                         # If it is set to true then one or more of max_package_size, max_file_size, or max_file_count must be provided.
#                                                         # Default is false.

# MAX_PACKAGE_SIZE=Integer                                # The maximum Package size allowed for Users to input and save through the Portal.

# MAX_FILE_SIZE=Integer                                   # The maximum size, in bytes, of an individual file allowed for Users to input and save through the Portal.

# MAX_FILE_COUNT=Integer                                  # The maximum number of files allowed for the Portal upload.

# FILE_TYPE_RESTRICTION_ENABLED=flase                     # Enable/disable list of File types allowed for Users to upload.
#                                                         # If file_type_restriction_enabled set to true, this list cannot be empty or omitted. Default is false.

# FILE_TYPES=Array of Strings                             # File types allowed for upload only.
#                                                         # File type is presented as a file extension prefixed with a dot like ".mov" or ".mp4".

# EXPIRY_ENABLED=flase                                    # Enable/disable expiry for the Portal.
#                                                         # When enabled this will make the Portal unavailable for new uploads once the expiry datetime has passed.
#                                                         # Default is false.

# EXPIRY=String                                           # Date-time expiry for the Portal.
#                                                         # Default: 0001-01-01T00:00:00.000Z.
#                                                         # Accepted Format: ISO 8601.

# PACKAGE_NAME_FORMAT="Package name format "              # Accepted syntax for package names sent through this Portal.
#                                                         # MASV enforces this format only when package_name_format_enabled is true.

# PACKAGE_NAME_FORMAT_ENABLED=false                       # Enable/disable encorcement of package_name_format
