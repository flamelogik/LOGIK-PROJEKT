__author__ = "Brian Willard"
__copyright__ = "Copyright 2023 Brian Willard"
__license__ = "Apache-2.0 - https://opensource.org/licenses/apache-2-0"
__version__ = "1.0.0"
__email__ = "brian@silo84.com"
__website__ = "www.silo84.com"
__status__ = "Production"

# prints the nuke.env to the script editor window

import nuke

def main():
    # Get all keys in nuke.env
    env_keys = nuke.env.keys()

    # Print key-value pairs
    for key in env_keys:
        value = nuke.env[key]
        print(f"{key}: {value}")
