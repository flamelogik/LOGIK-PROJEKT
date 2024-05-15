class FlamePushButton(QtWidgets.QPushButton):
    '''
    Custom Qt Flame Push Button Widget

    FlamePushButton(button_name, button_checked[, connect=None, button_width=150])

    button_name: text displayed on button [str]
    button_checked: True or False [bool]
    connect: (optional) execute when button is pressed [function]
    button_width: (optional) default is 150. [int]

    Example:

        pushbutton = FlamePushButton('Button Name', False)
    '''

    def __init__(
            self,
            button_name: str,
            button_checked: bool,
            connect: Optional[Callable[..., None]] = None,
            button_width: Optional[int] = 150
        ):
        super(FlamePushButton, self).__init__()

        # Check argument types

        if not isinstance(button_name, str):
            raise TypeError('FlamePushButton: button_name must be string.')
        if not isinstance(button_checked, bool):
            raise TypeError('FlamePushButton: button_checked must be bool.')
        if not isinstance(button_width, int):
            raise TypeError('FlamePushButton: button_width must be integer.')

        # Build push button

        self.setText(button_name)
        self.setCheckable(True)
        self.setChecked(button_checked)
        self.setMinimumSize(button_width, 28)
        self.setMaximumSize(button_width, 28)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clicked.connect(connect)
        self.setStyleSheet(
            'QPushButton {'
                'color: rgb(154, 154, 154); '
                'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, '
                    'stop: .93 rgb(58, 58, 58), '
                    'stop: .94 rgb(44, 54, 68)); '
                'text-align: left; '
                'border-top: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, '
                    'stop: .93 rgb(58, 58, 58), '
                    'stop: .94 rgb(44, 54, 68)); '
                'border-bottom: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, '
                    'stop: .93 rgb(58, 58, 58), '
                    'stop: .94 rgb(44, 54, 68)); '
                'border-left: 1px solid rgb(58, 58, 58); '
                'border-right: 1px solid rgb(44, 54, 68); '
                'padding-left: 5px; font: 14px "Discreet"'
            '}'
            'QPushButton:checked {'
                'color: rgb(217, 217, 217); '
                'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, '
                    'stop: .93 rgb(71, 71, 71), '
                    'stop: .94 rgb(50, 101, 173)); '
                'text-align: left; '
                'border-top: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, '
                    'stop: .93 rgb(71, 71, 71), '
                    'stop: .94 rgb(50, 101, 173)); '
                'border-bottom: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, '
                    'stop: .93 rgb(71, 71, 71), '
                    'stop: .94 rgb(50, 101, 173)); '
                'border-left: 1px solid rgb(71, 71, 71); '
                'border-right: 1px solid rgb(50, 101, 173); '
                'padding-left: 5px; font: italic'
            '}'
            'QPushButton:hover {border: 1px solid rgb(90, 90, 90)}'
            'QPushButton:disabled {'
                'color: #6a6a6a; '
                'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, '
                    'stop: .93 rgb(58, 58, 58), '
                    'stop: .94 rgb(50, 50, 50)); '
                'font: light; border: none'
            '}'
            'QToolTip {'
                'color: rgb(170, 170, 170); '
                'background-color: rgb(71, 71, 71); '
                'border: 10px solid rgb(71, 71, 71)'
            '}'
        )
