#!/usr/bin/python3
"""Unittest module for file storage."""


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from os import path, remove
import pycodestyle
import json


class Test_File_Storage(unittest.TestCase):
    """Test for the all method."""

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

    def test_all(self):
        """Check if it return a dictionary."""
        self.storage = FileStorage()
        self.assertIsInstance(self.storage.all(), dict)

    def test_pep8(self):
        """Test of pep8."""
        st = pycodestyle.StyleGuide(quiet=True)
        r = st.check_files(['models/engine/file_storage.py'])
        self.assertEqual(r.total_errors, 0,
                         "Found code style errors (and warnings).")

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

    def test_reload_method(self):
        """ Check the reload() method."""
        self.storage = FileStorage()
        MyModel = BaseModel()
        self.storage.save()
        self.storage.reload()
        key = "BaseModel.{}".format(MyModel.id)
        ob_dict = self.storage.all()
        self.assertFalse(ob_dict[key] is MyModel)
