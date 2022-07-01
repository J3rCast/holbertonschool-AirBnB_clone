#!/usr/bin/python3
"""This module contains a class BaseModel that defines all
   common attributes/methods for other classes.
"""


import uuid

class BaseModel:
    """This is an abstract class that defines attributes
    for other classes.
    """
    def __init__(self):
        """Initialize the object
        Args:
            id (string): Unique id of the object
        """
