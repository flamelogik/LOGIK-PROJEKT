import re

def parse_resolution_string(resolution_string: str) -> tuple[int, int, float]:
    print(f"parse_resolution_string: Input = {resolution_string}")
    if not resolution_string:
        print("parse_resolution_string: Input is empty.")
        return None, None, None

    try:
        resolution_part = resolution_string.split('|')[0].strip()
        print(f"parse_resolution_string: Resolution part = {resolution_part}")
        numbers = re.findall(r'\d+', resolution_part)
        print(f"parse_resolution_string: Found numbers = {numbers}")

        if len(numbers) >= 2:
            width = int(numbers[0])
            height = int(numbers[1])
            pixel_aspect_ratio = 1.0
            if len(numbers) >= 3:
                pixel_aspect_ratio = float(numbers[2])
            print(f"parse_resolution_string: Parsed width={width}, height={height}, pixel_aspect_ratio={pixel_aspect_ratio}")
            return width, height, pixel_aspect_ratio

    except (ValueError, IndexError) as e:
        print(f"parse_resolution_string: Error during parsing - {e}")
        pass

    print("parse_resolution_string: Could not parse resolution string.")
    return None, None, None

def replace_placeholders(path_string: str, placeholder_values: dict) -> str:
    """
    Replaces placeholders in a path string with their corresponding values.
    Handles nested placeholders by iterating until no more known placeholders are found.
    """
    resolved_path = path_string
    max_iterations = 10  # Prevent infinite loops for circular references

    for _ in range(max_iterations):
        found_placeholder = False
        for placeholder, value in placeholder_values.items():
            # Use re.escape to handle special characters in placeholder keys if they are regex patterns
            pattern = re.escape(placeholder)
            if re.search(pattern, resolved_path):
                resolved_path = resolved_path.replace(placeholder, value)
                found_placeholder = True
        if not found_placeholder:
            break  # No more placeholders found, exit loop

    return resolved_path


# -------------------------------------------------------------------------- #

# DISCLAIMER:   This file is part of LOGIK-PROJEKT.

#               Copyright © 2025 STRENGTH IN NUMBERS

#               LOGIK-PROJEKT creates directories, files, scripts & tools
#               for use with Autodesk Flame and other software.

#               LOGIK-PROJEKT is free software.

#               You can redistribute it and/or modify it under the terms
#               of the GNU General Public License as published by the
#               Free Software Foundation, either version 3 of the License,
#               or any later version.

#               This program is distributed in the hope that it will be
#               useful, but WITHOUT ANY WARRANTY; without even the
#               implied warranty of MERCHANTABILITY or
#               FITNESS FOR A PARTICULAR PURPOSE.

#               See the GNU General Public License for more details.
#               You should have received a copy of the GNU General
#               Public License along with this program.

#               If not, see <https://www.gnu.org/licenses/gpl-3.0.en.html>.

#               Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #
# C2 A9 32 30 32 35 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 #
# -------------------------------------------------------------------------- #
# Changelog:
# -------------------------------------------------------------------------- #
