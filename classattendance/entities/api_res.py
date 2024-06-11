"""
-- Created by: Ashok Kumar Pant
-- Email: asokpant@gmail.com
-- Created on: 11/06/2024
"""
from pydantic import BaseModel


class ApiResponse(BaseModel):
    error: bool = False
    msg: str = None
    result: dict = None
