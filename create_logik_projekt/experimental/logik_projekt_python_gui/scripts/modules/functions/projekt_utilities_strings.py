'''
File Name:        projekt_utilities_strings.py
Version:          1.0.0
Language:         python script
Author:           Phil MAN - phil_man@mac.com
Created:          2024-05-23
Modified:         2024-06-02

Description:      This program modifies and sanitizes strings
'''

# ========================================================================== #
# This function sanitizes strings according to the documented parameters
# ========================================================================== #

def string_clean(string):

    '''
    Clean string: allow only lower case letters, numbers, and underscores.

        * Convert to lowercase

        * Keep only lowercase letters, numbers, underscores, and replace
          other characters with underscores

        * Replace whitespace characters with underscores

        * Replace consecutive underscores with single underscore

        * Remove leading and trailing underscores

    '''

    string = string.lower()

    string = ''.join(character if character.islower() or character.isdigit() or character == '_' or character.isspace() else '_' for character in string)

    string = string.replace(' ', '_')

    string = '_'.join(filter(None, string.split('_')))

    string = string.strip('_')

    return string

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

'''
Disclaimer:       This program is part of LOGIK-PROJEKT.
                  LOGIK-PROJEKT is free software.

                  You can redistribute it and/or modify it under the terms
                  of the GNU General Public License as published by the
                  Free Software Foundation, either version 3 of the License,
                  or any later version.

                  This program is distributed in the hope that it will be
                  useful, but WITHOUT ANY WARRANTY; without even the
                  implied warranty of MERCHANTABILITY or FITNESS FOR A
                  PARTICULAR PURPOSE.

                  See the GNU General Public License for more details.

                  You should have received a copy of the GNU General
                  Public License along with this program.

                  If not, see <https://www.gnu.org/licenses/>.
'''

# -------------------------------------------------------------------------- #
# Changelist:
# -------------------------------------------------------------------------- #
