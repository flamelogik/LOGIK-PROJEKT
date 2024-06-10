class LogikProjektMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_projekt_UI()

    def init_projekt_UI(self):
        self.setWindowTitle("LOGIK-PROJEKT Creator")
        self.setGeometry(0, 0, 1024, 960)
        self.center()
        
        self.setStyleSheet("background-color: #333333;")
        
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        self.projekt_serial_number = self.create_labeled_entry(layout, "Projekt Serial Number")
        self.add_separator_line(layout)

        self.projekt_client_name = self.create_labeled_entry(layout, "Projekt Client Name")
        self.add_separator_line(layout)

        self.projekt_campaign_name = self.create_labeled_entry(layout, "Projekt Campaign Name")
        self.add_separator_line(layout)

        self.projekt_resolution_label = QLabel('Projekt Resolution:')
        self.projekt_resolution_label.setStyleSheet("color: white; font-family: 'Courier New';")
        layout.addWidget(self.projekt_resolution_label)

        self.projekt_resolution = QComboBox()
        self.projekt_resolution.setStyleSheet(self.get_combobox_stylesheet())
        layout.addWidget(self.projekt_resolution)
        self.add_separator_line(layout)

        self.projekt_bit_depth_label = QLabel('Projekt Bit Depth:')
        self.projekt_bit_depth_label.setStyleSheet("color: white; font-family: 'Courier New';")
        layout.addWidget(self.projekt_bit_depth_label)

        self.projekt_bit_depth = QComboBox()
        self.projekt_bit_depth.setStyleSheet(self.get_combobox_stylesheet())
        layout.addWidget(self.projekt_bit_depth)
        self.add_separator_line(layout)

        self.projekt_frame_rate_label = QLabel('Projekt Frame Rate:')
        self.projekt_frame_rate_label.setStyleSheet("color: white; font-family: 'Courier New';")
        layout.addWidget(self.projekt_frame_rate_label)

        self.projekt_frame_rate = QComboBox()
        self.projekt_frame_rate.setStyleSheet(self.get_combobox_stylesheet())
        layout.addWidget(self.projekt_frame_rate)
        self.add_separator_line(layout)

        self.projekt_color_science_label = QLabel('Projekt Color Science:')
        self.projekt_color_science_label.setStyleSheet("color: white; font-family: 'Courier New';")
        layout.addWidget(self.projekt_color_science_label)

        self.projekt_color_science = QComboBox()
        self.projekt_color_science.setStyleSheet(self.get_combobox_stylesheet())
        layout.addWidget(self.projekt_color_science)
        self.add_separator_line(layout)

        self.projekt_start_frame_label = QLabel('Projekt Start Frame:')
        self.projekt_start_frame_label.setStyleSheet("color: white; font-family: 'Courier New';")
        layout.addWidget(self.projekt_start_frame_label)

        self.projekt_start_frame = QComboBox()
        self.projekt_start_frame.setStyleSheet(self.get_combobox_stylesheet())
        layout.addWidget(self.projekt_start_frame)
        self.add_separator_line(layout)

        summary_label = QLabel("LOGIK-PROJEKT Summary")
        summary_label.setStyleSheet("color: white; font-family: 'Courier New', monospace; font-weight: bold;")
        layout.addWidget(summary_label)

        self.summary_text = QTextEdit()
        self.summary_text.setReadOnly(True)
        self.summary_text.setStyleSheet("""
            background-color: #111111;
            color: white;
            font-family: 'Courier New', monospace;
            font-weight: bold;
        """)
        layout.addWidget(self.summary_text)

        self.create_logik_projekt_button = self.create_button(layout, "Create LOGIK-PROJEKT", "#014400", self.create_logik_projekt)
        self.create_projekt_template_button = self.create_button(layout, "Create PROJEKT Template", "#864B00", self.create_projekt_template)
        self.cancel_button = self.create_button(layout, "Cancel", "#630000", self.cancel)

        self.projekt_serial_number.textChanged.connect(self.update_summary)
        self.projekt_client_name.textChanged.connect(self.update_summary)
        self.projekt_campaign_name.textChanged.connect(self.update_summary)
        self.projekt_resolution.currentTextChanged.connect(self.update_summary)
        self.projekt_bit_depth.currentTextChanged.connect(self.update_summary)
        self.projekt_frame_rate.currentTextChanged.connect(self.update_summary)
        self.projekt_color_science.currentTextChanged.connect(self.update_summary)
        self.projekt_start_frame.currentTextChanged.connect(self.update_summary)

        load_resolutions(self.projekt_resolution)
        load_bit_depths(self.projekt_bit_depth)
        load_frame_rates(self.projekt_frame_rate)
        load_color_sciences(self.projekt_color_science)
        load_start_frames(self.projekt_start_frame)

        self.projekt_resolution.currentIndexChanged.connect(self.update_summary)

        default_index = self.projekt_resolution.findText("1920 x 1080 | HD 1080 16:9")
        self.projekt_resolution.setCurrentIndex(default_index)
        self.update_summary()

        default_index = self.projekt_bit_depth.findText("16-bit fp")
        self.projekt_bit_depth.setCurrentIndex(default_index)
        self.update_summary()

        default_index = self.projekt_frame_rate.findText("23.976 fps")
        self.projekt_frame_rate.setCurrentIndex(default_index)
        self.update_summary()

        default_index = self.projekt_color_science.findText("Autodesk ACES 1.1")
        self.projekt_color_science.setCurrentIndex(default_index)
        self.update_summary()

        default_index = self.projekt_start_frame.findText("1001")
        self.projekt_start_frame.setCurrentIndex(default_index)
        self.update_summary()

        self.update_summary()

        # Environment Info label and text box
        self.env_info_label = QLabel("Environment Info:")
        self.environment_info = QTextEdit()
        self.environment_info.setReadOnly(True)
        layout.addWidget(self.env_info_label)
        layout.addWidget(self.environment_info)

        # Latest Flame Version label and text box
        self.latest_flame_version_label = QLabel("Latest Flame Version:")
        self.latest_flame_version_text = QTextEdit()
        self.latest_flame_version_text.setReadOnly(True)
        layout.addWidget(self.latest_flame_version_label)
        layout.addWidget(self.latest_flame_version_text)

        # Latest Sanitized Flame Version label and text box
        self.latest_sanitized_flame_version_label = QLabel("Latest Sanitized Flame Version:")
        self.latest_sanitized_flame_version_text = QTextEdit()
        self.latest_sanitized_flame_version_text.setReadOnly(True)
        layout.addWidget(self.latest_sanitized_flame_version_label)
        layout.addWidget(self.latest_sanitized_flame_version_text)

        # Populate the text boxes
        self.populate_text_boxes()

    def add_separator_line(self, layout):
        separator_line = QFrame()
        separator_line.setFrameShape(QFrame.HLine)
        separator_line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator_line)

    # Other methods such as create_labeled_entry, get_combobox_stylesheet, etc.
