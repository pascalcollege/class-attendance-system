"""
-- Created by: Ashok Kumar Pant
-- Created on: 11/06/2024
"""
from classattendance.utils.config import Config


class Settings:
    API_PORT = Config.get_instance().getint('default', 'api.port', fallback=8000)
