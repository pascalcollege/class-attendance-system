"""
-- Created by: Ashok Kumar Pant
-- Email: asokpant@gmail.com
-- Created on: 11/06/2024
"""
from typing import Optional

from pydantic import BaseModel


class FileDetail(BaseModel):
    error: Optional[bool] = False
    msg: Optional[str] = None
    file_path: Optional[str] = None
    file_name: Optional[str] = None
