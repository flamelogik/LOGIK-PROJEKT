# File Name:        create_masv_portal.py
# Version:          1.0.0
# Created:          2024-11-01
# Modified:         2024-11-01

# ========================================================================== #
# This section defines the import statements and environment setup.
# ========================================================================== #

import requests
import os

# Load MASV API key from environment variable
API_KEY = os.getenv("MASV_API_KEY")

if not API_KEY:
    raise ValueError("MASV_API_KEY environment variable not set")

BASE_URL = "https://api.massive.io/v1/portals"

# ========================================================================== #
# This section defines the primary function to create a MASV portal.
# ========================================================================== #

def create_masv_portal(portal_name, description, allow_download=True, require_password=False):
    """
    Creates a MASV portal with specified configurations.
    
    Parameters:
    - portal_name: str : Name of the portal.
    - description: str : Description of the portal.
    - allow_download: bool : Set to False to restrict download access.
    - require_password: bool : Set to True if a password is required for access.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "name": portal_name,
        "description": description,
        "allowDownload": allow_download,
        "requirePassword": require_password
    }

    response = requests.post(BASE_URL, headers=headers, json=payload)

    if response.status_code == 201:
        print("Portal created successfully!")
        print("Portal details:", response.json())
    else:
        print("Failed to create portal")
        print("Status Code:", response.status_code)
        print("Response:", response.json())
