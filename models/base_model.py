#!/usr/bin/python3
"""This module contains a class BaseModel that defines all
   common attributes/methods for other classes.
"""


import uuid
from datetime import datetime

class BaseModel:
    """This is an abstract class that defines attributes
    for other classes.
    """
    def __init__(self):
        """Initialize the object
        Args:
            id (string): Unique id of the object
        """
        self.id = uuid.uuid4()
        self.created_at = datetime()
        self.updated_at = datetime()

    def __str__(self):
        """Magic method that return a string to use
        when print function is called.
        """
        pass
