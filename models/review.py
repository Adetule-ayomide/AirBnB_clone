#!/usr/bin/python3
"""class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes review"""
        super().__init__(*args, **kwargs)
