"""
-- Created by: Ashok Kumar Pant
-- Created on: 10/17/22
"""
import traceback

from fastapi import APIRouter

from classattendance.endpoint.attendance_system import AttendanceSystem
from classattendance.utils.logger import Logger

logger = Logger.get_logger(__name__)
router = APIRouter()


@router.on_event("startup")
async def startup_event():
    global system
    try:
        system = AttendanceSystem()
    except Exception as e:
        logger.debug(f"System could not be loaded: {str(e)}")
        traceback.print_exc()
