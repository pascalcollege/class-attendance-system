"""
-- Created by: Ashok Kumar Pant
-- Email: asokpant@gmail.com
-- Created on: 11/06/2024
"""
from typing import List

from pydantic import BaseModel


class Face(BaseModel):
    face_id: int = None
    profile_id: int = None
    bbox: List[float] = None
    score: float = None
    face_encoding: str = None
    chip: bytes = None
