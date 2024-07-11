# File Name:        separators.py

'''
# -------------------------------------------------------------------------- #

# File Name:        separators.py
# Version:          0.4.4
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-06-12
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program contains function(s) that are used to
#                   create new logik projekts.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #
'''

# ========================================================================== #
# This section creates decorative separators for titles and banners.
# ========================================================================== #

# Function to repeat a character n times
def repeat_char(char, count):
    return char * count

# Function to ensure a line is exactly 79 characters
def make_line_79_chars(line):
    current_length = len(line)
    pad = 79 - current_length
    line = f"{line[:-2]}{repeat_char('=', pad)} #"
    return line

# Function to generate title line
def generate_title_line(title):
    title_pad_length = (79 - len(title) - 8) // 2
    title_line = (
        f"# {repeat_char('=', title_pad_length)} "
        f"{title} "
        f"{repeat_char('=', title_pad_length)} #\n"
    )
    title_line = make_line_79_chars(title_line)
    return title_line

# Function to generate end of title line
def generate_end_title_line(end_title):
    end_title_pad_length = (79 - len(end_title) - 8) // 2
    end_title_line = (
        f"# {repeat_char('=', end_title_pad_length)} "
        f"{end_title} "
        f"{repeat_char('=', end_title_pad_length)} #\n"
    )
    end_title_line = make_line_79_chars(end_title_line)
    return end_title_line

# Main function
def main():

    title = "My Title"
    end_title = "End Title"

    print(separator)
    print(separator_hash)

    print(generate_title_line(title))
    print(generate_end_title_line(end_title))

if __name__ == "__main__":
    main()

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 2D 4D 45 4B 41 4E 49 53 4D 5A #
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Disclaimer:       This program is part of LOGIK-PROJEKT.
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

# -------------------------------------------------------------------------- #
# Changelist:
# -------------------------------------------------------------------------- #
# version:               0.0.1
# modified:              2024-05-03 - 01:53:36
# comments:              Basic functionality defined and tested
# -------------------------------------------------------------------------- #
# version:               0.0.2
# modified:              2024-05-03 - 02:13:01
# comments:              Fixed some formatting and flame menus
# -------------------------------------------------------------------------- #
# version:               0.0.3
# modified:              2024-05-03 - 11:26:02
# comments:              Changed 'the_current_project' to 'the_current_projekt'
# -------------------------------------------------------------------------- #
# version:               0.0.4
# modified:              2024-05-03 - 11:38:53
# comments:              Standardized 'logik-projekt' menu entries
# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-12 - 15:37:50
# comments:              Added function to read directories from JSON files.
# -------------------------------------------------------------------------- #
# version:               0.0.6
# modified:              2024-05-12 - 18:16:05
# comments:              Added a 'separators' function and tested in flame 2025.
# -------------------------------------------------------------------------- #
# version:               0.0.7
# modified:              2024-05-14 - 16:30:58
# comments:              Minor reformatting.
# -------------------------------------------------------------------------- #
# version:               0.0.8
# modified:              2024-05-14 - 16:31:23
# comments:              Changed object_colors from python to JSON.
# -------------------------------------------------------------------------- #
# version:               0.0.9
# modified:              2024-05-14 - 16:31:47
# comments:              Tested in flame 2025.
# -------------------------------------------------------------------------- #
# version:               0.1.0
# modified:              2024-05-14 - 16:46:55
# comments:              Production tested in flame 2025.
# -------------------------------------------------------------------------- #
# version:               0.2.0
# modified:              2024-05-14 - 18:05:26
# comments:              Prepped for obsolete code removal. Tested in flame 2025
# -------------------------------------------------------------------------- #
# version:               0.3.0
# modified:              2024-05-14 - 19:27:33
# comments:              Restored 'object_colors' from python function.
# -------------------------------------------------------------------------- #
# version:               0.3.1
# modified:              2024-05-15 - 07:55:47
# comments:              Renamed 'classes_and_functions' dir to 'modules'.
# -------------------------------------------------------------------------- #
# version:               0.4.1
# modified:              2024-05-18 - 18:01:29
# comments:              Added GNU GPLv3 Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.2
# modified:              2024-05-18 - 18:46:51
# comments:              Minor modification to Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.3
# modified:              2024-06-03 - 10:32:22
# comments:              Moved import flame statement to each function
# -------------------------------------------------------------------------- #
# version:               0.4.4
# modified:              2024-06-12 - 12:21:22
# comments:              Restored import flame statement to top of script.
