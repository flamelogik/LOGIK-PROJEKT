
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

# File Name:        defaults.
# Version:          0.0.1
# Created:          2024-10-31
# Modified:         2021-11-07


'''
This module provides default values for Nuke nodes and settings.
'''


import nuke
import nukescripts
import os



# ========================================================================== #
# This section sets the defualt frame rate
# ========================================================================== #

# Project Settings > Default FPS: 23.976
nuke.knobDefault("Root.fps", "23.976")

# Project Settings > Default FPS: 24
# nuke.knobDefault("Root.fps", "24")

# Project Settings > Default FPS: 29.976
#nuke.knobDefault("Root.fps", "29.976")

#nuke.knobDefault("Root.fps", '25')
#nuke.knobDefault("Viewer.fps", "25")

# ========================================================================== #
# This section sets the default frame range
# ========================================================================== #

# timeline settings settings
nuke.knobDefault("Root.first_frame", "1001")
nuke.knobDefault("Root.last_frame", "1101")
nuke.knobDefault("Root.lock_range", "1")


# ========================================================================== #
# This section sets the default projekt format
# ========================================================================== #

# Project Settings > Default format: 4K_DCP 4096x2160
# nuke.knobDefault("Root.format", "4K_DCP")

# Project Settings > Default format: UHD_4K 3840x2160
nuke.knobDefault("Root.format", "UHD_4K")

# Project Settings > Default format: HD_1080 1920x1080
# nuke.knobDefault("Root.format", "HD_1080")

# ========================================================================== #
# This section sets the render_mode to top-down as the default
# ========================================================================== #

#nuke.knobDefault("Root.render_mode", "classic" )
nuke.knobDefault("Root.render_mode", "top-down" )

# ========================================================================== #
# This section sets color management to OCIO as the default
# ========================================================================== #

#Color Management
nuke.knobDefault('Root.colorManagement', 'OCIO')

# ========================================================================== #
# This section sets the label for the Write node and format settings
# ========================================================================== #

nuke.knobDefault("Write.label", '[if {[value file_type] == "exr"} {return [value compression]\\n[value datatype]} else {return ""}] [if {[value file_type] == "mov"} {return [value mov_prores_codec_profile]} else {return ""}]')

# Write > Default for MOV files: ProRes 4444 XQ with ALPHA
nuke.knobDefault("Write.mov.mov_prores_codec_profile","ProRes 4444 XQ 12-bit")
nuke.knobDefault("Write.mov.channels","rgba")
#nuke.knobDefault("Write.mov.colorspace","sRGB")
#nuke.knobDefault("Write.mov.colorspace","rec709")

# Write > Default for EXR files: 16bit Half, DWAB
nuke.knobDefault("Write.exr.channels","all")
nuke.knobDefault("Write.exr.compression","DWAB")
nuke.knobDefault("Write.exr.create_directories","1")

# Write > Default for JPEG files: quality 1.0, 4:4:4
nuke.knobDefault( "Write.jpeg.channels","rgb")
nuke.knobDefault( 'Write.jpeg._jpeg_quality', '1' )
nuke.knobDefault( 'Write.jpeg._jpeg_sub_sampling', '4:4:4' )

# ========================================================================== #
# This section sets the label for the Read node
# ========================================================================== #

nuke.knobDefault("Read.label",
                 "<font size=\"3\" color =#548DD4><b> Frame range :</b></font> "
                 "<font color = red>[value first] - [value last] </font>")


# ========================================================================== #
# This section adds labels to the following nodes
# ========================================================================== #


nuke.knobDefault('Constant.label', '[value width] x [value height]')

nuke.knobDefault('VectorDistort.label', 'ref frame [value referenceFrame]')
#nuke.knobDefault("VectorDistort.label", "REF: [value reference_frame]")

#nuke.knobDefault('Tracker4.label', '[value transform] <br> ref frame: [value reference_frame]')
nuke.knobDefault('Tracker4.label', 'Motion: [value transform]\nRef Frame: [value reference_frame]')


nuke.knobDefault("AdjBBox.label", "[value numpixels]")

nuke.knobDefault("Blur.label", "[value size] px")
nuke.knobDefault("FilterErode.label", "[value size] px")
nuke.knobDefault("Erode.label", "[value size] px")
nuke.knobDefault("Dilate.label", "[value size] px")
nuke.knobDefault("Soften.label", "[value size] px")
nuke.knobDefault("Sharpen.label", "[value size] px")
nuke.knobDefault("Defocus.label", "[value defocus]")

nuke.knobDefault('OCIOColorSpace.label', '<i>[value in_colorspace]</i> <b>to</b> <i>[value out_colorspace]')
nuke.knobDefault("Colorspace.label", "[value colorspace_in] - [value colorspace_out]")

nuke.knobDefault("Merge2.label", "[if {[value mix]<1} { value mix }]")
nuke.knobDefault('Switch.label', '[value which]')
nuke.knobDefault('Dissolve.label', 'which: [value which] \nmetadata: [value metainput]')

nuke.knobDefault("TimeOffset.label", "[value time_offset]")
nuke.knobDefault("FrameRange.label", "[value knob.first_frame] - [value knob.last_frame]")
nuke.knobDefault('TimeClip.label', '[value first] to [value last]')
nuke.knobDefault("Retime.label", "speed: [value speed]")

nuke.knobDefault("Remove.label", "[value channels]")
nuke.knobDefault("Shuffle.label", "[value in]")

nuke.knobDefault("Saturation.label", "[if {[value saturation]<1} { value saturation }]")
nuke.knobDefault("Saturation.label", "[value saturation]")
nuke.knobDefault("Multiply.label", "[value value]")
nuke.knobDefault("Expression.label", "[knob expr3]")

# Labels for the classic 3D System
nuke.knobDefault("ScanlineRender.label", "[value samples]")
#nuke.knobDefault("Project3D2.label", "project on [value project_on] \n crop: [value crop] \n[value occlusion_mode]")
nuke.knobDefault("Project3D2.label", '[value project_on] \n crop [expr { [value crop] == true ? "on" : "off"}]\n occlusion [value occlusion_mode]')


# ========================================================================== #
# This section sets the default values for the following nodes
# ========================================================================== #

#nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')

nuke.knobDefault("NoOp.hide_input", "1")
nuke.knobDefault("DeepReformat.pbb", "1")
nuke.knobDefault("DeepReformat.resize", "none")
nuke.knobDefault("STMap.channels", "rgba")
nuke.knobDefault("STMap.uv", "rgb")
nuke.knobDefault("AdjBBox.numpixels", "100")
#nuke.knobDefault("Constant.channels", "rgba")
#nuke.knobDefault("Constant.channels", "rgb")


# ========================================================================== #
# This section sets default values for the Dot node
# ========================================================================== #

nuke.knobDefault("Dot.note_font_size", "22")
# nuke.knobDefault("Dot.note_font", "Bitstream Vera Sans Bold")


# ========================================================================== #
# This section sets default values for the StickyNote node
# ========================================================================== #

# nuke.knobDefault("StickyNote.note_font_size", "40")
# nuke.knobDefault("StickyNote.note_font", "Avenir Black")


# ========================================================================== #
# This section sets the default value for the Retime node
# ========================================================================== #

nuke.knobDefault("Retime.before", "continue")
nuke.knobDefault("Retime.after", "continue")
nuke.knobDefault("Retime.filter", "nearest")


# ========================================================================== #
# This section sets the default values for for the following nodes
# ========================================================================== #

# Exposure Tool > Use stops instead of densities
nuke.knobDefault("EXPTool.mode", "0")
nuke.knobDefault("Gamma.channels", "rgba")
nuke.knobDefault('Multiply.channels', 'rgba')
nuke.knobDefault('Invert.channels', 'rgba')


# ========================================================================== #
# This section sets the default values for the Remove node
# ========================================================================== #

nuke.knobDefault("Remove.operation", "keep")
nuke.knobDefault("Remove.channels", "rgba")

# ========================================================================== #
# This section sets the default values to be rgba for the following nodes
# ========================================================================== #


nuke.knobDefault("Dilate.channels", "rgba")
nuke.knobDefault("Soften.channels", "rgba")
nuke.knobDefault("Sharpen.channels", "rgb")
nuke.knobDefault("GodRays.channels", "rgba")
nuke.knobDefault("Defocus.channels", "rgba")
nuke.knobDefault("ZDefocus2.channels", "rgba")
nuke.knobDefault("VectorBlur.channels", "rgba")
nuke.knobDefault("FilterErode.channels","alpha")


# ========================================================================== #
# This section sets the LayerContactSheet node to show layer names by default
# ========================================================================== #

nuke.knobDefault('LayerContactSheet.showLayerNames', '1')


# ========================================================================== #
# This section sets the default values for the ContactSheet node
# ========================================================================== #

# Sets relevant expressions in relevant knobs to automagically figure out the contact sheet's resolution, rows, columns, etc.
nuke.knobDefault("ContactSheet.width", '{"input.width * columns"}')
nuke.knobDefault("ContactSheet.height", '{"input.height * rows"}')
nuke.knobDefault("ContactSheet.roworder", 'TopBottom')
nuke.knobDefault("ContactSheet.colorder", 'LeftRight')
nuke.knobDefault("ContactSheet.rows", '{"ceil(inputs/columns)"}')
nuke.knobDefault("ContactSheet.columns", '{"ceil(sqrt(inputs))"}')


# ========================================================================== #
# This section sets the default values for the Mirror and Mirror2 nodes
# ========================================================================== #

nuke.knobDefault("Mirror.Horizontal", "1")
nuke.knobDefault("Mirror2.flop", "1")
nuke.knobDefault('Mirror2.flop', 'True')

# ========================================================================== #
# This section sets the default values for the Tracker4 node
# ========================================================================== #

#nuke.knobDefault('Tracker4.reference_frame', '1001')
nuke.addOnUserCreate(lambda:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4') # ref frame --> current frame
nuke.knobDefault('Tracker4.adjust_for_luminance_changes', '1') # adj for luma changes --> checked
nuke.knobDefault('Tracker4.cornerPinOptions', "7") # export --> matchmove baked
nuke.knobDefault('Tracker4.hide_progress_bar', '1') # hide progress bar --> checked




# ========================================================================== #
# This section sets the default values for the ScanlineRender node
# ========================================================================== #

nuke.knobDefault("ScanlineRender.antialiasing", "3")
nuke.knobDefault("ScanlineRender.motion_vectors_type", "off")

# motion vector channels
nuke.knobDefault("ScanlineRender.MB_channel", "none")


# ========================================================================== #
# This section sets motion blur to centered as the default for the following nodes
# ========================================================================== #

nuke.knobDefault("Tracker4.shutteroffset", "centered")
nuke.knobDefault('TimeBlur.shutteroffset','centered')
nuke.knobDefault("Transform.shutteroffset", "centered")
nuke.knobDefault("TransformMasked.shutteroffset", "centered")
nuke.knobDefault("CornerPin2D.shutteroffset", "centered")
nuke.knobDefault("MotionBlur2D.shutteroffset","centred")
nuke.knobDefault("MotionBlur3D.shutteroffset","centred")
nuke.knobDefault("Card3D.shutteroffset", "centered")
nuke.knobDefault("ScanlineRender.shutteroffset", "centered")
nuke.knobDefault("Reconcile3D.shutteroffset", "centered")

# ========================================================================== #
# This section sets no clip as the default for the following nodes
# ========================================================================== #

nuke.knobDefault("Project3D.crop", "0")
nuke.knobDefault("Roto.cliptype","no clip")
nuke.knobDefault("RotoPaint.cliptype","no clip")
nuke.knobDefault("Grid.cliptype","no clip")
nuke.knobDefault("Noise.cliptype","no clip")
nuke.knobDefault("Radial.cliptype","no clip")
nuke.knobDefault("Rectangle.cliptype","no clip")
nuke.knobDefault("Ramp.cliptype","no clip")
nuke.knobDefault("Text2.cliptype","no clip")


# ========================================================================== #
# This section hides the default yellow line in the checkerboard node
# ========================================================================== #

# nuke.knobDefault("LensDistortion.gridType", "Thin Line")
nuke.knobDefault("CheckerBoard2.centerlinewidth","0")

# ========================================================================== #
# This section sets the default values for Viewer
# ========================================================================== #

nuke.knobDefault("Viewer.frame_increment", "4")

nuke.knobDefault("Viewer.center_fstop", "0")
nuke.knobDefault("Viewer.useGPUForViewer", "1")
nuke.knobDefault("Viewer.useGPUForInputs", "1")
nuke.knobDefault("Viewer.disableGPUDitherForViewer", "1")
#nuke.knobDefault("Viewer.gl_buffer_depth", "half-float")
nuke.knobDefault("Viewer.gl_buffer_depth", "float")




# ========================================================================== #
# This section sets the default values for localizationPolicy
# ========================================================================== #

# ReadGeo
nuke.knobDefault("ReadGeo2.localizationPolicy", "off")

# -------------------------------------------------------------------------- #

# ========================================================================== #
# 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 C2 A9 32 30 32 35 #
# ========================================================================== #