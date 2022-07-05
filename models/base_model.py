#!/usr/bin/python3
"""This module contains a class BaseModel that defines all
   common attributes/methods for other classes.
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """This is an abstract class that defines attributes
    for other classes.
    """
    def __init__(self, *args, **kwargs):
        """Initialize the object
        Args:
            id (string): Unique id of the object
        """
        if kwargs:
            for arg in kwargs:
                if arg == '__class__':
                    continue
                if arg == 'created_at' or arg == 'updated_at':
                    setattr(self, arg, datetime.fromisoformat(kwargs[arg]))
                else:
                    setattr(self, arg, kwargs[arg])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Magic method that return a string to use
        when print function is called.
        """
        return "[{:s}] ({:s}) {:s}"\
            .format(type(self).__name__, self.id, str(self.__dict__))

    def save(self):
        """Update the updated_at attribute.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance
        and add __class__ key to this dictionary.
        """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
