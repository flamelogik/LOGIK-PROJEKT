# Function:         add_render_node

def add_render_node():

        # Create render node

        self.render_node = self.batch_group.create_node('Render')

        self.render_node.range_start = self.batch_group.start_frame
        self.render_node.range_end = int(str(self.batch_group.start_frame)) + int(str(self.clip_duration)) - 1

        self.render_node.frame_rate = self.clip_frame_rate

        self.render_node.source_timecode = self.clip_timecode
        self.render_node.record_timecode = self.clip_timecode

        self.render_node.name = self.clip_shot_name + '_comp'
        # self.render_node.name = self.clip_name + '_mattes'
        # self.render_node.name = self.clip_name + '_neat_video'
        # self.render_node.name = self.clip_name + '_precomp'

        # self.render_node.destination = ('Batch Reels', 'comp')
        # self.render_node.destination = ('Batch Reels', 'mattes')
        # self.render_node.destination = ('Batch Reels', 'neat_video')
        # self.render_node.destination = ('Batch Reels', 'precomp')
        self.render_node.destination = ('Libraries')

        # self.render_node.bit_depth = '10-bit'
        self.render_node.bit_depth = '16-bit fp'

        if self.clip_shot_name:
        self.render_node.shot_name = self.clip_shot_name

        # add version note
        self.render_node.note = "This node was configured by projekt_comp."
        # add version note collapsed state
        self.render_node.note_collapsed = True
