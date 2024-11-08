import nuke
 
def change_colorspace_to_scene_linear(): 
    # Get the selected nodes
    selected_nodes = nuke.selectedNodes()
     
    # Iterate through the selected nodes and set the colorspace
    for node in selected_nodes:
        if node.Class() == 'Read':
            node['colorspace'].setValue('scene_linear')
     
    # Optional: Refresh the GUI to reflect the changes
    nuke.updateUI()

def main():
    change_colorspace_to_scene_linear()
