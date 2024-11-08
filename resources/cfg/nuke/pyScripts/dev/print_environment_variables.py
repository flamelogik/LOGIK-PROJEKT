__author__ = "Brian Willard"
__copyright__ = "Copyright 2023 Brian Willard"
__license__ = "Apache-2.0 - https://opensource.org/licenses/apache-2-0"
__version__ = "1.0.0"
__email__ = "brian@silo84.com"
__website__ = "www.silo84.com"
__status__ = "Production"

# prints all environment variables to the script editor window. 

import os
import sys
import os

def print_environment_variables():
    # Get all keys (environment variable names) in os.environ
    env_keys = os.environ.keys()

    # Print key-value pairs
    for key in env_keys:
        value = os.environ[key]
        print(f"{key}: {value}")


def main():
    print_environment_variables()
