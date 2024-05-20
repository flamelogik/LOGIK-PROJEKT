'''
Script Name: mmm_mattes
Script Version: 1.1
Script Family: MAN_MADE_MATERIAL
Modified by: Phil MAN phil_man@mac.com
Modification Date: 2023-12-05
Based on original python by: Michael Vaglienty
Creation Date: 2023-04-05
Flame Version: 2025

Custom Action Type: Batch

Description:

    Add MUX/Render/Write nodes to selected clips in batch or select multiple clips in the media panel to build a new
    batch group with MUX/Render/Write nodes for all selected clips.

    Based on Michael Vaglienty's wonderful Neat Freak tool.

    Render/Write node outputs are set to match each clip(name, duration, timecode, fps).

    Write node options can be set in Config.

Menus:

    Config:

        Flame 2023.2+:

            Flame Main Menu -> mmm_python -> mmm_openclip -> configure mmm_mattes

    Batch:

        Flame 2023.2+:

            Right-click on any clip in batch -> mmm_mattes selected clips

    Media Panel:

        Flame 2023.2+:

            Right-click on any clip in media panel -> mmm_mattes selected clips

To install:

    Copy script into /opt/Autodesk/shared/python/man_made_material/openclip_workflow/mmm_mattes

Updates:

    v1.1 2023-12-05

        Updated script to use PySide6 for compatibility with flame 2025.

    v1.0 2023-04-05

        Changed write file parameters to conform to Legacy Method VFX Pipeline constraints.

        Render/Write nodes now take start frame into account when setting render range.

        Colour Management in render node now gets set to 16-bit float, Colour Management node is no longer needed/added.

        Moved menus for Flame 2023.2+:

            Config:

                Flame Main Menu -> mmm_python -> mmm_openclip -> configure mmm_mattes

            Batch:

                Right-click on any clip in batch -> mmm_mattes selected clips

            Media Panel:

                Right-click on any clip in media panel -> mmm_mattes selected clips

        Updated config file loading/saving.

'''

# ---------------------------------------- #
# Imports

from functools import partial
try:
    from PySide6 import QtWidgets, QtCore
except ImportError:
    from PySide2 import QtWidgets, QtCore
from pyflame_lib_mmm_mattes import (
    FlameMessageWindow,
    FlameWindow,
    FlameButton,
    FlameLabel,
    FlameLineEdit,
    FlameSlider,
    FlameTokenPushButton,
    FlamePushButton,
    FlamePushButtonMenu,
    pyflame_print,
    pyflame_file_browser,
    pyflame_get_shot_name,
    pyflame_load_config,
    pyflame_save_config,
)

# ---------------------------------------- #
# Main Script

SCRIPT_NAME = 'mmm_mattes'
SCRIPT_PATH = f'/opt/Autodesk/shared/python/man_made_material/openclip_workflow/{SCRIPT_NAME}'
VERSION = 'v1.1'

class class_mmm_mattes():

    def __init__(self, selection):

        print('\n')
        print('>' * 10, f'{SCRIPT_NAME} {VERSION}', '<' * 10, '\n')

        self.selection = selection

        # Load config file

        self.settings = pyflame_load_config(SCRIPT_NAME, SCRIPT_PATH, {
            'render_node_type': 'Write File Node',
            'write_file_media_path': '/JOBS/',
            'write_file_pattern': '<project nickname>/shots/<shot name>/openclip/renders/<name>_<version name>/<name>_<version name><frame><ext>',
            'write_file_create_open_clip': 'True',
            'write_file_include_setup': 'True',
            'write_file_create_open_clip_value': '<project nickname>/shots/<shot name>/openclip/output_clips/<name><ext>',
            'write_file_include_setup_value': '<project nickname>/shots/<shot name>/openclip/batch_setups/<name>_<version name>_<workstation>_<user nickname><ext>',
            'write_file_image_format': 'OpenEXR 16-bit fp',
            'write_file_compression': 'PIZ',
            'write_file_padding': '8',
            'write_file_frame_index': 'Use Start Frame',
            'write_file_version_name': 'v<version>'
        })

        # Init Variables

        self.y_position = 0
        self.x_position = 0
        self.batch_duration = 1

    # ---------------------------------------- #

    def batch_mmm_mattes_clips(self):
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

    def media_panel_mmm_mattes_clips(self):
        import flame

        flame.go_to('Batch')

        # Create batch group
        batch_group = flame.batch.create_batch_group('mmm_mattes', reels=['sources','reference','CGI','mattes','neat_video','precomp','roto','comp'])

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

        # Run batch mattes clips on all clips in batch
        self.batch_mmm_mattes_clips()

        batch_group.frame_all()

    def get_clip_info(self, clip):
        import flame

        # Get clip values

        self.clip_name = str(clip.name)[1:-1]
        #print('clip_name: ', self.clip_name)

        self.clip_duration = clip.duration
        #print('clip_duration:', self.clip_duration)

        self.clip_frame_rate = clip.clip.frame_rate
        #print('clip_frame_rate:', self.clip_frame_rate)

        self.clip_timecode = clip.clip.start_time
        #print('clip_timecode:', self.clip_timecode)

        self.clip_shot_name = pyflame_get_shot_name(clip)

    def create_batch_nodes(self, clip):
        import flame

        def add_render_node():

            # Create render node

            self.render_node = self.batch_group.create_node('Render')

            self.render_node.range_start = self.batch_group.start_frame
            self.render_node.range_end = int(str(self.batch_group.start_frame)) + int(str(self.clip_duration)) - 1

            self.render_node.frame_rate = self.clip_frame_rate

            self.render_node.source_timecode = self.clip_timecode
            self.render_node.record_timecode = self.clip_timecode

            # self.render_node.name = self.clip_shot_name + '_comp'
            self.render_node.name = self.clip_name + '_mattes'
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
            self.render_node.note = "This node was configured by mmm_mattes."
            # add version note collapsed state
            self.render_node.note_collapsed = True

        def add_write_node():

            # Create write node

            self.render_node = flame.batch.create_node('Write File')

            self.render_node.range_start = int(str(flame.batch.start_frame))
            self.render_node.range_end = int(str(self.batch_group.start_frame)) + int(str(self.clip_duration)) - 1

            self.render_node.frame_rate = self.clip_frame_rate

            self.render_node.source_timecode = self.clip_timecode
            self.render_node.record_timecode = self.clip_timecode

            # self.render_node.name = self.clip_shot_name + '_comp'
            self.render_node.name = self.clip_name + '_mattes'
            # self.render_node.name = self.clip_name + '_neat_video'
            # self.render_node.name = self.clip_name + '_precomp'

            # self.render_node.destination = ('Batch Reels', 'comp')
            self.render_node.destination = ('Batch Reels', 'mattes')
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
            self.render_node.note = "This node was configured by mmm_mattes."
            # add version note collapsed state
            self.render_node.note_collapsed = True

            if self.settings.write_file_create_open_clip:
                # self.render_node.version_mode = 'Follow Iteration' # Enable for final comps.
                self.render_node.version_mode = 'Custom Version' # Enable for intermediate renders.
                self.render_node.version_name = self.settings.write_file_version_name

                # add version number
                self.render_node.version_number = 1 # Enable if using 'Custom Version'
                # add version padding
                self.render_node.version_padding = 4 # Enable if using 'Custom Version'

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

        pyflame_print(SCRIPT_NAME, f'Added MUX nodes added for: {self.clip_name}')

    # ---------------------------------------- #

    def write_node_setup(self):

        def save_config():

            if not self.write_file_media_path_lineedit.text():
                FlameMessageWindow('error', f'{SCRIPT_NAME}: Error', 'Write Node Setup: Enter Media Path.')
            elif not self.write_file_pattern_lineedit.text():
                FlameMessageWindow('error', f'{SCRIPT_NAME}: Error', 'Write Node Setup: Enter Pattern for image files.')
            elif not self.write_file_create_open_clip_lineedit.text():
                FlameMessageWindow('error', f'{SCRIPT_NAME}: Error', 'Write Node Setup: Enter Create Open Clip Naming.')
            elif not self.write_file_include_setup_lineedit.text():
                FlameMessageWindow('error', f'{SCRIPT_NAME}: Error', 'Write Node Setup: Enter Include Setup Naming.')
            elif not self.write_file_version_name_lineedit.text():
                FlameMessageWindow('error', f'{SCRIPT_NAME}: Error', 'Write Node Setup: Enter Version Naming.')
            else:
                pyflame_save_config(SCRIPT_NAME, SCRIPT_PATH, {
                    'render_node_type': self.write_file_render_node_type_push_btn.text(),
                    'write_file_media_path': self.write_file_media_path_lineedit.text(),
                    'write_file_pattern': self.write_file_pattern_lineedit.text(),
                    'write_file_create_open_clip': str(self.write_file_create_open_clip_btn.isChecked()),
                    'write_file_include_setup': str(self.write_file_include_setup_btn.isChecked()),
                    'write_file_create_open_clip_value': self.write_file_create_open_clip_lineedit.text(),
                    'write_file_include_setup_value': self.write_file_include_setup_lineedit.text(),
                    'write_file_image_format': self.write_file_image_format_push_btn.text(),
                    'write_file_compression': self.write_file_compression_push_btn.text(),
                    'write_file_padding': self.write_file_padding_slider.text(),
                    'write_file_frame_index': self.write_file_frame_index_push_btn.text(),
                    'write_file_version_name': self.write_file_version_name_lineedit.text(),
                })

                self.setup_window.close()

        def write_file_create_open_clip_btn_check():
            if self.write_file_create_open_clip_btn.isChecked():
                self.write_file_create_open_clip_lineedit.setDisabled(False)
                self.write_file_open_clip_token_btn.setDisabled(False)
            else:
                self.write_file_create_open_clip_lineedit.setDisabled(True)
                self.write_file_open_clip_token_btn.setDisabled(True)

        def write_file_include_setup_btn_check():
            if self.write_file_include_setup_btn.isChecked():
                self.write_file_include_setup_lineedit.setDisabled(False)
                self.write_file_include_setup_token_btn.setDisabled(False)
            else:
                self.write_file_include_setup_lineedit.setDisabled(True)
                self.write_file_include_setup_token_btn.setDisabled(True)

        def render_node_type_toggle():

            if self.write_file_render_node_type_push_btn.text() == 'Render Node':
                self.write_file_setup_label.setDisabled(True)
                self.write_file_media_path_label.setDisabled(True)
                self.write_file_pattern_label.setDisabled(True)
                self.write_file_type_label.setDisabled(True)
                self.write_file_frame_index_label.setDisabled(True)
                self.write_file_padding_label.setDisabled(True)
                self.write_file_compression_label.setDisabled(True)
                self.write_file_settings_label.setDisabled(True)
                self.write_file_version_name_label.setDisabled(True)
                self.write_file_media_path_lineedit.setDisabled(True)
                self.write_file_pattern_lineedit.setDisabled(True)
                self.write_file_create_open_clip_lineedit.setDisabled(True)
                self.write_file_include_setup_lineedit.setDisabled(True)
                self.write_file_version_name_lineedit.setDisabled(True)
                self.write_file_padding_slider.setDisabled(True)
                self.write_file_image_format_push_btn.setDisabled(True)
                self.write_file_compression_push_btn.setDisabled(True)
                self.write_file_frame_index_push_btn.setDisabled(True)
                self.write_file_pattern_token_btn.setDisabled(True)
                self.write_file_browse_btn.setDisabled(True)
                self.write_file_include_setup_btn.setDisabled(True)
                self.write_file_create_open_clip_btn.setDisabled(True)
                self.write_file_open_clip_token_btn.setDisabled(True)
                self.write_file_include_setup_token_btn.setDisabled(True)
            else:
                self.write_file_setup_label.setDisabled(False)
                self.write_file_media_path_label.setDisabled(False)
                self.write_file_pattern_label.setDisabled(False)
                self.write_file_type_label.setDisabled(False)
                self.write_file_frame_index_label.setDisabled(False)
                self.write_file_padding_label.setDisabled(False)
                self.write_file_compression_label.setDisabled(False)
                self.write_file_settings_label.setDisabled(False)
                self.write_file_version_name_label.setDisabled(False)
                self.write_file_media_path_lineedit.setDisabled(False)
                self.write_file_pattern_lineedit.setDisabled(False)
                self.write_file_create_open_clip_lineedit.setDisabled(False)
                self.write_file_include_setup_lineedit.setDisabled(False)
                self.write_file_version_name_lineedit.setDisabled(False)
                self.write_file_padding_slider.setDisabled(False)
                self.write_file_image_format_push_btn.setDisabled(False)
                self.write_file_compression_push_btn.setDisabled(False)
                self.write_file_frame_index_push_btn.setDisabled(False)
                self.write_file_pattern_token_btn.setDisabled(False)
                self.write_file_browse_btn.setDisabled(False)
                self.write_file_include_setup_btn.setDisabled(False)
                self.write_file_create_open_clip_btn.setDisabled(False)
                self.write_file_open_clip_token_btn.setDisabled(False)
                self.write_file_include_setup_token_btn.setDisabled(False)

                write_file_create_open_clip_btn_check()

                write_file_include_setup_btn_check()

        def media_path_browse():

            file_path = pyflame_file_browser('Select Directory', [''], self.write_file_media_path_lineedit.text(), select_directory=True, window_to_hide=[self.setup_window])

            if file_path:
                self.write_file_media_path_lineedit.setText(file_path)

        gridbox = QtWidgets.QGridLayout()
        self.setup_window = FlameWindow(f'{SCRIPT_NAME}: Render/Write Node Setup <small>{VERSION}', gridbox, 1000, 570)

        # Labels

        self.write_file_render_node_type_label = FlameLabel('Render Node Type')
        self.write_file_setup_label = FlameLabel('Write File Node Setup', label_type='underline')
        self.write_file_media_path_label = FlameLabel('Media Path')
        self.write_file_pattern_label = FlameLabel('Pattern')
        self.write_file_type_label = FlameLabel('File Type')
        self.write_file_frame_index_label = FlameLabel('Frame Index')
        self.write_file_padding_label = FlameLabel('Padding')
        self.write_file_compression_label = FlameLabel('Compression')
        self.write_file_settings_label = FlameLabel('Settings', label_type='underline')
        self.write_file_version_name_label = FlameLabel('Version Name')

        # LineEdits

        self.write_file_media_path_lineedit = FlameLineEdit(self.settings.write_file_media_path)
        self.write_file_pattern_lineedit = FlameLineEdit(self.settings.write_file_pattern)
        self.write_file_create_open_clip_lineedit = FlameLineEdit(self.settings.write_file_create_open_clip_value)
        self.write_file_include_setup_lineedit = FlameLineEdit(self.settings.write_file_include_setup_value)
        self.write_file_version_name_lineedit = FlameLineEdit(self.settings.write_file_version_name, max_width=150)

        # Sliders

        self.write_file_padding_slider = FlameSlider(int(self.settings.write_file_padding), 1, 20, value_is_float=False, slider_width=150)

        # Image format pushbutton

        image_format_menu = QtWidgets.QMenu(self.setup_window)
        image_format_menu.setStyleSheet('QMenu {color: #9a9a9a; background-color:#2d3744; border: none; font: 14px "Discreet"}'
                                        'QMenu::item:selected {color: #d9d9d9; background-color: #3a4551}')

        self.write_file_image_format_push_btn = QtWidgets.QPushButton(self.settings.write_file_image_format)
        self.write_file_image_format_push_btn.setMenu(image_format_menu)
        self.write_file_image_format_push_btn.setMinimumSize(QtCore.QSize(150, 28))
        self.write_file_image_format_push_btn.setMaximumSize(QtCore.QSize(150, 28))
        self.write_file_image_format_push_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.write_file_image_format_push_btn.setStyleSheet('QPushButton {color: #9a9a9a; background-color: #2d3744; border: none; font: 14px "Discreet"}'
                                                            'QPushButton:hover {border: 1px solid #5a5a5a}'
                                                            'QPushButton:disabled {color: #747474; background-color: #2d3744; border: none}'
                                                            'QPushButton::menu-indicator { image: none; }')

        # -------------------------------------------------------------

        def compression(file_format):

            def create_menu(option):
                self.write_file_compression_push_btn.setText(option)

            compression_menu.clear()

            self.write_file_image_format_push_btn.setText(file_format)

            if 'Dpx' in file_format:
                self.write_file_compression_push_btn.setText('Uncompressed')
                compression_list = ['Uncompressed', 'Pixspan', 'Packed']
                self.write_file_compression_push_btn.setEnabled(True)

            elif 'Jpeg' in file_format:
                self.write_file_compression_push_btn.setText('')
                compression_list = []
                self.write_file_compression_push_btn.setEnabled(False)

            elif 'OpenEXR' in file_format:
                # self.write_file_compression_push_btn.setText('Uncompressed')
                self.write_file_compression_push_btn.setText('PIZ')
                compression_list = ['Uncompressed', 'Scanline', 'Multi_Scanline', 'RLE', 'PXR24', 'PIZ', 'DWAB', 'DWAA', 'B44A', 'B44']
                self.write_file_compression_push_btn.setEnabled(True)

            elif 'Png' in file_format:
                self.write_file_compression_push_btn.setText('')
                compression_list = []
                self.write_file_compression_push_btn.setEnabled(False)

            elif 'Sgi' in file_format:
                self.write_file_compression_push_btn.setText('Uncompressed')
                compression_list = ['Uncompressed', 'RLE']
                self.write_file_compression_push_btn.setEnabled(True)

            elif 'Targa' in file_format:
                self.write_file_compression_push_btn.setText('')
                compression_list = []
                self.write_file_compression_push_btn.setEnabled(False)

            elif 'Tiff' in file_format:
                self.write_file_compression_push_btn.setText('Uncompressed')
                compression_list = ['Uncompressed', 'RLE', 'LZW']
                self.write_file_compression_push_btn.setEnabled(True)

            for option in compression_list:
                compression_menu.addAction(option, partial(create_menu, option))

        image_format_menu.addAction('Dpx 8-bit', partial(compression, 'Dpx 8-bit'))
        image_format_menu.addAction('Dpx 10-bit', partial(compression, 'Dpx 10-bit'))
        image_format_menu.addAction('Dpx 12-bit', partial(compression, 'Dpx 12-bit'))
        image_format_menu.addAction('Dpx 16-bit', partial(compression, 'Dpx 16-bit'))
        image_format_menu.addAction('Jpeg 8-bit', partial(compression, 'Jpeg 8-bit'))
        image_format_menu.addAction('OpenEXR 16-bit fp', partial(compression, 'OpenEXR 16-bit fp'))
        image_format_menu.addAction('OpenEXR 32-bit fp', partial(compression, 'OpenEXR 32-bit fp'))
        image_format_menu.addAction('Png 8-bit', partial(compression, 'Png 8-bit'))
        image_format_menu.addAction('Png 16-bit', partial(compression, 'Png 16-bit'))
        image_format_menu.addAction('Sgi 8-bit', partial(compression, 'Sgi 8-bit'))
        image_format_menu.addAction('Sgi 16-bit', partial(compression, 'Sgi 16-bit'))
        image_format_menu.addAction('Targa 8-bit', partial(compression, 'Targa 8-bit'))
        image_format_menu.addAction('Tiff 8-bit', partial(compression, 'Tiff 8-bit'))
        image_format_menu.addAction('Tiff 16-bit', partial(compression, 'Tiff 16-bit'))

        compression_menu = QtWidgets.QMenu(self.setup_window)
        compression_menu.setStyleSheet('QMenu {color: #9a9a9a; background-color:#2d3744; border: none; font: 14px "Discreet"}'
                                    'QMenu::item:selected {color: #d9d9d9; background-color: #3a4551}')

        self.write_file_compression_push_btn = QtWidgets.QPushButton(self.settings.write_file_compression)
        self.write_file_compression_push_btn.setMenu(compression_menu)
        self.write_file_compression_push_btn.setMinimumSize(QtCore.QSize(150, 28))
        self.write_file_compression_push_btn.setMaximumSize(QtCore.QSize(150, 28))
        self.write_file_compression_push_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.write_file_compression_push_btn.setStyleSheet('QPushButton {color: #9a9a9a; background-color: #2d3744; border: none; font: 14px "Discreet"}'
                                                        'QPushButton:hover {border: 1px solid #5a5a5a}'
                                                        'QPushButton:disabled {color: #747474; background-color: #2d3744; border: none}'
                                                        'QPushButton::menu-indicator { image: none; }')
        self.write_file_compression_push_btn.setText(self.settings.write_file_compression)

        # Render Type Pushbutton Menu

        render_node_options = ['Render Node', 'Write File Node']
        self.write_file_render_node_type_push_btn = FlamePushButtonMenu(self.settings.render_node_type, render_node_options, menu_action=render_node_type_toggle)

        # Frame Index Pushbutton Menu

        frame_index = ['Use Start Frame', 'Use Timecode']
        self.write_file_frame_index_push_btn = FlamePushButtonMenu(self.settings.write_file_frame_index, frame_index)

        # Token Push Buttons

        write_file_token_dict = {'Batch Name': '<batch name>', 'Batch Iteration': '<batch iteration>', 'Iteration': '<iteration>',
                                'Project': '<project>', 'Project Nickname': '<project nickname>', 'Shot Name': '<shot name>', 'Clip Height': '<height>',
                                'Clip Width': '<width>', 'Clip Name': '<name>', }

        self.write_file_pattern_token_btn = FlameTokenPushButton('Add Token', write_file_token_dict, self.write_file_pattern_lineedit)
        self.write_file_open_clip_token_btn = FlameTokenPushButton('Add Token', write_file_token_dict, self.write_file_create_open_clip_lineedit)
        self.write_file_include_setup_token_btn = FlameTokenPushButton('Add Token', write_file_token_dict, self.write_file_include_setup_lineedit)

        # Pushbuttons

        self.write_file_create_open_clip_btn = FlamePushButton('Create Open Clip', self.settings.write_file_create_open_clip)
        self.write_file_create_open_clip_btn.clicked.connect(write_file_create_open_clip_btn_check)
        write_file_create_open_clip_btn_check()

        self.write_file_include_setup_btn = FlamePushButton('Include Setup', self.settings.write_file_include_setup)
        self.write_file_include_setup_btn.clicked.connect(write_file_include_setup_btn_check)
        write_file_include_setup_btn_check()

        # Buttons

        self.write_file_browse_btn = FlameButton('Browse', media_path_browse)
        self.write_file_save_btn = FlameButton('Save', save_config)
        self.write_file_cancel_btn = FlameButton('Cancel', self.setup_window.close)

        # ------------------------------------------------------------- #

        compression(self.write_file_image_format_push_btn.text())
        self.write_file_compression_push_btn.setText(self.settings.write_file_compression)

        render_node_type_toggle()

        # UI Widget layout

        gridbox.setContentsMargins(20, 20, 20, 20)# gridbox.setMargin(20)  # Fix for flame 2025
        gridbox.setVerticalSpacing(5)
        gridbox.setHorizontalSpacing(5)
        gridbox.setRowStretch(3, 2)
        gridbox.setRowStretch(6, 2)
        gridbox.setRowStretch(9, 2)

        gridbox.addWidget(self.write_file_render_node_type_label, 0, 0)
        gridbox.addWidget(self.write_file_render_node_type_push_btn, 0, 1)

        gridbox.addWidget(self.write_file_setup_label, 1, 0, 1, 6)

        gridbox.addWidget(self.write_file_media_path_label, 2, 0)
        gridbox.addWidget(self.write_file_media_path_lineedit, 2, 1, 1, 4)
        gridbox.addWidget(self.write_file_browse_btn, 2, 5)

        gridbox.addWidget(self.write_file_pattern_label, 3, 0)
        gridbox.addWidget(self.write_file_pattern_lineedit, 3, 1, 1, 4)
        gridbox.addWidget(self.write_file_pattern_token_btn, 3, 5)

        gridbox.setRowMinimumHeight(4, 28)

        gridbox.addWidget(self.write_file_create_open_clip_btn, 5, 0)
        gridbox.addWidget(self.write_file_create_open_clip_lineedit, 5, 1, 1, 4)
        gridbox.addWidget(self.write_file_open_clip_token_btn, 5, 5)

        gridbox.addWidget(self.write_file_include_setup_btn, 6, 0)
        gridbox.addWidget(self.write_file_include_setup_lineedit, 6, 1, 1, 4)
        gridbox.addWidget(self.write_file_include_setup_token_btn, 6, 5)

        gridbox.setRowMinimumHeight(7, 28)

        gridbox.addWidget(self.write_file_settings_label, 8, 0, 1, 5)
        gridbox.addWidget(self.write_file_frame_index_label, 9, 0)
        gridbox.addWidget(self.write_file_frame_index_push_btn, 9, 1)
        gridbox.addWidget(self.write_file_type_label, 10, 0)
        gridbox.addWidget(self.write_file_image_format_push_btn, 10, 1)
        gridbox.addWidget(self.write_file_compression_label, 11, 0)
        gridbox.addWidget(self.write_file_compression_push_btn, 11, 1)

        gridbox.addWidget(self.write_file_padding_label, 9, 2)
        gridbox.addWidget(self.write_file_padding_slider, 9, 3)
        #gridbox.addWidget(self.write_file_iteration_padding_label, 10, 2)
        #gridbox.addWidget(self.write_file_iteration_padding_slider, 10, 3)
        gridbox.addWidget(self.write_file_version_name_label, 11, 2)
        gridbox.addWidget(self.write_file_version_name_lineedit, 11, 3)

        gridbox.addWidget(self.write_file_save_btn, 13, 5)
        gridbox.addWidget(self.write_file_cancel_btn, 14, 5)

        self.setup_window.show()

# ---------------------------------------- #

def mmm_mattes_media_panel_clips(selection):

    script = class_mmm_mattes(selection)
    script.media_panel_mmm_mattes_clips()

def mmm_mattes_batch_clips(selection):

    script = class_mmm_mattes(selection)
    script.batch_mmm_mattes_clips()

def setup(selection):

    script = class_mmm_mattes(selection)
    script.write_node_setup()

# ---------------------------------------- #
# Scopes

def scope_clip(selection):
    import flame

    for item in selection:
        if isinstance(item, (flame.PyClip, flame.PyClipNode)):
            return True
    return False

def scope_folder(selection):
    import flame

    for item in selection:
        if isinstance(item, (flame.PyFolder)):
            return True
    return False

def scope_library(selection):
    import flame

    for item in selection:
        if isinstance(item, (flame.PyLibrary)):
            return True
    return False

def scope_segment(selection):
    import flame

    for item in selection:
        if isinstance(item, flame.PySegment):
            return True
    return False

def scope_seq(selection):
    import flame

    for item in selection:
        if isinstance(item, flame.PySequence):
            return True
    return False

# ---------------------------------------- #
# Flame Menus

def get_batch_custom_ui_actions():

    return [
        {
            'name': 'mmm_python',
            'hierarchy': [],
            'actions': []
        },
        {
            'name': 'mmm_openclip',
            'hierarchy': ['mmm_python'],
            'order': 2,
            'actions': [
               {
                    'name': 'mmm_mattes selected clips',
                    'order': 2,
                    'separator': 'below',
                    'isVisible': scope_clip,
                    'execute': mmm_mattes_batch_clips,
                    'minimumVersion': '2025'
               }
           ]
        }
    ]

def get_main_menu_custom_ui_actions():

    return [
        {
            'name': 'mmm_python',
            'hierarchy': [],
            'actions': []
        },
        {
            'name': 'mmm_openclip',
            'hierarchy': ['mmm_python'],
            'order': 2,
            'actions': [
               {
                    'name': 'configure mmm_mattes',
                    'execute': setup,
                    'minimumVersion': '2025'
               }
           ]
        }
    ]

def get_media_panel_custom_ui_actions():

    return [
        {
            'name': 'mmm_python',
            'hierarchy': [],
            'actions': []
        },
        {
            'name': 'mmm_openclip',
            'hierarchy': ['mmm_python'],
            'order': 2,
            'actions': [
               {
                    'name': 'mmm_mattes selected clips',
                    'order': 2,
                    'separator': 'below',
                    'isVisible': scope_clip,
                    'execute': mmm_mattes_media_panel_clips,
                    'minimumVersion': '2025'
               }
           ]
        }
    ]

# def get_timeline_custom_ui_actions():

#     return [
#         {
#             'name': 'mmm_python',
#             'hierarchy': [],
#             'actions': []
#         },
#         {
#             'name': 'mmm_openclip',
#             'hierarchy': ['mmm_python'],
#             'order': 0,
#             'actions': [
#                 {
#                     'name': 'mmm_comp selected clips',
#                     'order': 0,
#                     'separator': 'below',
#                     "isVisible": scope_segment,
#                     'execute': mmm_mattes_media_panel_clips,
#                     'minimumVersion': '2025'
#                 }
#             ]
#         }

#      ]
