"""
-- Created by: Ashok Kumar Pant
-- Email: asokpant@gmail.com
-- Created on: 11/06/2024
"""
import logging
import os
from logging import config


class Logger(object):
    _instance = None

    def __new__(cls):
        """Creates a new instance only if it doesn't already exist."""
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        """Constructor that reads the configuration file."""
        filepath = os.environ.get('LOGGING_FILE_PATH', 'logging.ini')
        super().__init__()
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Logging config file not found: {filepath}")
        config.fileConfig(fname=filepath)

    @classmethod
    def get_logger(cls, name="root"):
        if not cls._instance:
            Logger()
        return logging.getLogger(name)

# Example usage
