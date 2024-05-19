# Function:         add_write_node

def add_write_node():

        # Create write node

        self.render_node = flame.batch.create_node('Write File')

        self.render_node.range_start = int(str(flame.batch.start_frame))
        self.render_node.range_end = int(str(self.batch_group.start_frame)) + int(str(self.clip_duration)) - 1

        self.render_node.frame_rate = self.clip_frame_rate

        self.render_node.source_timecode = self.clip_timecode
        self.render_node.record_timecode = self.clip_timecode

        self.render_node.name = self.clip_shot_name + '_comp'
        # self.render_node.name = self.clip_name + '_mattes'
        # self.render_node.name = self.clip_name + '_neat_video'
        # self.render_node.name = self.clip_name + '_precomp'

        self.render_node.destination = ('Batch Reels', 'comp')
        # self.render_node.destination = ('Batch Reels', 'mattes')
        # self.render_node.destination = ('Batch Reels', 'neat_video')
        # self.render_node.destination = ('Batch Reels', 'precomp')

        # self.render_node.destination = ('Libraries')

        image_format = self.settings.write_file_image_format.split(' ', 1)[0]
        bit_depth = self.settings.write_file_image_format.split(' ', 1)[1]

        self.render_node.file_type = image_format
        self.render_node.bit_depth = bit_depth

        self.render_node.media_path = self.settings.write_file_media_path
        self.render_node.media_path_pattern = self.settings.write_file_pattern
        self.render_node.create_clip = self.settings.write_file_create_open_clip
        self.render_node.include_setup = self.settings.write_file_include_setup
        self.render_node.create_clip_path = self.settings.write_file_create_open_clip_value
        self.render_node.include_setup_path = self.settings.write_file_include_setup_value

        if self.settings.write_file_compression:
        self.render_node.compress = True
        self.render_node.compress_mode = self.settings.write_file_compression
        if image_format == 'Jpeg':
        self.render_node.quality = 100

        self.render_node.frame_index_mode = self.settings.write_file_frame_index
        self.render_node.frame_padding = int(self.settings.write_file_padding)

        self.render_node.shot_name = self.clip_shot_name

        # add version note
        self.render_node.note = "This node was configured by projekt_comp."
        # add version note collapsed state
        self.render_node.note_collapsed = True

        if self.settings.write_file_create_open_clip:
        self.render_node.version_mode = 'Follow Iteration' # Enable for final comps.
        # self.render_node.version_mode = 'Custom Version' # Enable for intermediate renders.
        self.render_node.version_name = self.settings.write_file_version_name

        # add version number
        # self.render_node.version_number = 1 # Enable if using 'Custom Version'
        # add version padding
        # self.render_node.version_padding = 4 # Enable if using 'Custom Version'
