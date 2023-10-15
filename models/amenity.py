#!/usr/bin/python3
"""class Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """A Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes amenity"""
        super().__init__(*args, **kwargs)
