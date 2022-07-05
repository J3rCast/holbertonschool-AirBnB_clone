#!/usr/bin/python3
"""This module contains a class
called City.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """This class inherits from BaseModel."""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwars):
        """ Initialize the City class."""
        super().__init__(*args, **kwars)
