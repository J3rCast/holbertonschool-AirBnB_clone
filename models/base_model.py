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
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at attribute.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance
        and add __class__ key to this dictionary
        """
        new_dict = self.__dict__
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict

    def __str__(self):
        """Magic method that return a string to use
        when print function is called.
        """
        return "[{}] ({}) {}"\
            .format(type(self).__name__, self.id, self.__dict__)
