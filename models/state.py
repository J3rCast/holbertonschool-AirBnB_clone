#!/usr/bin/python3
"""This module contains a class
called State.
"""


from models.base_model import BaseModel


class State(BaseModel):
    """This class inherits from BaseModel."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the class State."""
        super().__init__(self, *args, **kwargs)
