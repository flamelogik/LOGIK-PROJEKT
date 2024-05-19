# Function:         compression

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
