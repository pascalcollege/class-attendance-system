"""
-- Created by: Ashok Kumar Pant
-- Email: asokpant@gmail.com
-- Created on: 11/06/2024
"""
import logging

from classattendance.utils.logger import Logger

if __name__ == '__main__':
    logger = Logger.get_logger(__name__)
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.debug('This is a debug message')
