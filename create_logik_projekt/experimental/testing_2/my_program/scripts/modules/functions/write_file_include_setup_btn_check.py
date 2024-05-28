# Function:         write_file_include_setup_btn_check

def write_file_include_setup_btn_check():
        if self.write_file_include_setup_btn.isChecked():
        self.write_file_include_setup_lineedit.setDisabled(False)
        self.write_file_include_setup_token_btn.setDisabled(False)
        else:
        self.write_file_include_setup_lineedit.setDisabled(True)
        self.write_file_include_setup_token_btn.setDisabled(True)
