import nuke

def set_root_format_from_read():
    # Get the Read1 node
    read_node = nuke.toNode('Read1')
    
    # Check if the Read1 node exists
    if read_node:
        # Get the format of the Read1 node
        read_format = read_node.format()
        
        # Get the frame range from the Read1 node
        fr_first = int(read_node['first'].getValue())
        fr_last = int(read_node['last'].getValue())
        
        # Get the width, height, and pixel aspect ratio from the read format
        res_width = read_format.width()
        res_height = read_format.height()
        pixel_aspect = read_format.pixelAspect()
        
        # Create a TCL format string for the new format
        format_name = 'FormatFromRead'
        new_proj_format = f'{res_width} {res_height} {pixel_aspect} FormatFromRead'
        
        # Check if the format already exists in Nuke's format list
        existing_formats = [fmt.name() for fmt in nuke.formats()]
        if format_name not in existing_formats:
            nuke.addFormat(new_proj_format)
        
        # Set the root format to the new format
        nuke.root().knob('format').setValue(format_name)
        
        # Set the first and last frame
        nuke.root().knob('first_frame').setValue(fr_first)
        nuke.root().knob('last_frame').setValue(fr_last)
        
        print(f'Root format set to: {format_name}')
        print(f'Frame range set to: {fr_first}-{fr_last}')
    else:
        print('Read1 node not found')

# Run the function
set_root_format_from_read()
