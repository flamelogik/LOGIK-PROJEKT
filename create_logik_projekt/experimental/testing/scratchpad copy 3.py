# filename: FlameTextEdit

from PySide6 import QtWidgets, QtCore, QtGui
import xml.etree.ElementTree as ET
from typing import Union, List, Dict, Optional, Callable
import os, re, datetime, shutil, ast

class FlameTextEdit(QtWidgets.QPlainTextEdit):
    '''
    Custom Qt Flame Text Edit Widget

    FlameTextEdit(text[, read_only=False])

    text: text to be displayed [str]
    read_only: (optional) make text in window read only [bool] - default is False

    Example:

        text_edit = FlameTextEdit('Some important text here', read_only=True)
    '''

    def __init__(self, text: str, read_only: Optional[bool]=False):
        super(FlameTextEdit, self).__init__()

        # Check argument types

        if not isinstance(text, str):
            raise TypeError('FlameTextEdit: text must be a string.')
        if not isinstance(read_only, bool):
            raise TypeError('FlameTextEdit: read_only must be a boolean.')

        # Build text edit

        self.setMinimumHeight(50)
        self.setMinimumWidth(150)
        self.setText(text)
        self.setReadOnly(read_only)
        self.setFocusPolicy(QtCore.Qt.ClickFocus)

        style_sheet = '''
            QTextEdit {
                color: rgb(154, 154, 154);
                background-color: #37414b;
                selection-color: #262626;
                selection-background-color: #b8b1a7;
                border: none;
                padding-left: 5px;
                font: 14px "Discreet";
            }
            QScrollBar {
                color: 111111;
                background: rgb(49, 49, 49);
            }
            QScrollBar::handle {
                color: 111111;
                background : 111111;
            }
            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical,
            QScrollBar::add-line:horizontal,
            QScrollBar::sub-line:horizontal {
                border: none;
                background: none;
                width: 0px;
                height: 0px;
            }
        '''

        if read_only:
            style_sheet += '''
                QTextEdit:focus {
                    background-color: #495663;
                }
            '''
        self.setStyleSheet(style_sheet)
