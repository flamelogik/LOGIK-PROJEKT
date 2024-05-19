# filename: FlameMessageWindow.py

from PySide6 import QtWidgets, QtCore, QtGui
import xml.etree.ElementTree as ET
from typing import Union, List, Dict, Optional, Callable
import os, re, datetime, shutil, ast

class FlameMessageWindow(QtWidgets.QDialog):
    '''
    Custom Qt Flame Message Window

    FlameMessageWindow(message_type, message_title, message[, time=3, parent=None])

    message_type: Type of message window to be shown. Options are: confirm, message, error, warning [str] Confirm and warning return True or False values
    message_title: Text shown in top left of window ie. Confirm Operation [str]
    message: Text displayed in body of window [str]
    time: (optional) Time in seconds to display message in flame message area. Default is 3. [int]
    parent: (optional) - Parent window [QtWidget]

    Message Window Types:

        confirm: confirm and cancel button / grey left bar - returns True or False
        message: ok button / blue left bar
        error: ok button / yellow left bar
        warning: confirm and cancel button / red left bar - returns True of False

    Examples:

        FlameMessageWindow('error', f'{SCRIPT_NAME}: Error', f'Unable to create folder.<br>Check folder permissions')

        or

        if FlameMessageWindow('confirm', 'Confirm Operation', 'Some important message'):
            do something
    '''

    def __init__(self, message_type: str, message_title: str, message: str, time: int = 3, parent=None):
        super(FlameMessageWindow, self).__init__()

        # Check argument types
        valid_message_types = ['confirm', 'message', 'error', 'warning']
        if message_type not in valid_message_types:
            raise ValueError(f"FlameMessageWindow: message_type must be one of: {', '.join(valid_message_types)}")
        if not isinstance(message_title, str):
            raise TypeError('FlameMessageWindow: message_title must be a string.')
        if not isinstance(message, str):
            raise TypeError('FlameMessageWindow: message must be a string.')
        if not isinstance(time, int):
            raise TypeError('FlameMessageWindow: time must be an integer.')

        # Create message window
        self.message_type = message_type
        self.confirmed = False  # Initialize confirmed attribute

        # Rest of your __init__ method...

        self.ok_button = FlameButton('Ok', self.confirm, button_color='blue', button_width=110)
        self.confirm_button = FlameButton('Confirm', self.confirm, button_color='blue', button_width=110)
        self.cancel_button = FlameButton('Cancel', self.cancel, button_width=110)

        # Rest of your __init__ method...

    # Other methods...

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        colors = {
            'confirm': QtGui.QColor(71, 71, 71),
            'message': QtGui.QColor(0, 110, 176),
            'error': QtGui.QColor(251, 181, 73),
            'warning': QtGui.QColor(200, 29, 29)
        }

        line_color = colors.get(self.message_type, QtGui.QColor(71, 71, 71))

        # Draw lines with painter...
