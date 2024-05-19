# Function:     media_panel_projekt_comp_clips

def media_panel_projekt_comp_clips(self):
    import flame

    flame.go_to('Batch')

    # Create batch group
    batch_group = flame.batch.create_batch_group('projekt_comp', reels=['sources','reference','CGI','mattes','neat_video','precomp','roto','comp'])

    # Add source clip(s) to 'sources_reel'
    sources_reel = batch_group.reels[0]

    batch_group.expanded = False

    # Copy all clips in selection to batch
    for clip in self.selection:
        flame.media_panel.copy(clip, sources_reel)

    # Create new selection of all clips in batch
    self.selection = flame.batch.nodes
    self.selection.reverse()

    # Repo clips in batch to spread them out

    # clip_pos_y = 200
    clip_pos_y = 192

    for clip in self.selection:
            clip_pos_y += 192
            clip.pos_y = clip_pos_y

    # Set batch duration if duration of current clip is longer than last or Default
    for clip in flame.batch.nodes:
        if int(str(clip.duration)) > int(str(batch_group.duration)):
            batch_group.duration = int(str(clip.duration))

    # Run batch comp clips on all clips in batch
    self.batch_projekt_comp_clips()

    batch_group.frame_all()
