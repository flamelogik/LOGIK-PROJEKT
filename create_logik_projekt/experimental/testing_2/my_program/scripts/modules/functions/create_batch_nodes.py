# Function:     create_batch_nodes


    def create_batch_nodes(self, clip):
        import flame

        # def add_render_node():

        #     # Create render node

        #     self.render_node = self.batch_group.create_node('Render')

        #     self.render_node.range_start = self.batch_group.start_frame
        #     self.render_node.range_end = int(str(self.batch_group.start_frame)) + int(str(self.clip_duration)) - 1

        #     self.render_node.frame_rate = self.clip_frame_rate

        #     self.render_node.source_timecode = self.clip_timecode
        #     self.render_node.record_timecode = self.clip_timecode

        #     self.render_node.name = self.clip_shot_name + '_comp'
        #     # self.render_node.name = self.clip_name + '_mattes'
        #     # self.render_node.name = self.clip_name + '_neat_video'
        #     # self.render_node.name = self.clip_name + '_precomp'

        #     # self.render_node.destination = ('Batch Reels', 'comp')
        #     # self.render_node.destination = ('Batch Reels', 'mattes')
        #     # self.render_node.destination = ('Batch Reels', 'neat_video')
        #     # self.render_node.destination = ('Batch Reels', 'precomp')
        #     self.render_node.destination = ('Libraries')

        #     # self.render_node.bit_depth = '10-bit'
        #     self.render_node.bit_depth = '16-bit fp'

        #     if self.clip_shot_name:
        #         self.render_node.shot_name = self.clip_shot_name

        #     # add version note
        #     self.render_node.note = "This node was configured by projekt_comp."
        #     # add version note collapsed state
        #     self.render_node.note_collapsed = True

        # def add_write_node():

        #     # Create write node

        #     self.render_node = flame.batch.create_node('Write File')

        #     self.render_node.range_start = int(str(flame.batch.start_frame))
        #     self.render_node.range_end = int(str(self.batch_group.start_frame)) + int(str(self.clip_duration)) - 1

        #     self.render_node.frame_rate = self.clip_frame_rate

        #     self.render_node.source_timecode = self.clip_timecode
        #     self.render_node.record_timecode = self.clip_timecode

        #     self.render_node.name = self.clip_shot_name + '_comp'
        #     # self.render_node.name = self.clip_name + '_mattes'
        #     # self.render_node.name = self.clip_name + '_neat_video'
        #     # self.render_node.name = self.clip_name + '_precomp'

        #     self.render_node.destination = ('Batch Reels', 'comp')
        #     # self.render_node.destination = ('Batch Reels', 'mattes')
        #     # self.render_node.destination = ('Batch Reels', 'neat_video')
        #     # self.render_node.destination = ('Batch Reels', 'precomp')

        #     # self.render_node.destination = ('Libraries')

        #     image_format = self.settings.write_file_image_format.split(' ', 1)[0]
        #     bit_depth = self.settings.write_file_image_format.split(' ', 1)[1]

        #     self.render_node.file_type = image_format
        #     self.render_node.bit_depth = bit_depth

        #     self.render_node.media_path = self.settings.write_file_media_path
        #     self.render_node.media_path_pattern = self.settings.write_file_pattern
        #     self.render_node.create_clip = self.settings.write_file_create_open_clip
        #     self.render_node.include_setup = self.settings.write_file_include_setup
        #     self.render_node.create_clip_path = self.settings.write_file_create_open_clip_value
        #     self.render_node.include_setup_path = self.settings.write_file_include_setup_value

        #     if self.settings.write_file_compression:
        #         self.render_node.compress = True
        #         self.render_node.compress_mode = self.settings.write_file_compression
        #     if image_format == 'Jpeg':
        #         self.render_node.quality = 100

        #     self.render_node.frame_index_mode = self.settings.write_file_frame_index
        #     self.render_node.frame_padding = int(self.settings.write_file_padding)

        #     self.render_node.shot_name = self.clip_shot_name

        #     # add version note
        #     self.render_node.note = "This node was configured by projekt_comp."
        #     # add version note collapsed state
        #     self.render_node.note_collapsed = True

        #     if self.settings.write_file_create_open_clip:
        #         self.render_node.version_mode = 'Follow Iteration' # Enable for final comps.
        #         # self.render_node.version_mode = 'Custom Version' # Enable for intermediate renders.
        #         self.render_node.version_name = self.settings.write_file_version_name

        #         # add version number
        #         # self.render_node.version_number = 1 # Enable if using 'Custom Version'
        #         # add version padding
        #         # self.render_node.version_padding = 4 # Enable if using 'Custom Version'

        # Add MUX node

        mux_node = self.batch_group.create_node('MUX')
        mux_node.pos_x = self.x_position + 288
        mux_node.pos_y = self.y_position - 24

        # Add neat video node

        # neat_video_node = self.batch_group.create_node('OpenFX')
        # neat_video_node.change_plugin('Reduce Noise v5')
        # neat_video_node.pos_x = self.x_position + 288
        # neat_video_node.pos_y = self.y_position - 24

        # Add Render Node or Write File Node

        if self.settings.render_node_type == 'Render Node':
            add_render_node()
        else:
            add_write_node()

        self.render_node.pos_x = mux_node.pos_x + 288
        self.render_node.pos_y = mux_node.pos_y - 0

        # Connect nodes

        flame.batch.connect_nodes(clip, 'Default', mux_node, 'Default')
        flame.batch.connect_nodes(mux_node, 'Default', self.render_node, 'Default')
        # flame.batch.connect_nodes(clip, 'Default', neat_video_node, 'Default')
        # flame.batch.connect_nodes(neat_video_node, 'Default', self.render_node, 'Default')

        self.y_position = self.y_position - 192

        pyside6_qt_print(SCRIPT_NAME, f'Added MUX nodes added for: {self.clip_name}')
