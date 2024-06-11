"""
-- Created by: Ashok Kumar Pant
-- Created on: 11/06/2024
"""
from classattendance.utils.config import Config

if __name__ == '__main__':
    print(Config().get_instance())
    print(Config().get_instance())
    print(Config())
    print(Config())
    print(Config.get_instance())
    print(Config.get_instance())
    print(Config.get_instance().sections())
    print(Config.get_instance().get("default", "environment"))
