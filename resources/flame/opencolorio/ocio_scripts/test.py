#

# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 man-made-mekanyzms
                
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
                
#                   Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #

# File Name:        test.py
# Version:          0.0.1
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section defines the import statements and directory paths.
# ========================================================================== #

import os
import PyOpenColorIO as ocio

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create a new folder
new_folder = os.path.join(script_dir, 'flame_colortoolkit_ocio', 'transforms')
os.makedirs(new_folder, exist_ok=True)
print(f"Creating folder: {new_folder}\n")
    
# Define config
config = ocio.Config.CreateFromFile("ocio://studio-config-latest")

# Define path to the Syncolor transforms
transforms_dir = "/opt/Autodesk/Synergy/SynColor/2019.1/transforms"
print(f"Transforms directory: {transforms_dir}")  # Debugging

# Create FileTransform objects for each CTF file
ft1_path = "/opt/Autodesk/Synergy/SynColor/2019.1/transforms/primaries/ACEScg_to_ACES.ctf"
ft2_path = "/opt/Autodesk/Synergy/SynColor/2019.1/transforms/camera/Arri/ACES_to_Alexa-v3-LogC-EI800_no-cam-black.ctf"
ft3_path = "/opt/Autodesk/Synergy/SynColor/2019.1/transforms/camera/Arri/LogC_to_HD-video.ctf"

print(f"Creating FileTransform for: {ft1_path}")  # Debugging
ft1 = ocio.FileTransform(ft1_path)

print(f"Creating FileTransform for: {ft2_path}")  # Debugging
ft2 = ocio.FileTransform(ft2_path)

print(f"Creating FileTransform for: {ft3_path}")  # Debugging
ft3 = ocio.FileTransform(ft3_path)

# Invert the second FileTransform
print(f"Inverting FileTransform: {ft2_path}")  # Debugging
ft2.setDirection(ocio.TRANSFORM_DIR_INVERSE)

# Create a GroupTransform object with all three FileTransforms
print("Creating GroupTransform with all FileTransforms")  # Debugging
gt = ocio.GroupTransform([ft1, ft2, ft3])

# Write the GroupTransform to a new CTF file
output_file = "test_2.ctf"
print(f"Writing GroupTransform to: {output_file}")  # Debugging
gt.write("Color Transform Format", output_file, config)
print("Finished writing GroupTransform")

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:       

# -------------------------------------------------------------------------- #
# version:          0.0.1
# modified:         2024-08-31 - 16:51:09
# comments:         prep for release - code appears to be functional
# -------------------------------------------------------------------------- #
