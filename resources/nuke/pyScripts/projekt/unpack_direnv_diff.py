
# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 Silo 84
               
#                   LOGIK-PROJEKT creates directories, files, scripts & tools
#                   for use with Autodesk Flame and other software.

#                   LOGIK-PROJEKT is free software.

#                   You can redistribute it and/or modify it under the terms
#                   of the GNU General Public License as published by the
#                   Free Software Foundation, either version 3 of the License,
#                   or any later version.

#                   This program is distributed in the hope that it will be
#                   useful, but WITHOUT ANY WARRANTY; without even the
#                   implied warranty of MERCHANTABILITY or FITNESS FOR A
#                   PARTICULAR PURPOSE.

#                   See the GNU General Public License for more details.

#                   You should have received a copy of the GNU General
#                   Public License along with this program.

#                   If not, see <https://www.gnu.org/licenses/>.
               
#                   Contact: brian@silo84.com

# -------------------------------------------------------------------------- #

# File Name:        unpack_direnv_diff.py
# Version:          0.0.1
# Created:          2024-11-08
# Modified:         

# -------------------------------------------------------------------------- #


import os
import base64
import zlib
import json

def decompress_diff(string):
    """
    Decompresses a base64-encoded, zlib-compressed JSON string and extracts the value associated with the key 'n'.

    Args:
        string (str): The base64-encoded, zlib-compressed JSON string.

    Returns:
        The value associated with the key 'n' in the decompressed JSON object.
    """
    decode = base64.urlsafe_b64decode(string)
    decompress = zlib.decompress(decode)
    x = json.loads(decompress)['n']
    return x

def strip_direnv_from_dictionary(dic,strip):
    def strip_direnv_from_dictionary(dic, strip):
        """
        Removes entries from a dictionary where the keys start with a specified prefix.

        Args:
            dic (dict): The dictionary from which to remove entries.
            strip (str): The prefix to check for in the dictionary keys.

        Returns:
            dict: A new dictionary with the entries removed where the keys start with the specified prefix.
        """
    dic = {k: v for k, v in dic.items() if not k.startswith(strip)}
    return dic

def main():
    """
    Main function to unpack and print environment variables from the DIRENV_DIFF environment variable.

    This function retrieves the 'DIRENV_DIFF' environment variable, decompresses it using the 
    decompress_diff function, and then prints each key-value pair in the resulting dictionary.

    Raises:
        KeyError: If the 'DIRENV_DIFF' environment variable is not set.
    """
    string = os.environ['DIRENV_DIFF']


    partytime_env = decompress_diff(string)

    for k,v in partytime_env.items():
        print(f"{k}: {v}")

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 32 30 32 34 20 7C 20 62 72 69 61 6E 40 73 69 6C 6F 38 34 2E 63 6F 6D #
# ========================================================================== #
