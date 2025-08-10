
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

# File Name:        disableGPUAcceleration.py
# Version:          0.0.1
# Created:          2024-11-08
# Modified:

# -------------------------------------------------------------------------- #

import nuke

def disableGPUAcceleration():
    """
    Disables GPU acceleration for all nodes in the current Nuke script.

    This function iterates through all nodes in the Nuke script and sets the
    GPU-related knobs to 0 (disabled) if they exist. Specifically, it targets
    the following knobs:
    - 'useGPUIfAvailable'
    - 'r3dUseCUDA'
    - 'arriUseCUDA'
    - 'Use GPU if Available'

    Note:
    - This function requires the Nuke environment to be properly set up and
      accessible.
    - The function does not return any value.
    """
    for i in nuke.allNodes():
        if i.knob('useGPUIfAvailable'):
            i.knob('useGPUIfAvailable').setValue(0)
        if i.knob('r3dUseCUDA'):
            i.knob('r3dUseCUDA').setValue(0)
        if i.knob('arriUseCUDA'):
            i.knob('r3dUseCUDA').setValue(0)
        # Use GPU if Available' knobs...
        if i.knob('Use GPU if Available'):
            i.knob('Use GPU if Available').setValue(0)


def main():
    print('disabling GPU acceleration knobs...')
    disableGPUAcceleration()

# -------------------------------------------------------------------------- #

# ========================================================================== #
# 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 C2 A9 32 30 32 35 #
# ========================================================================== #
