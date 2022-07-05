#!/usr/bin/python3
"""This module contains a class
called amenity.
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class inherits from BaseModel."""
    name = ""

    def __init__(self, *args, **kargs):
        """ Initialize the Amenity class."""
        super().__init__(*args, **kargs)
