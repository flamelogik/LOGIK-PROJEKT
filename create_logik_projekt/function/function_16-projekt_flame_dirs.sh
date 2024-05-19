#!/bin/bash

# -------------------------------------------------------------------------- #

# File Name:        function_16-projekt_flame_dirs.sh
# Version:          2.1.4
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Modified:         2024-05-18
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program contains function(s) that are used to
#                   create new logik projekts.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines global variables.
# ========================================================================== #

# Declare global variables
# declare -g flame_proj_dir=""
flame_proj_dir=""

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to create the flame projekt directory.
create_projekt_directory() {

    # Set the umask to 0
    umask 0

    # ---------------------------------------------------------------------- #

    # Create the flame projekt directory
    flame_proj_dir="/opt/Autodesk/project/$name"

    echo -e "  creating flame projekt directory:"
    echo -e "\n$separator\n"

    if [ ! -d "$flame_proj_dir" ]; then
        mkdir -p -m 2777 "$flame_proj_dir" \
        | sed 's/^ *mkdir: created directory //' \
        | sed 's/^/  /'
    fi

    echo -e "  $flame_proj_dir"
    echo -e "\n$separator\n"

    echo -e "  flame projekt directory created."
    echo -e "\n$separator\n"

    echo -e "  creating flame projekt setup directories:"
    echo -e "\n$separator\n"
}

# -------------------------------------------------------------------------- #

# Function to create the flame projekt setup directories.
create_projekt_setup_directories() {
    # Create the directories
    for flame_proj_setup_dir in "${flame_proj_setup_dirs[@]}"; do
        mkdir -p -v -m 2777 "$flame_proj_dir/$flame_proj_setup_dir" \
        | sed 's/^ *mkdir: created directory //' \
        | sed 's/^/  /'
    done

    echo -e "\n$separator\n"

    echo -e "  flame projekt setup directories created."
    echo -e "\n$separator\n"
}

# -------------------------------------------------------------------------- #

# Define the default flame projekt subdirectories
flame_proj_setup_dirs=(
    "2dtransform"
    "2dtransform/flame"
    "2dtransform/pref"
    "2dtransform/presets"
    "3dblur"
    "3dblur/flame"
    "3dblur/pref"
    "3dblur/presets"
    "aaf"
    "action"
    "action/contextmenu"
    "action/flame"
    "action/ibl"
    "action/presets"
    "action/transitions"
    "audio"
    "audio/pref"
    "audio/pref/ALSA"
    "automatte"
    "automatte/flame"
    "automatte/pref"
    "automatte/presets"
    "autostabilize"
    "autostabilize/flame"
    "autostabilize/pref"
    "autostabilize/presets"
    "average"
    "average/flame"
    "average/pref"
    "average/presets"
    "axis"
    "batch"
    "batch/flame"
    "batch/log"
    "batch/pref"
    "batchclip"
    "batchclip/flame"
    "batchclip/pref"
    "batchclip/presets"
    "blendComp"
    "blendComp/flame"
    "blendComp/pref"
    "blendComp/presets"
    "blur"
    "blur/flame"
    "blur/pref"
    "blur/presets"
    "blur/presets/DEFOCUS"
    "bumpDisplace"
    "bumpDisplace/flame"
    "bumpDisplace/pref"
    "bumpDisplace/presets"
    "burn_letterbox"
    "burn_letterbox/flame"
    "burn_letterbox/pref"
    "burn_letterbox/presets"
    "burn_metadata"
    "burn_metadata/flame"
    "burn_metadata/overlay"
    "burn_metadata/overlay/presets"
    "burn_metadata/pref"
    "burn_metadata/presets"
    "ccurves"
    "ccurves/flame"
    "ccurves/pref"
    "ccurves/presets"
    "cfg"
    "cfg/linux"
    "cfg/linux/template"
    "check"
    "check/flame"
    "check/pref"
    "check/presets"
    "clamp"
    "clamp/flame"
    "clamp/pref"
    "clamp/presets"
    "colour_correct"
    "colour_correct/flame"
    "colour_correct/pref"
    "colour_correct/presets"
    "colourwarper"
    "colourwarper/flame"
    "colourwarper/pref"
    "colourwarper/presets"
    "combine"
    "combine/flame"
    "combine/pref"
    "combine/presets"
    "comp"
    "comp/flame"
    "compound"
    "compound/flame"
    "compound/pref"
    "compound/presets"
    "comp/pref"
    "comp/presets"
    "cryptoMatte"
    "cryptoMatte/flame"
    "cryptoMatte/pref"
    "cryptoMatte/presets"
    "damage"
    "damage/flame"
    "damage/pref"
    "damage/presets"
    "damage/presets/ANALOG"
    "damage/presets/DIGITAL"
    "damage/presets/FILM"
    "deal"
    "deal/flame"
    "deal/pref"
    "deal/presets"
    "deform"
    "deform/flame"
    "deform/pref"
    "deform/presets"
    "degrain"
    "degrain/flame"
    "degrain/pref"
    "degrain/presets"
    "deinterlace"
    "deinterlace/flame"
    "deinterlace/pref"
    "deinterlace/presets"
    "denoise"
    "denoise/flame"
    "denoise/pref"
    "denoise/presets"
    "depthOfField"
    "depthOfField/flame"
    "depthOfField/pref"
    "depthOfField/presets"
    "difference"
    "difference/flame"
    "difference/pref"
    "difference/presets"
    "dissolve"
    "dissolve/flame"
    "dissolve/pref"
    "dissolve/presets"
    "distort"
    "distort/flame"
    "distort/pref"
    "distort/presets"
    "edge"
    "edgeDetect"
    "edgeDetect/flame"
    "edgeDetect/pref"
    "edgeDetect/presets"
    "edge/flame"
    "edge/pref"
    "edge/presets"
    "edl"
    "export"
    "export/flame"
    "export/pref"
    "export/presets"
    "export/presets/flame"
    "export/presets/flame/audio_file"
    "export/presets/flame/audio_file/AIFF"
    "export/presets/flame/audio_file/AIFF-C"
    "export/presets/flame/audio_file/AVR"
    "export/presets/flame/audio_file/BICSF"
    "export/presets/flame/audio_file/MP3"
    "export/presets/flame/audio_file/NEXTSND"
    "export/presets/flame/audio_file/WAVE"
    "export/presets/flame/distribution_package"
    "export/presets/flame/distribution_package/Dolby Vision"
    "export/presets/flame/file_sequence"
    "export/presets/flame/file_sequence/Alias"
    "export/presets/flame/file_sequence/Cineon"
    "export/presets/flame/file_sequence/DPX"
    "export/presets/flame/file_sequence/Jpeg"
    "export/presets/flame/file_sequence/Maya"
    "export/presets/flame/file_sequence/OpenEXR"
    "export/presets/flame/file_sequence/Pict"
    "export/presets/flame/file_sequence/Pixar"
    "export/presets/flame/file_sequence/Png"
    "export/presets/flame/file_sequence/SGI"
    "export/presets/flame/file_sequence/Softimage"
    "export/presets/flame/file_sequence/Targa"
    "export/presets/flame/file_sequence/Tiff"
    "export/presets/flame/file_sequence/Wavefront"
    "export/presets/flame/movie_file"
    "export/presets/flame/movie_file/Apple Final Cut Pro"
    "export/presets/flame/movie_file/AVC-Intra"
    "export/presets/flame/movie_file/Avid Media Composer"
    "export/presets/flame/movie_file/Cinedeck"
    "export/presets/flame/movie_file/DVCPro HD"
    "export/presets/flame/movie_file/H.264"
    "export/presets/flame/movie_file/MP4"
    "export/presets/flame/movie_file/Panasonic"
    "export/presets/flame/movie_file/QuickTime"
    "export/presets/flame/movie_file/Sony XAVC"
    "export/presets/flame/movie_file/Sony XDCAM"
    "export/presets/flame/sequence_publish"
    "export/presets/flame/sequence_publish/Apple Final Cut Pro"
    "export/presets/flame/sequence_publish/Avid Media Composer"
    "export/presets/flame/sequence_publish/Avid Pro Tools"
    "export/presets/flame/sequence_publish/DaVinci Resolve"
    "export/presets/flame/sequence_publish/EDL Publish"
    "export/presets/flame/sequence_publish/Filmlight Baselight"
    "export/presets/flame/sequence_publish/Shot Publish"
    "export/presets/flame/sequence_publish/Simple Publish"
    "export/presets/flame/sequence_publish/Source Media Export"
    "export/presets/flame/sequence_publish/Source Media Publish"
    "export/presets/shotgun"
    "export/presets/shotgun/audio_file"
    "export/presets/shotgun/distribution_package"
    "export/presets/shotgun/file_sequence"
    "export/presets/shotgun/movie_file"
    "export/presets/shotgun/sequence_publish"
    "exposure"
    "exposure/flame"
    "exposure/pref"
    "exposure/presets"
    "expressions"
    "fieldmerge"
    "fieldmerge/flame"
    "fieldmerge/pref"
    "fieldmerge/presets"
    "filmrestore"
    "filmrestore/pref"
    "filmrestore/presets"
    "filter"
    "filter/flame"
    "filter/pref"
    "filter/presets"
    "flip"
    "flip/flame"
    "flip/pref"
    "flip/presets"
    "gateway_import"
    "gateway_import/flame"
    "gateway_import/pref"
    "gateway_import/presets"
    "glow"
    "glow/flame"
    "glow/pref"
    "glow/presets"
    "gmask"
    "gmask/default"
    "gmask/flame"
    "gmask/pref"
    "gmask/presets"
    "gmask/transitions"
    "gmask/transitions/SMPTE"
    "gradient"
    "gradient/flame"
    "gradient/pref"
    "gradient/presets"
    "hdr"
    "hdr/flame"
    "hdr/pref"
    "hdr/presets"
    "histo2d"
    "histo2d/flame"
    "histo2d/pref"
    "histo2d/presets"
    "hub"
    "hub/flame"
    "hub/pref"
    "hub/presets"
    "image"
    "image/flame"
    "image/presets"
    "images"
    "import"
    "import/flame"
    "import/pref"
    "import/presets"
    "interlace"
    "interlace/flame"
    "interlace/pref"
    "interlace/presets"
    "key"
    "keyer3d"
    "keyer3d/flame"
    "keyer3d/pref"
    "keyer3d/presets"
    "keyerChannel"
    "keyerChannel/flame"
    "keyerChannel/pref"
    "keyerChannel/presets"
    "keyerHLS"
    "keyerHLS/flame"
    "keyerHLS/pref"
    "keyerHLS/presets"
    "keyerRGB"
    "keyerRGBCMYL"
    "keyerRGBCMYL/flame"
    "keyerRGBCMYL/pref"
    "keyerRGBCMYL/presets"
    "keyerRGB/flame"
    "keyerRGB/pref"
    "keyerRGB/presets"
    "keyerYUV"
    "keyerYUV/flame"
    "keyerYUV/pref"
    "keyerYUV/presets"
    "key/flame"
    "key/pref"
    "key/presets"
    "lensDistort"
    "lensDistort/flame"
    "lens_distortion"
    "lens_distortion/flame"
    "lens_distortion/pref"
    "lens_distortion/presets"
    "lensDistort/pref"
    "lensDistort/presets"
    "look"
    "look/flame"
    "look/pref"
    "look/presets"
    "lut"
    "lutfloat"
    "lut/pref"
    "lut/presets"
    "mapConvert"
    "mapConvert/flame"
    "mapConvert/pref"
    "mapConvert/presets"
    "mask"
    "mask/flame"
    "mask/pref"
    "mask/presets"
    "masterkey"
    "masterkey/flame"
    "masterkey/pref"
    "masterkey/presets"
    "matchbox"
    "matchbox/flame"
    "matchbox/pref"
    "matchGrain"
    "matchGrain/flame"
    "matchGrain/pref"
    "matchGrain/presets"
    "mattecurves"
    "mattecurves/flame"
    "mattecurves/pref"
    "mattecurves/presets"
    "mediaImport"
    "mediaImport/pref"
    "mediaImport/presets"
    "mix"
    "mix/flame"
    "mix/pref"
    "mix/presets"
    "modularKeyer"
    "modularKeyer/flame"
    "modularKeyer/pref"
    "modularKeyer/presets"
    "mono"
    "mono/flame"
    "mono/pref"
    "mono/presets"
    "motif"
    "motif/flame"
    "motif/pref"
    "motif/presets"
    "motion_analysis"
    "motion_analysis/flame"
    "motion_analysis/pref"
    "motion_analysis/presets"
    "motionBlur"
    "motionBlur/flame"
    "motionBlur/pref"
    "motionBlur/presets"
    "motion_convert"
    "motion_convert/flame"
    "motion_convert/pref"
    "motion_convert/presets"
    "note"
    "note/flame"
    "note/pref"
    "note/presets"
    "openfx"
    "openfx/flame"
    "openfx/pref"
    "openfx/presets"
    "optics"
    "optics/flame"
    "optics/pref"
    "optics/presets"
    "output"
    "output/flame"
    "output/pref"
    "output/presets"
    "overlays"
    "overlays/presets"
    "paint"
    "paint/autopaint"
    "paint/brush"
    "paint/cutout"
    "paint/flame"
    "paint/geometry"
    "paint/mask"
    "paint/palette"
    "paint/picture"
    "paint/pref"
    "paint/presets"
    "paint/set"
    "particules"
    "path"
    "pixelspread"
    "pixelspread/flame"
    "pixelspread/pref"
    "pixelspread/presets"
    "posterize"
    "posterize/flame"
    "posterize/pref"
    "posterize/presets"
    "pulldown"
    "pulldown/flame"
    "pulldown/pref"
    "pulldown/presets"
    "pybox"
    "pybox/flame"
    "pybox/pref"
    "pybox/presets"
    "python"
    "quickcomp"
    "quickcomp/flame"
    "quickcomp/pref"
    "quickcomp/presets"
    "recursiveOps"
    "recursiveOps/flame"
    "recursiveOps/pref"
    "recursiveOps/presets"
    "regrain"
    "regrain/flame"
    "regrain/pref"
    "regrain/presets"
    "repeat"
    "repeat/flame"
    "repeat/pref"
    "repeat/presets"
    "resize"
    "resize/flame"
    "resize/pref"
    "resize/presets"
    "separate"
    "separate/flame"
    "separate/pref"
    "separate/presets"
    "sparks"
    "sparks/flame"
    "stabilizer"
    "stabilizer/pref"
    "stabilizer/presets"
    "status"
    "stereo"
    "stereoAnaglyph"
    "stereoAnaglyph/flame"
    "stereoAnaglyph/pref"
    "stereoAnaglyph/presets"
    "stereo/flame"
    "stereoInterlace"
    "stereoInterlace/flame"
    "stereoInterlace/pref"
    "stereoInterlace/presets"
    "stereo/pref"
    "stereo/presets"
    "stereoToolbox"
    "stereoToolbox/flame"
    "stereoToolbox/pref"
    "stereoToolbox/presets"
    "stmap"
    "stmap/flame"
    "stmap/pref"
    "stmap/presets"
    "stylize"
    "stylize/flame"
    "stylize/pref"
    "stylize/presets"
    "substance"
    "substance/flame"
    "substance/pref"
    "substance/presets"
    "subtitle"
    "subtitle/flame"
    "subtitle/pref"
    "subtitle/presets"
    "synColor"
    "synColor/policy"
    "synColor/policy/user_color_spaces"
    "synColor/transforms"
    "text"
    "text/flame"
    "text/pref"
    "text/presets"
    "timewarp"
    "timewarp/flame"
    "timewarp/pref"
    "timewarp/presets"
    "tmp"
    "viewing"
    "viewing/flame"
    "viewing/pref"
    "viewing/presets"
    "warper"
    "warper/magnet"
    "warper/pref"
    "warper/presets"
    "wipe"
    "xml"
)

# -------------------------------------------------------------------------- #

create_flame_projekt_directories() {
    create_projekt_directory
    create_projekt_setup_directories
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# # Call the function to create the flame projekt directories
# create_flame_projekt_directories

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    create_flame_projekt_directories
fi

# -------------------------------------------------------------------------- #

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
# version:               1.0.0
# modified:              2024-04-20 - 16:20:00
# comments:              refactored monolithic program into separate functions
# -------------------------------------------------------------------------- #
# version:               2.0.0
# modified:              2024-04-29 - 11:29:27
# comments:              testing production readiness
# -------------------------------------------------------------------------- #
# version:               2.0.1
# modified:              2024-04-30 - 07:06:00
# comments:              Removed 'declare -g' statements for macOS compatibility
# -------------------------------------------------------------------------- #
# version:               2.0.2
# modified:              2024-04-30 - 12:29:07
# comments:              added 'umask 0' statements for rsync commands
# -------------------------------------------------------------------------- #
# version:               2.0.3
# modified:              2024-05-03 - 10:16:09
# comments:              Restored CamelCase keys for projekt_metadata_xml_file
# -------------------------------------------------------------------------- #
# version:               2.0.4
# modified:              2024-05-03 - 10:56:34
# comments:              Restore 'jobs_dir' to /JOBS
# -------------------------------------------------------------------------- #
# version:               2.1.4
# modified:              2024-05-18 - 18:00:11
# comments:              Added GNU GPLv3 Disclaimer.
