def write_node_setup(self):

    def save_config():
        if not self.write_file_media_path_lineedit.text():
            pyside6_qt_message_window('error', f'{SCRIPT_NAME}: Error', 'Write Node Setup: Enter Media Path.')
        elif not self.write_file_pattern_lineedit.text():
            pyside6_qt_message_window('error', f'{SCRIPT_NAME}: Error', 'Write Node Setup: Enter Pattern for image files.')
        elif not self.write_file_create_open_clip_lineedit.text():
            pyside6_qt_message_window('error', f'{SCRIPT_NAME}: Error', 'Write Node Setup: Enter Create Open Clip Naming.')
        elif not self.write_file_include_setup_lineedit.text():
            pyside6_qt_message_window('error', f'{SCRIPT_NAME}: Error', 'Write Node Setup: Enter Include Setup Naming.')
        elif not self.write_file_version_name_lineedit.text():
            pyside6_qt_message_window('error', f'{SCRIPT_NAME}: Error', 'Write Node Setup: Enter Version Naming.')
        else:
            pyside6_qt_save_config(SCRIPT_NAME, CONFIG_PATH, {
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
            for widget in self.write_file_widgets:
                widget.setDisabled(True)
        else:
            for widget in self.write_file_widgets:
                widget.setDisabled(False)
            write_file_create_open_clip_btn_check()
            write_file_include_setup_btn_check()

    def media_path_browse():
        file_path = pyside6_qt_file_browser('Select Directory', [''], self.write_file_media_path_lineedit.text(), select_directory=True, window_to_hide=[self.setup_window])
        if file_path:
            self.write_file_media_path_lineedit.setText(file_path)

    # Layout setup
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
    image_format_menu.setStyleSheet('QMenu {color: #9a9a9a; background-color:#2d3744; border: none; font: 14px "Discreet"} QMenu::item:selected {color: #d9d9d9; background-color: #3a4551}')

    self.write_file_image_format_push_btn = QtWidgets.QPushButton(self.settings.write_file_image_format)
    self.write_file_image_format_push_btn.setMenu(image_format_menu)
    self.write_file_image_format_push_btn.setMinimumSize(QtCore.QSize(150, 28))
    self.write_file_image_format_push_btn.setMaximumSize(QtCore.QSize(150, 28))
    self.write_file_image_format_push_btn.setFocusPolicy(QtCore.Qt.NoFocus)
    self.write_file_image_format_push_btn.setStyleSheet('QPushButton {color: #9a9a9a; background-color: #2d3744; border: none; font: 14px "Discreet"} QPushButton:hover {border: 1px solid #5a5a5a} QPushButton:disabled {color: #747474; background-color: #2d3744; border: none} QPushButton::menu-indicator { image: none; }')

    # Compression Menu
    compression_menu = QtWidgets.QMenu(self.setup_window)
    compression_menu.setStyleSheet('QMenu {color: #9a9a9a; background-color:#2d3744; border: none; font: 14px "Discreet"} QMenu::item:selected {color: #d9d9d9; background-color: #3a4551}')

    self.write_file_compression_push_btn = QtWidgets.QPushButton(self.settings.write_file_compression)
    self.write_file_compression_push_btn.setMenu(compression_menu)
    self.write_file_compression_push_btn.setMinimumSize(QtCore.QSize(150, 28))
    self.write_file_compression_push_btn.setMaximumSize(QtCore.QSize(150, 28))
    self.write_file_compression_push_btn.setFocusPolicy(QtCore.Qt.NoFocus)
    self.write_file_compression_push_btn.setStyleSheet('QPushButton {color: #9a9a9a; background-color: #2d3744; border: none; font: 14px "Discreet"} QPushButton:hover {border: 1px solid #5a5a5a} QPushButton:disabled {color: #747474; background-color: #2d3744; border: none} QPushButton::menu-indicator { image: none; }')
    self.write_file_compression_push_btn.setText(self.settings.write_file_compression)

    def compression(file_format):
        def create_menu(option):
            self.write_file_compression_push_btn.setText(option)

        compression_menu.clear()
        self.write_file_image_format_push_btn.setText(file_format)
        if file_format == 'Exr':
            compression_options = ['None', 'PIZ', 'ZIP', 'RLE', 'ZIPS', 'B44', 'B44A', 'DWAA', 'DWAB']
        elif file_format == 'Dpx':
            compression_options = ['None']
        elif file_format == 'Jpg':
            compression_options = ['None']
        elif file_format == 'Tiff':
            compression_options = ['None', 'PackBits', 'LZW', 'Deflate']
        elif file_format == 'Tga':
            compression_options = ['None']
        else:
            compression_options = []

        for option in compression_options:
            compression_menu.addAction(option, partial(create_menu, option))

    for format_option in ['Exr', 'Dpx', 'Jpg', 'Tiff', 'Tga']:
        image_format_menu.addAction(format_option, partial(compression, format_option))

    # Render Node / Write File Node Button
    render_node_type_menu = QtWidgets.QMenu(self.setup_window)
    render_node_type_menu.setStyleSheet('QMenu {color: #9a9a9a; background-color:#2d3744; border: none; font: 14px "Discreet"} QMenu::item:selected {color: #d9d9d9; background-color: #3a4551}')

    self.write_file_render_node_type_push_btn = QtWidgets.QPushButton(self.settings.render_node_type)
    self.write_file_render_node_type_push_btn.setMenu(render_node_type_menu)
    self.write_file_render_node_type_push_btn.setMinimumSize(QtCore.QSize(200, 28))
    self.write_file_render_node_type_push_btn.setMaximumSize(QtCore.QSize(200, 28))
    self.write_file_render_node_type_push_btn.setFocusPolicy(QtCore.Qt.NoFocus)
    self.write_file_render_node_type_push_btn.setStyleSheet('QPushButton {color: #9a9a9a; background-color: #2d3744; border: none; font: 14px "Discreet"} QPushButton:hover {border: 1px solid #5a5a5a} QPushButton:disabled {color: #747474; background-color: #2d3744; border: none} QPushButton::menu-indicator { image: none; }')

    render_node_type_menu.addAction('Render Node', lambda: self.write_file_render_node_type_push_btn.setText('Render Node'))
    render_node_type_menu.addAction('Write File Node', lambda: self.write_file_render_node_type_push_btn.setText('Write File Node'))

    # Frame Index Menu
    frame_index_menu = QtWidgets.QMenu(self.setup_window)
    frame_index_menu.setStyleSheet('QMenu {color: #9a9a9a; background-color:#2d3744; border: none; font: 14px "Discreet"} QMenu::item:selected {color: #d9d9d9; background-color: #3a4551}')

    self.write_file_frame_index_push_btn = QtWidgets.QPushButton(self.settings.write_file_frame_index)
    self.write_file_frame_index_push_btn.setMenu(frame_index_menu)
    self.write_file_frame_index_push_btn.setMinimumSize(QtCore.QSize(200, 28))
    self.write_file_frame_index_push_btn.setMaximumSize(QtCore.QSize(200, 28))
    self.write_file_frame_index_push_btn.setFocusPolicy(QtCore.Qt.NoFocus)
    self.write_file_frame_index_push_btn.setStyleSheet('QPushButton {color: #9a9a9a; background-color: #2d3744; border: none; font: 14px "Discreet"} QPushButton:hover {border: 1px solid #5a5a5a} QPushButton:disabled {color: #747474; background-color: #2d3744; border: none} QPushButton::menu-indicator { image: none; }')

    for frame_index_option in ['Start Frame', 'Timeline Frame', 'Segment Frame']:
        frame_index_menu.addAction(frame_index_option, lambda fi=frame_index_option: self.write_file_frame_index_push_btn.setText(fi))

    # Checkboxes
    self.write_file_create_open_clip_btn = pyside6_qt_push_btn('Create Open Clip')
    self.write_file_create_open_clip_btn.setCheckable(True)
    self.write_file_create_open_clip_btn.setMinimumSize(QtCore.QSize(200, 28))
    self.write_file_create_open_clip_btn.setMaximumSize(QtCore.QSize(200, 28))
    self.write_file_create_open_clip_btn.setFocusPolicy(QtCore.Qt.NoFocus)
    self.write_file_create_open_clip_btn.setStyleSheet('QPushButton {color: #9a9a9a; background-color: #2d3744; border: none; font: 14px "Discreet"} QPushButton:hover {border: 1px solid #5a5a5a} QPushButton:disabled {color: #747474; background-color: #2d3744; border: none} QPushButton:checked {color: orange;}')
    self.write_file_create_open_clip_btn.setChecked(eval(self.settings.write_file_create_open_clip))

    self.write_file_include_setup_btn = pyside6_qt_push_btn('Include Setup')
    self.write_file_include_setup_btn.setCheckable(True)
    self.write_file_include_setup_btn.setMinimumSize(QtCore.QSize(200, 28))
    self.write_file_include_setup_btn.setMaximumSize(QtCore.QSize(200, 28))
    self.write_file_include_setup_btn.setFocusPolicy(QtCore.Qt.NoFocus)
    self.write_file_include_setup_btn.setStyleSheet('QPushButton {color: #9a9a9a; background-color: #2d3744; border: none; font: 14px "Discreet"} QPushButton:hover {border: 1px solid #5a5a5a} QPushButton:disabled {color: #747474; background-color: #2d3744; border: none} QPushButton:checked {color: orange;}')
    self.write_file_include_setup_btn.setChecked(eval(self.settings.write_file_include_setup))

    # Token Push Buttons
    self.write_file_token_btn = pyside6_qt_push_btn('Add Token...', token=True)
    self.write_file_open_clip_token_btn = pyside6_qt_push_btn('Add Token...', token=True)
    self.write_file_include_setup_token_btn = pyside6_qt_push_btn('Add Token...', token=True)

    # Buttons
    self.write_file_media_path_browse_btn = pyside6_qt_push_btn('Browse...', browse=True)
    self.write_file_save_btn = pyside6_qt_push_btn('Save')
    self.write_file_cancel_btn = pyside6_qt_push_btn('Cancel')

    # Set Disabled widgets
    self.write_file_widgets = [
        self.write_file_media_path_lineedit,
        self.write_file_media_path_browse_btn,
        self.write_file_pattern_lineedit,
        self.write_file_create_open_clip_lineedit,
        self.write_file_create_open_clip_btn,
        self.write_file_include_setup_lineedit,
        self.write_file_include_setup_btn,
        self.write_file_image_format_push_btn,
        self.write_file_compression_push_btn,
        self.write_file_padding_slider,
        self.write_file_frame_index_push_btn,
        self.write_file_version_name_lineedit,
        self.write_file_token_btn,
        self.write_file_open_clip_token_btn,
        self.write_file_include_setup_token_btn
    ]

    render_node_type_toggle()

    self.write_file_create_open_clip_btn.clicked.connect(write_file_create_open_clip_btn_check)
    self.write_file_include_setup_btn.clicked.connect(write_file_include_setup_btn_check)
    self.write_file_render_node_type_push_btn.clicked.connect(render_node_type_toggle)
    self.write_file_media_path_browse_btn.clicked.connect(media_path_browse)
    self.write_file_save_btn.clicked.connect(save_config)
    self.write_file_cancel_btn.clicked.connect(self.setup_window.close)

    # Gridbox Layout
    gridbox.addWidget(self.write_file_render_node_type_label, 1, 0, QtCore.Qt.AlignRight)
    gridbox.addWidget(self.write_file_render_node_type_push_btn, 1, 1, QtCore.Qt.AlignLeft)
    gridbox.addWidget(self.write_file_setup_label, 2, 0, 1, 2, QtCore.Qt.AlignCenter)
    gridbox.addWidget(self.write_file_media_path_label, 3, 0, QtCore.Qt.AlignRight)
    gridbox.addWidget(self.write_file_media_path_lineedit, 3, 1, QtCore.Qt.AlignLeft)
    gridbox.addWidget(self.write_file_media_path_browse_btn, 3, 2, QtCore.Qt.AlignLeft)
    gridbox.addWidget(self.write_file_pattern_label, 4, 0, QtCore.Qt.AlignRight)
    gridbox.addWidget(self.write_file_pattern_lineedit, 4, 1, QtCore.Qt.AlignLeft)
    gridbox.addWidget(self.write_file_token_btn, 4, 2, QtCore.Qt.AlignLeft)
    gridbox.addWidget(self.write_file_type_label, 5, 0, QtCore.Qt.AlignRight)
    gridbox.addWidget(self.write_file_image_format_push_btn, 5, 1, QtCore.Qt.AlignLeft)
    gridbox.addWidget(self.write_file_compression_label, 5, 2, QtCore.Qt.AlignRight)
    gridbox.addWidget(self.write_file_compression_push_btn, 5, 3, QtCore.Qt.AlignLeft)
    gridbox.addWidget(self.write_file_frame_index_label, 6, 0, QtCore.Qt.AlignRight)
    gridbox.addWidget(self.write_file_frame_index_push_btn, 6, 1, QtCore.Qt.AlignLeft)
    gridbox.addWidget(self.write_file_padding_label, 7, 0, QtCore.Qt.AlignRight)
    gridbox.addWidget(self.write_file_padding_slider, 7, 1, 1, 2, QtCore.Qt.AlignLeft)
    gridbox.addWidget(self.write_file_create_open_clip_label, 8, 0, QtCore.Qt.AlignRight)
    gridbox.addWidget(self.write_file_create_open_clip_lineedit, 8, 1, QtCore.Qt.AlignLeft)
    gridbox.addWidget(self.write_file_create_open_clip_btn, 8, 2, QtCore.Qt.AlignLeft)
    gridbox.addWidget(self.write_file_open_clip_token_btn, 8, 3, QtCore.Qt.AlignLeft)
    gridbox.addWidget(self.write_file_include_setup_label, 9, 0, QtCore.Qt.AlignRight)
    gridbox.addWidget(self.write_file_include_setup_lineedit, 9, 1, QtCore.Qt.AlignLeft)
    gridbox.addWidget(self.write_file_include_setup_btn, 9, 2, QtCore.Qt.AlignLeft)
    gridbox.addWidget(self.write_file_include_setup_token_btn, 9, 3, QtCore.Qt.AlignLeft)
    gridbox.addWidget(self.write_file_version_name_label, 10, 0, QtCore.Qt.AlignRight)
    gridbox.addWidget(self.write_file_version_name_lineedit, 10, 1, QtCore.Qt.AlignLeft)
    gridbox.addWidget(self.write_file_btn_hbox, 11, 0, 1, 4, QtCore.Qt.AlignCenter)

    gridbox.setColumnMinimumWidth(1, 100)
    gridbox.setColumnMinimumWidth(2, 200)
    gridbox.setColumnStretch(1, 2)
    gridbox.setColumnStretch(2, 2)

    self.write_file_window.setLayout(gridbox)

    # Center Window
    center_window(self.write_file_window)

    self.write_file_window.show()

    # Refresh Write File Menu
    refresh_write_file()

# Write File Menu
write_file_menu()
