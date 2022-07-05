#!/usr/bin/env python3
"""
User class that inherits from BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """ Class that defines attributes for an user """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the class User."""
        super().__init__(self, *args, **kwargs)
