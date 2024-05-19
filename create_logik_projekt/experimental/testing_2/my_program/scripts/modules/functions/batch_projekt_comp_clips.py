# Function:     batch_projekt_comp_clips

def batch_projekt_comp_clips(self):
    import flame

    # Get current batch
    self.batch_group = flame.batch

    # Define reel names
    reel_names = ["sources", "reference", "CGI", "mattes", "neat_video", "precomp", "roto", "comp"]

    # Rename 'Schematic Reel' or 'Schematic Reel 1' to 'sources' if it exists
    for reel in flame.batch.reels:
        if reel.name == 'Schematic Reel' or reel.name == 'Schematic Reel 1':
            reel.name = 'sources'
            print(f"Renamed '{reel.name}' to 'sources'.")

    # Create reels that don't exist
    for reel_name in reel_names:
        if not any(reel.name == reel_name for reel in flame.batch.reels):
            flame.batch.create_reel(reel_name)
            print(f"Created new schematic reel named '{reel_name}'.")
        else:
            print(f"Schematic reel named '{reel_name}' already exists.")

    for clip in self.selection:
        self.x_position = clip.pos_x
        self.y_position = clip.pos_y

        self.get_clip_info(clip)

        self.create_batch_nodes(clip)

    self.batch_group.frame_all()

    print('Done.\n')
