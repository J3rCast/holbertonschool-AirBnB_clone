#!/usr/bin/python3
"""This module contains a class
called Review.
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """This class inherits from BaseModel."""
    user_id = ""
    place_id = ""
    text = ""
