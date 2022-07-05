#!/usr/bin/python3
"""This module contains a class
called City.
"""


from model.base_models import BaseModel


class City(BaseModel):
    """This class inherits from BaseModel."""
    name = ""
    state_id = ""
