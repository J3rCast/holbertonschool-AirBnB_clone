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
        FileStorage.__objects[key_name] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects."""
        file = FileStorage.__file_path
        if path.isfile(file):
            with open(file, mode='r', encoding='utf-8') as f:
                FileStorage.__objects = json.load(f)
