#!/usr/bin/python3
"""Unittest module for file storage."""


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from os import path, remove
import json


class Test_all(unittest.TestCase):
    """Test for the all method."""

    def test_all(self):
        """Check if it return a dictionary."""
        self.storage = FileStorage()
        self.assertIsInstance(self.storage.all(), dict)

class Test_new(unittest.TestCase):
    """Test for the new method."""

    def setUp(self):
        """Set up for every test"""
        try:
            remove("file.json")
        except Exception:
            pass
        FileStorage.__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except Exception:
            pass

    def test_new(self):
        """Check if the object is in __object."""
        self.storage = FileStorage()
        self.user = User()
        ob_dict = self.storage.all()
        key = "{}.{}".format(type(self.user).__name__, self.user.id)
        self.assertTrue(key in ob_dict.keys())

    def test_save(self):
        """Check the save method."""
        MyModel = BaseModel()
        self.storage = FileStorage()
        self.storage.save()
        self.path = self.storage._FileStorage__file_path
        with open(self.path) as file:
            file_dict = json.load(file)
        self.assertIn(MyModel.to_dict(), file_dict.values())
