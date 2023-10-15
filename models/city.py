#!/usr/bin/python3
"""class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """A City class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
