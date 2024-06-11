"""
-- Created by: Ashok Kumar Pant
-- Email: asokpant@gmail.com
-- Created on: 11/06/2024
"""
from typing import List, Optional

from pydantic import BaseModel

from classattendance.entities.face import Face


class FaceDetectionRequest(BaseModel):
    image_url: str = None


class FaceDetectionResponse(BaseModel):
    error: bool = False
    message: str = None
    faces: Optional[List[Face]] = None
