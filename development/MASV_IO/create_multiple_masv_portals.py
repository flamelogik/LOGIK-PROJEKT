# File Name:        create_multiple_masv_portals.py
# Version:          1.0.0
# Created:          2024-11-01
# Modified:         2024-11-01

# ========================================================================== #
# This section defines the import statements and MASV API configuration.
# ========================================================================== #

import requests
import os

# Load MASV API key from environment variable
API_KEY = os.getenv("MASV_API_KEY")

if not API_KEY:
    raise ValueError("MASV_API_KEY environment variable not set")

BASE_URL = "https://api.massive.io/v1/portals"

# Paths and names for each portal
portal_paths = {
    "Graded Footage": "/PROJEKTS/$my_projekt/assets/footage/graded",
    "Raw Footage": "/PROJEKTS/$my_projekt/assets/footage/raw",
    "Transcoded Footage": "/PROJEKTS/$my_projekt/assets/footage/transcodes"
}

# ========================================================================== #
# This section defines the primary function to create multiple MASV portals.
# ========================================================================== #

def create_masv_portal(portal_name, upload_path):
    """
    Creates a MASV portal for uploading to a specific path with restricted permissions.

    Parameters:
    - portal_name: str : The name of the portal.
    - upload_path: str : The path associated with the portal.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "name": portal_name,
        "description": f"Portal for uploading files to {upload_path}",
        "allowDownload": False,
        "requirePassword": False
    }

    response = requests.post(BASE_URL, headers=headers, json=payload)

    if response.status_code == 201:
        print(f"Portal '{portal_name}' created successfully!")
        print("Portal details:", response.json())
    else:
        print(f"Failed to create portal '{portal_name}'")
        print("Status Code:", response.status_code)
        print("Response:", response.json())

# Create portals for each specified path
for name, path in portal_paths.items():
    create_masv_portal(name, path)
