#

# -------------------------------------------------------------------------- #

# File Name:        pyside6_qt_print.py
# Version:          1.1.0
# Created:          2024-01-19
# Modified:         2025-11-14

# ========================================================================== #
# Imports
# ========================================================================== #

from typing import Optional

# ========================================================================== #
# Function Definition
# ========================================================================== #

def pyside6_qt_print(
        script_name: str,
        message: str,
        message_type: Optional[str]='message',
        time: Optional[int]=3
    ) -> None:
    '''
    Print message to terminal. If using Flame 2023.1 or later also prints to the Flame message window

    script_name: Name of script [str]
    message: Message to print. Warning message will print red, Error message will print yellow. [str]
    message_type: Type of message (message, error, warning) [str]
    time: Amount of time to display message for [int]

    Example:

        pyside6_qt_print('Script Name', 'Config not found.', message_type='error')
    '''

    import flame

    # Check argument values

    if not isinstance(script_name, str):
        raise TypeError('Pyflame Print: script_name must be a string')
    if not isinstance(message, str):
        raise TypeError('Pyflame Print: message must be a string')
    if message_type not in ['message', 'error', 'warning']:
        raise ValueError('Pyflame Print: message Type must be one of: message, error, warning')
    if not isinstance(time, int):
        raise TypeError('Pyflame Print: time must be an integer')

    # Print to terminal/shell

    if message_type == 'warning':
        # print message text in red
        print(f'\033[91m--> {message}\033[0m\n')
    elif message_type == 'error':
        # print message text in yellow
        print(f'\033[93m--> {message}\033[0m\n')
    else:
        print(f'--> {message}\n')

    # Print to Flame Message Window - Flame 2023.1 and later
    # Warning and error intentionally swapped to match color of message window

    script_name = script_name.upper()

    try:
        if message_type == 'message' or message_type == 'confirm':
            flame.messages.show_in_console(f'{script_name}: {message}', 'info', time)
        elif message_type == 'error':
            flame.messages.show_in_console(f'{script_name}: {message}', 'warning', time)
        elif message_type == 'warning':
            flame.messages.show_in_console(f'{script_name}: {message}', 'error', time)
    except:
        pass

# -------------------------------------------------------------------------- #
# Changelist
# -------------------------------------------------------------------------- #

# version:               1.1.0
# modified:              2025-11-14
# comments:              Refactored imports - removed unnecessary imports
# -------------------------------------------------------------------------- #
# version:               1.0.3
# modified:              2025-02-25 - 07:01:21
# comments:              Added legacy support for PySide2 imports
# -------------------------------------------------------------------------- #
# version:               1.0.2
# modified:              2025-01-19 - 17:47:48
# comments:              Changed import statements to fix shell errors.
# -------------------------------------------------------------------------- #
# version:               1.0.1
# modified:              2024-11-16 - 16:52:07
# comments:              Fixed circular import statements
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-10-30 - 07:35:27
# comments:              Refactored PySide6 Output Node Config UI.
# -------------------------------------------------------------------------- #