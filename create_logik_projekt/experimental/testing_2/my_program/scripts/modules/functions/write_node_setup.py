# Function:     write_node_setup

    def write_node_setup(self):

        # def save_config():

        #     if not self.write_file_media_path_lineedit.text():
        #         pyside6_qt_message_window('error', f'{SCRIPT_NAME}: Error', 'Write Node Setup: Enter Media Path.')
        #     elif not self.write_file_pattern_lineedit.text():
        #         pyside6_qt_message_window('error', f'{SCRIPT_NAME}: Error', 'Write Node Setup: Enter Pattern for image files.')
        #     elif not self.write_file_create_open_clip_lineedit.text():
        #         pyside6_qt_message_window('error', f'{SCRIPT_NAME}: Error', 'Write Node Setup: Enter Create Open Clip Naming.')
        #     elif not self.write_file_include_setup_lineedit.text():
        #         pyside6_qt_message_window('error', f'{SCRIPT_NAME}: Error', 'Write Node Setup: Enter Include Setup Naming.')
        #     elif not self.write_file_version_name_lineedit.text():
        #         pyside6_qt_message_window('error', f'{SCRIPT_NAME}: Error', 'Write Node Setup: Enter Version Naming.')
        #     else:
        #         pyside6_qt_save_config(SCRIPT_NAME, SCRIPT_PATH, {
        #             'render_node_type': self.write_file_render_node_type_push_btn.text(),
        #             'write_file_media_path': self.write_file_media_path_lineedit.text(),
        #             'write_file_pattern': self.write_file_pattern_lineedit.text(),
        #             'write_file_create_open_clip': str(self.write_file_create_open_clip_btn.isChecked()),
        #             'write_file_include_setup': str(self.write_file_include_setup_btn.isChecked()),
        #             'write_file_create_open_clip_value': self.write_file_create_open_clip_lineedit.text(),
        #             'write_file_include_setup_value': self.write_file_include_setup_lineedit.text(),
        #             'write_file_image_format': self.write_file_image_format_push_btn.text(),
        #             'write_file_compression': self.write_file_compression_push_btn.text(),
        #             'write_file_padding': self.write_file_padding_slider.text(),
        #             'write_file_frame_index': self.write_file_frame_index_push_btn.text(),
        #             'write_file_version_name': self.write_file_version_name_lineedit.text(),
        #         })

        #         self.setup_window.close()

        # def write_file_create_open_clip_btn_check():
        #     if self.write_file_create_open_clip_btn.isChecked():
        #         self.write_file_create_open_clip_lineedit.setDisabled(False)
        #         self.write_file_open_clip_token_btn.setDisabled(False)
        #     else:
        #         self.write_file_create_open_clip_lineedit.setDisabled(True)
        #         self.write_file_open_clip_token_btn.setDisabled(True)

        # def write_file_include_setup_btn_check():
        #     if self.write_file_include_setup_btn.isChecked():
        #         self.write_file_include_setup_lineedit.setDisabled(False)
        #         self.write_file_include_setup_token_btn.setDisabled(False)
        #     else:
        #         self.write_file_include_setup_lineedit.setDisabled(True)
        #         self.write_file_include_setup_token_btn.setDisabled(True)

        # def render_node_type_toggle():

        #     if self.write_file_render_node_type_push_btn.text() == 'Render Node':
        #         self.write_file_setup_label.setDisabled(True)
        #         self.write_file_media_path_label.setDisabled(True)
        #         self.write_file_pattern_label.setDisabled(True)
        #         self.write_file_type_label.setDisabled(True)
        #         self.write_file_frame_index_label.setDisabled(True)
        #         self.write_file_padding_label.setDisabled(True)
        #         self.write_file_compression_label.setDisabled(True)
        #         self.write_file_settings_label.setDisabled(True)
        #         self.write_file_version_name_label.setDisabled(True)
        #         self.write_file_media_path_lineedit.setDisabled(True)
        #         self.write_file_pattern_lineedit.setDisabled(True)
        #         self.write_file_create_open_clip_lineedit.setDisabled(True)
        #         self.write_file_include_setup_lineedit.setDisabled(True)
        #         self.write_file_version_name_lineedit.setDisabled(True)
        #         self.write_file_padding_slider.setDisabled(True)
        #         self.write_file_image_format_push_btn.setDisabled(True)
        #         self.write_file_compression_push_btn.setDisabled(True)
        #         self.write_file_frame_index_push_btn.setDisabled(True)
        #         self.write_file_pattern_token_btn.setDisabled(True)
        #         self.write_file_browse_btn.setDisabled(True)
        #         self.write_file_include_setup_btn.setDisabled(True)
        #         self.write_file_create_open_clip_btn.setDisabled(True)
        #         self.write_file_open_clip_token_btn.setDisabled(True)
        #         self.write_file_include_setup_token_btn.setDisabled(True)
        #     else:
        #         self.write_file_setup_label.setDisabled(False)
        #         self.write_file_media_path_label.setDisabled(False)
        #         self.write_file_pattern_label.setDisabled(False)
        #         self.write_file_type_label.setDisabled(False)
        #         self.write_file_frame_index_label.setDisabled(False)
        #         self.write_file_padding_label.setDisabled(False)
        #         self.write_file_compression_label.setDisabled(False)
        #         self.write_file_settings_label.setDisabled(False)
        #         self.write_file_version_name_label.setDisabled(False)
        #         self.write_file_media_path_lineedit.setDisabled(False)
        #         self.write_file_pattern_lineedit.setDisabled(False)
        #         self.write_file_create_open_clip_lineedit.setDisabled(False)
        #         self.write_file_include_setup_lineedit.setDisabled(False)
        #         self.write_file_version_name_lineedit.setDisabled(False)
        #         self.write_file_padding_slider.setDisabled(False)
        #         self.write_file_image_format_push_btn.setDisabled(False)
        #         self.write_file_compression_push_btn.setDisabled(False)
        #         self.write_file_frame_index_push_btn.setDisabled(False)
        #         self.write_file_pattern_token_btn.setDisabled(False)
        #         self.write_file_browse_btn.setDisabled(False)
        #         self.write_file_include_setup_btn.setDisabled(False)
        #         self.write_file_create_open_clip_btn.setDisabled(False)
        #         self.write_file_open_clip_token_btn.setDisabled(False)
        #         self.write_file_include_setup_token_btn.setDisabled(False)

        #         write_file_create_open_clip_btn_check()

        #         write_file_include_setup_btn_check()

        # def media_path_browse():

        #     file_path = pyside6_qt_file_browser('Select Directory', [''], self.write_file_media_path_lineedit.text(), select_directory=True, window_to_hide=[self.setup_window])

        #     if file_path:
        #         self.write_file_media_path_lineedit.setText(file_path)

        gridbox = QtWidgets.QGridLayout()
        self.setup_window = pyside6_qt_window(f'{SCRIPT_NAME}: Render/Write Node Setup <small>{VERSION}', gridbox, 1000, 570)

        # Labels

        self.write_file_render_node_type_label = pyside6_qt_label('Render Node Type')
        self.write_file_setup_label = pyside6_qt_label('Write File Node Setup', label_type='underline')
        self.write_file_media_path_label = pyside6_qt_label('Media Path')
        self.write_file_pattern_label = pyside6_qt_label('Pattern')
        self.write_file_type_label = pyside6_qt_label('File Type')
        self.write_file_frame_index_label = pyside6_qt_label('Frame Index')
        self.write_file_padding_label = pyside6_qt_label('Padding')
        self.write_file_compression_label = pyside6_qt_label('Compression')
        self.write_file_settings_label = pyside6_qt_label('Settings', label_type='underline')
        self.write_file_version_name_label = pyside6_qt_label('Version Name')

        # LineEdits

        self.write_file_media_path_lineedit = pyside6_qt_line_edit(self.settings.write_file_media_path)
        self.write_file_pattern_lineedit = pyside6_qt_line_edit(self.settings.write_file_pattern)
        self.write_file_create_open_clip_lineedit = pyside6_qt_line_edit(self.settings.write_file_create_open_clip_value)
        self.write_file_include_setup_lineedit = pyside6_qt_line_edit(self.settings.write_file_include_setup_value)
        self.write_file_version_name_lineedit = pyside6_qt_line_edit(self.settings.write_file_version_name, max_width=150)

        # Sliders

        self.write_file_padding_slider = pyside6_qt_slider(int(self.settings.write_file_padding), 1, 20, value_is_float=False, slider_width=150)

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

        # def compression(file_format):

        #     def create_menu(option):
        #         self.write_file_compression_push_btn.setText(option)

        #     compression_menu.clear()

        #     self.write_file_image_format_push_btn.setText(file_format)

        #     if 'Dpx' in file_format:
        #         self.write_file_compression_push_btn.setText('Uncompressed')
        #         compression_list = ['Uncompressed', 'Pixspan', 'Packed']
        #         self.write_file_compression_push_btn.setEnabled(True)

        #     elif 'Jpeg' in file_format:
        #         self.write_file_compression_push_btn.setText('')
        #         compression_list = []
        #         self.write_file_compression_push_btn.setEnabled(False)

        #     elif 'OpenEXR' in file_format:
        #         # self.write_file_compression_push_btn.setText('Uncompressed')
        #         self.write_file_compression_push_btn.setText('PIZ')
        #         compression_list = ['Uncompressed', 'Scanline', 'Multi_Scanline', 'RLE', 'PXR24', 'PIZ', 'DWAB', 'DWAA', 'B44A', 'B44']
        #         self.write_file_compression_push_btn.setEnabled(True)

        #     elif 'Png' in file_format:
        #         self.write_file_compression_push_btn.setText('')
        #         compression_list = []
        #         self.write_file_compression_push_btn.setEnabled(False)

        #     elif 'Sgi' in file_format:
        #         self.write_file_compression_push_btn.setText('Uncompressed')
        #         compression_list = ['Uncompressed', 'RLE']
        #         self.write_file_compression_push_btn.setEnabled(True)

        #     elif 'Targa' in file_format:
        #         self.write_file_compression_push_btn.setText('')
        #         compression_list = []
        #         self.write_file_compression_push_btn.setEnabled(False)

        #     elif 'Tiff' in file_format:
        #         self.write_file_compression_push_btn.setText('Uncompressed')
        #         compression_list = ['Uncompressed', 'RLE', 'LZW']
        #         self.write_file_compression_push_btn.setEnabled(True)

        #     for option in compression_list:
        #         compression_menu.addAction(option, partial(create_menu, option))

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
        self.write_file_render_node_type_push_btn = pyside6_qt_push_button_menu(self.settings.render_node_type, render_node_options, menu_action=render_node_type_toggle)

        # Frame Index Pushbutton Menu

        frame_index = ['Use Start Frame', 'Use Timecode']
        self.write_file_frame_index_push_btn = pyside6_qt_push_button_menu(self.settings.write_file_frame_index, frame_index)

        # Token Push Buttons

        write_file_token_dict = {'Batch Name': '<batch name>', 'Batch Iteration': '<batch iteration>', 'Iteration': '<iteration>',
                                'Project': '<project>', 'Project Nickname': '<project nickname>', 'Shot Name': '<shot name>', 'Clip Height': '<height>',
                                'Clip Width': '<width>', 'Clip Name': '<name>', }

        self.write_file_pattern_token_btn = pyside6_qt_token_push_button('Add Token', write_file_token_dict, self.write_file_pattern_lineedit)
        self.write_file_open_clip_token_btn = pyside6_qt_token_push_button('Add Token', write_file_token_dict, self.write_file_create_open_clip_lineedit)
        self.write_file_include_setup_token_btn = pyside6_qt_token_push_button('Add Token', write_file_token_dict, self.write_file_include_setup_lineedit)

        # Pushbuttons

        self.write_file_create_open_clip_btn = pyside6_qt_push_button('Create Open Clip', self.settings.write_file_create_open_clip)
        self.write_file_create_open_clip_btn.clicked.connect(write_file_create_open_clip_btn_check)
        write_file_create_open_clip_btn_check()

        self.write_file_include_setup_btn = pyside6_qt_push_button('Include Setup', self.settings.write_file_include_setup)
        self.write_file_include_setup_btn.clicked.connect(write_file_include_setup_btn_check)
        write_file_include_setup_btn_check()

        # Buttons

        self.write_file_browse_btn = pyside6_qt_button('Browse', media_path_browse)
        self.write_file_save_btn = pyside6_qt_button('Save', save_config)
        self.write_file_cancel_btn = pyside6_qt_button('Cancel', self.setup_window.close)

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
