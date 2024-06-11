"""
-- Created by: Ashok Kumar Pant
-- Created on: 10/17/22
"""
import traceback

from fastapi import APIRouter, UploadFile, File

from classattendance.endpoint.attendance_system import AttendanceSystem
from classattendance.entities.attendance_req_res import FaceDetectionResponse
from classattendance.entities.file_detail import FileDetail
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


@router.post("/face/detect", tags=["Attendance"], response_model=FaceDetectionResponse)
async def detect_face(file: UploadFile = File(default=None)):
    try:
        if file is None:
            return FaceDetectionResponse(error=True, msg="File not selected")
        file_detail = FileDetail(file_name=file.filename, file_path=file.file)
        return await system.get_face_detector().detect(file_detail.file_path)
    except Exception as e:
        logger.exception(e)
        return FaceDetectionResponse(error=True, msg=str(e))
