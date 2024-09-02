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

# File Name:        copyright_example.py
# Version:          0.0.1
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section defines the import statements and directory paths.
# ========================================================================== #

import PyOpenColorIO as ocio

# Create FileTransform objects for each CTF file
ft1 = ocio.FileTransform("<Path to first CTF file>")
ft2 = ocio.FileTransform("<Path to second CTF file>")
ft3 = ocio.FileTransform("<Path to third CTF file>")

# Invert the second FileTransform if necessary
ft2.setDirection(ocio.TRANSFORM_DIR_INVERSE)

# Create a GroupTransform object with all three FileTransforms
gt = ocio.GroupTransform([ft1, ft2, ft3])

# Set the metadata with a copyright token
metadata = ocio.InfoMetadata()
metadata.setAttribute("Copyright", "© 2024 Your Name or Company. All rights reserved.")
gt.setMetadata(metadata)

# Write the GroupTransform to a new CTF file
gt.write("Color Transform Format", "test.ctf", config)

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:       

# -------------------------------------------------------------------------- #
# version:          0.0.1
# modified:         2024-08-31 - 16:51:09
# comments:         prep for release - code appears to be functional
# -------------------------------------------------------------------------- #
