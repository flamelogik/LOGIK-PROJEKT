import platform
import logging

def check_operating_system():
    """Check if the operating system is Linux or macOS."""
    os_name = platform.system()
    if os_name == 'Linux':
        logging.info("Operating system is Linux.")
        return 'Linux'
    elif os_name == 'Darwin':
        logging.info("Operating system is macOS.")
        return 'macOS'
    else:
        logging.error(f"Unsupported operating system: {os_name}")
        raise EnvironmentError(f"Unsupported operating system: {os_name}")
