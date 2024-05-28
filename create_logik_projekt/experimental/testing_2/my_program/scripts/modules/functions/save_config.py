# Function:         save_config

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
        pyside6_qt_save_config(SCRIPT_NAME, SCRIPT_PATH, {
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
