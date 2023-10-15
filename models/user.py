#!/usr/bin/python3
"""
a class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """a class User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
