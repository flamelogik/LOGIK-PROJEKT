# Static Analysis: `src/core/utils/session_log_utils.py`

## Overview
The `session_log_utils.py` script defines a function `setup_session_logger` that configures and returns a Python `logging.Logger` instance. This logger is specifically designed to create session-specific log files, organized by date, to capture debug-level messages and above. It ensures that log directories are created as needed.

## Dependencies
- **Python Standard Library**: `logging`, `os`, `datetime`

## Function: `setup_session_logger()`

### Purpose
To provide a centralized and standardized way to set up a session-specific logger for the application, enabling detailed logging of events and debugging information to a file.

### Signature
`def setup_session_logger():`

### Logic
1.  **Define Log Directory Base**: Sets `log_dir_base` to `"logs/session-logs"`.
2.  **Get Current Time**: Obtains the current timestamp using `datetime.now()`.
3.  **Construct Date-Based Log Directory**: Extracts the year, month, and day from the current timestamp to create a hierarchical directory structure (e.g., `logs/session-logs/YYYY/MM/DD`).
4.  **Create Log Directory**: Uses `os.makedirs(log_dir, exist_ok=True)` to ensure that the full log directory path exists. `exist_ok=True` prevents an error if the directories already exist.
5.  **Construct Log Filename**: Creates a unique log filename using the full timestamp (e.g., `YYYY-MM-DD-HH-MM-SS-session.log`).
6.  **Construct Full Log File Path**: Combines the `log_dir` and `log_filename` to get the complete `log_filepath`.
7.  **Get Logger Instance**: Retrieves a logger instance named `"session_logger"` using `logging.getLogger()`.
8.  **Set Logger Level**: Sets the logger's level to `logging.DEBUG`, meaning it will process all messages from DEBUG level upwards.
9.  **Create File Handler**: Creates a `logging.FileHandler` for the `log_filepath`.
10. **Set File Handler Level**: Sets the file handler's level to `logging.DEBUG`, ensuring all debug messages are written to the file.
11. **Create Formatter**: Defines a `logging.Formatter` with a standard log message format (`%(asctime)s - %(name)s - %(levelname)s - %(message)s`).
12. **Add Formatter to Handler**: Assigns the formatter to the file handler.
13. **Add Handler to Logger**: Adds the configured file handler to the logger instance.

### Observations
-   This function provides a robust and organized logging solution, automatically creating dated directories for log files.
-   Logging to a file at `DEBUG` level is highly beneficial for detailed debugging and troubleshooting in a production environment.
-   The use of `logging.getLogger("session_logger")` ensures that subsequent calls to this function or `logging.getLogger("session_logger")` will return the same logger instance, preventing duplicate handlers.
-   The log file naming convention ensures uniqueness and easy identification of logs by session and date.
-   This setup is ideal for capturing application behavior over time without cluttering the console.
