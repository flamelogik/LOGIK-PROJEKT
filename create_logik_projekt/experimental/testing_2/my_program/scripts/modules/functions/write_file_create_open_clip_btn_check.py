# Function:         write_file_create_open_clip_btn_check

def write_file_create_open_clip_btn_check():
        if self.write_file_create_open_clip_btn.isChecked():
        self.write_file_create_open_clip_lineedit.setDisabled(False)
        self.write_file_open_clip_token_btn.setDisabled(False)
        else:
        self.write_file_create_open_clip_lineedit.setDisabled(True)
        self.write_file_open_clip_token_btn.setDisabled(True)
