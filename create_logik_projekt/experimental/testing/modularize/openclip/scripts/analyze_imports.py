# filename: analyze_imports.py

'''
# -------------------------------------------------------------------------- #

# File Name:        analyze_imports.py
# Version:          0.0.4
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-05-09
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program is a tool to analyze python imports.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Attribution:      This script is derived from work originally authored by
#                   Michael Vaglienty: 'pyflame_lib_script_template.py'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #
'''

'''
import modulegraph.modulegraph as mg

# Instantiate a ModuleGraph object.
mg_obj = mg.ModuleGraph()

# Add your project files to the ModuleGraph object using the add_package()
# or add_script() method.

# mg_obj.add_package('path.to.your.package')
# # or
# mg_obj.add_script('path/to/your/script.py')

mg_obj.run_script('create_logik_projekt/experimental/testing/modularize/openclip/scripts/modules/functions/pyflame_file_browser.py')
mg_obj.run_script('create_logik_projekt/experimental/testing/modularize/openclip/scripts/modules/functions/pyflame_get_flame_version.py')
mg_obj.run_script('create_logik_projekt/experimental/testing/modularize/openclip/scripts/modules/functions/pyflame_get_shot_name.py')
mg_obj.run_script('create_logik_projekt/experimental/testing/modularize/openclip/scripts/modules/functions/pyflame_load_config.py')
mg_obj.run_script('create_logik_projekt/experimental/testing/modularize/openclip/scripts/modules/functions/pyflame_open_in_finder.py')
mg_obj.run_script('create_logik_projekt/experimental/testing/modularize/openclip/scripts/modules/functions/pyflame_print.py')
mg_obj.run_script('create_logik_projekt/experimental/testing/modularize/openclip/scripts/modules/functions/pyflame_refresh_hooks.py')
mg_obj.run_script('create_logik_projekt/experimental/testing/modularize/openclip/scripts/modules/functions/pyflame_resolve_path_tokens.py')
mg_obj.run_script('create_logik_projekt/experimental/testing/modularize/openclip/scripts/modules/functions/pyflame_resolve_shot_name.py')
mg_obj.run_script('create_logik_projekt/experimental/testing/modularize/openclip/scripts/modules/functions/pyflame_save_config.py')

# Analyze the dependencies using the create_xref() method.
mg_obj.create_xref()

# Use the cycles() method to check for circular imports.
circular_imports = mg_obj.find_cycles()
if circular_imports:
    print("Circular imports found:")
    for cycle in circular_imports:
        print(cycle)
else:
    print("No circular imports found.")
'''

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #

# Changelist:
# -------------------------------------------------------------------------- #
# version:               0.0.1
# modified:              2024-05-07 - 21:48:20
# comments:              Refactored monolithic code to discreet modules
# -------------------------------------------------------------------------- #
# version:               0.0.2
# modified:              2024-05-07 - 21:49:31
# comments:              Added docstrings
# -------------------------------------------------------------------------- #
# version:               0.0.3
# modified:              2024-05-07 - 21:50:00
# comments:              Prep for initial production test
# -------------------------------------------------------------------------- #
# version:               0.0.4
# modified:              2024-05-09 - 13:18:47
# comments:              Refactored code works in flame 2025. Time to tidy up.
