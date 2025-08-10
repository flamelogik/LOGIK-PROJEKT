# Static Analysis: `src/core/utils/threaded_logging_utils.py`

## Overview
The `threaded_logging_utils.py` module provides utilities for managing logging in a multi-threaded PySide6 application. It defines a custom `logging.Handler` that emits log messages as PySide6 signals, allowing log output from any thread to be safely displayed in the GUI.

## Dependencies
- **Python Standard Library**: `logging`
- **PySide6.QtCore**: `QObject`, `Signal`

## Class: `LogEmitter(QObject)`

### Purpose
To act as a `QObject` that can emit a signal containing a log message. This signal can then be connected to a slot in the GUI thread to update a display element (e.g., a `QTextEdit`).

### Signals
- `message_logged(str)`: Emitted when a log message is received, carrying the formatted log string.

## Class: `SignalHandler(logging.Handler)`

### Purpose
To bridge Python's standard `logging` module with PySide6's signal-slot mechanism. It's a custom logging handler that, instead of writing to a file or console, emits log records as signals via a `LogEmitter`.

### Initialization (`__init__`)
- Inherits from `logging.Handler`.
- Takes an `emitter` (an instance of `LogEmitter`) as an argument.
- Calls the superclass constructor (`super().__init__()`).
- Sets a `logging.Formatter` for itself, defining how log records should be formatted before being emitted.

### Methods

#### `emit(self, record)`
- **Purpose**: Processes a log `record` and emits it as a signal.
- **Arguments**: `record` (logging.LogRecord): The log record to be handled.
- **Logic**:
    - Formats the `record` into a string message using its configured formatter (`self.format(record)`).
    - Emits the formatted `message` via the `self.emitter.message_logged` signal.

## Observations
- This module is crucial for building responsive PySide6 applications that perform long-running operations in background threads. It solves the common problem of safely updating the GUI with log messages from non-GUI threads.
- The `LogEmitter` acts as a simple `QObject` that can be moved to the GUI thread, ensuring that the signal emission happens in the correct thread context.
- The `SignalHandler` integrates seamlessly with Python's standard logging system, allowing developers to use familiar `logging.info()`, `logging.error()`, etc., calls, while the output is redirected to the GUI.
- This pattern promotes a clean separation of concerns between logging logic and GUI display logic.
