# Function:         media_path_browse

def media_path_browse():

        file_path = pyside6_qt_file_browser('Select Directory', [''], self.write_file_media_path_lineedit.text(), select_directory=True, window_to_hide=[self.setup_window])

        if file_path:
        self.write_file_media_path_lineedit.setText(file_path)
