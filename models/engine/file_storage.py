#!/usr/bin/python3
"""This module contains a class that serializes instances to a
SON file and deserializes JSON file to instances:
"""


import json
from os import path


class FileStorage:
    """This class serializes and deserializes
    instances and JSON files.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id

        Args:
            obj: object to set in __object
        """
        key_name = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key_name] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        new_dict = {}
        for key in self.__objects:
            new_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects."""
        from ..amenity import Amenity
        from ..city import City
        from ..place import Place
        from ..review import Review
        from ..state import State
        from ..user import User
        from models.base_model import BaseModel
        file = FileStorage.__file_path
        if path.isfile(file):
            with open(self.__file_path, 'r') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value['__class__'])(**value)
                    self.__objects[key] = value
