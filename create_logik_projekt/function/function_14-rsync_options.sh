#!/bin/bash

# -------------------------------------------------------------------------- #

# filename: "subprograms/sub_18-rsync_vars.sh"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section creates a variable to store rsync options.
# ========================================================================== #

# The following command is too long:
# 'rsync -av --no-group --no-perms --no-times --size-only --ignore-existing '

# Wrap the rsync options as an array into the variable 'sync_opts'
# sync_opts=(-av --no-group --no-perms --no-times --size-only --ignore-existing)
# sync_opts="-av --no-group --no-perms --no-times --size-only --ignore-existing"
sync_opts="-Rav"

# To use the variable in your rsync command
# rsync "${sync_opts[@]}" source_directory/ destination_directory/

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #
