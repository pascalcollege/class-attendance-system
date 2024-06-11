"""
-- Created by: Ashok Kumar Pant
-- Created on: 11/06/2024
"""

import configparser
import os.path
from configparser import ConfigParser


class Config(configparser.ConfigParser):
    """Singleton class that wraps ConfigParser for a single configuration instance."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        """Creates a new instance only if it doesn't already exist."""
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.__init__(*args, **kwargs)
        return cls._instance

    def __init__(self):
        """Constructor that reads the configuration file."""
        config_file_path = os.environ.get('CONFIG_FILE_PATH', 'config.ini')
        super().__init__()
        if not os.path.exists(config_file_path):
            raise FileNotFoundError(f"Config file not found: {config_file_path}")
        self.read(config_file_path)

    @classmethod
    def get_instance(cls) -> ConfigParser:
        """Returns the singleton instance of the ConfigParser subclass."""
        if not Config._instance:
            Config()
        return Config._instance
