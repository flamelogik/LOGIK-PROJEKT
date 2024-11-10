# File Name:        env_loader_example.py
# Version:          1.0.0
# Created:          2024-11-01
# Modified:         2024-11-01

# ========================================================================== #
# This section defines the import statements and environment loader setup.
# ========================================================================== #

from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

API_KEY = os.getenv("MASV_API_KEY")

if not API_KEY:
    raise ValueError("MASV_API_KEY environment variable not set")

# ========================================================================== #
# This section defines a placeholder function to demonstrate API key usage.
# ========================================================================== #

def demo_api_usage():
    """
    Placeholder function demonstrating secure API key usage.
    """
    print("API key loaded securely for use in the script.")
