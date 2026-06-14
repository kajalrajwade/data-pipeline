import logging
import sys
from datetime import datetime

def get_logger(name):
    """
    Create a logger with consistent formatting across the project
    
    Args:
        name: Name of the logger (usually __name__)
    
    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)
    
    # Only add handler if it doesn't exist (avoid duplicates)
    if not logger.handlers:
        # Create handler that writes to terminal
        handler = logging.StreamHandler(sys.stdout)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Connect formatter to handler
        handler.setFormatter(formatter)
        
        # Add handler to logger
        logger.addHandler(handler)
        
        # Set log level
        logger.setLevel(logging.INFO)
    
    return logger
