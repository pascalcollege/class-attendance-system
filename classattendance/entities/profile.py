"""
-- Created by: Ashok Kumar Pant
-- Email: asokpant@gmail.com
-- Created on: 11/06/2024
"""
from pydantic import BaseModel


class Profile(BaseModel):
    profile_id: int = None
    first_name: str = None
    last_name: str = None
    email: str = None
    phone: str = None
    profile_picture_url: str = None
