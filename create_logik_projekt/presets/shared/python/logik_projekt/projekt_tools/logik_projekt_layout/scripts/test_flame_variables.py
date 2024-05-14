
import flame

the_current_projekt = flame.projects.current_project
print(f"the_current_projekt")
the_current_workspace = the_current_projekt.current_workspace
the_current_desktop = the_current_workspace.desktop
# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-12 - 15:37:50
# comments:              Added function to read directories from JSON files.
# -------------------------------------------------------------------------- #
# version:               0.0.6
# modified:              2024-05-12 - 18:16:05
# comments:              Added a 'separators' function and tested in flame 2025.
