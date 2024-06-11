"""
-- Created by: Ashok Kumar Pant
-- Email: asokpant@gmail.com
-- Created on: 11/06/2024
"""
from classattendance.service.attendance_service import AttendanceService
from classattendance.service.enrollment_service import EnrollmentService
from classattendance.service.face_detector import FaceDetector
from classattendance.utils.singleton import singleton


@singleton
class AttendanceSystem:
    def __init__(self):
        self.face_detector = None
        self.enrollment_service = None
        self.attendance_service = None

        self.__build()

    def __build(self):
        self.face_detector = FaceDetector()
        self.enrollment_service = EnrollmentService()
        self.attendance_service = AttendanceService()

    def get_face_detector(self):
        return self.face_detector

    def get_enrollment_service(self):
        return self.enrollment_service

    def get_attendance_service(self):
        return self.attendance_service
