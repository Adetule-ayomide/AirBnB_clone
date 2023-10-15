#!/usr/bin/python3
"""class State"""

from base_model import BaseModel


class State(BaseModel):
    """A state class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
