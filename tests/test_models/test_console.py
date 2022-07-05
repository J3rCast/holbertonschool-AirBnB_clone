#!/usr/bin/env python3
""" Unittests for AirBnB Console"""


from console import HBNBCommand
import unittest
from unittest.mock import patch
import io
from models.engine.file_storage import FileStorage
from models import storage


class Test_non_existing_command(unittest.TestCase):
    """ Tests a command that does not exist """

    def test_unknown(self):
        """ Command that does not exist """
        msg = "*** Unknown syntax: asd\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("asd")
            st = f.getvalue()
            self.assertEqual(msg, st)

class Test_help(unittest.TestCase):
    """ Tests the help commands """

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_help_help(self):
        """  Test for help of quit command """
        msg = "List available commands with \"help\" or " \
            "detailed help with \"help cmd\".\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help help")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_help_quit(self):
        """  Test for help of quit command """
        msg = "Quit command to exit the program\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_help_create(self):
        """  Test for help of create command """
        msg = "Create an instance if the Model exists\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help create")
            st = f.getvalue()
            self.assertEqual(msg, st)

class Test_create(unittest.TestCase):
    """ Tests the create commands """

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_create_no_class(self):
        """  Test for create with class missing """
        msg = "** class name missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_create_invalid_class(self):
        """ Test for create invalid class """
        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            st = f.getvalue()
            self.assertEqual(msg, st)

class Test_show(unittest.TestCase):
    """Test the show command."""
    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_show_name_missing(self):
        """Test when name is not given.(ex: $ show)"""
        error = "** class name missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show")
            st = f.getvalue()
            self.assertEqual(error, st)

    def test_show_no_name(self):
        """Test when name doesnt exist."""
        error = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            st = f.getvalue()
            self.assertEqual(error, st)

    def test_show_id_missing(self):
        """Test when id is missing(show BaseModel)."""
        error = "** instance id missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            st = f.getvalue()
            self.assertEqual(error, st)

    def test_show_no_id(self):
        """Test when id doesnt exists(show BaseModel 121212)."""
        error = "** no instance found **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 121212")
            st = f.getvalue()
            self.assertEqual(error, st)

class Test_destroy(unittest.TestCase):
    """Test the destroy command."""

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_destroy_name_missing(self):
        """Test when name is missing ($ destroy)"""
        error = "** class name missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            st = f.getvalue()
            self.assertEqual(error, st)

    def test_destroy_no_name(self):
        """Test when name doesnt exist ($ destroy MyModel)"""
        error = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            st = f.getvalue()
            self.assertEqual(error, st)

    def test_destroy_id_missing(self):
        """Test when id is missing (ex: $ destroy BaseModel)"""
        error = "** instance id missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            st = f.getvalue()
            self.assertEqual(error, st)

    def test_destroy_no_id(self):
        """Test when id doesnt exist (ex: $ destroy BaseModel 121212)"""
        error = "** no instance found **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 121212")
            st = f.getvalue()
            self.assertEqual(error, st)

class Test_all(unittest.TestCase):
    """Test the all command."""

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_all_no_name(self):
        """Test when name doesnt exist (ex: $ all MyModel)"""
        error = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            st = f.getvalue()
            self.assertEqual(error, st)

class Test_update(unittest.TestCase):
    """Test the update command."""

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_update_name_missing(self):
        """Test when name is missing ($ update)"""
        error = "** class name missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update")
            st = f.getvalue()
            self.assertEqual(error, st)

    def test_update_no_name(self):
        """Test when name doesnt exist ($ update MyModel)"""
        error = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
            st = f.getvalue()
            self.assertEqual(error, st)

    def test_update_id_missing(self):
        """Test when id is missing (ex: $ update BaseModel)"""
        error = "** instance id missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            st = f.getvalue()
            self.assertEqual(error, st)

    def test_update_no_id(self):
        """Test when id doesnt exist (ex: $ update BaseModel 121212)"""
        error = "** no instance found **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 121212")
            st = f.getvalue()
            self.assertEqual(error, st)

    def test_update_attribute_name_missing(self):
        """Test when attribute name is missing
        (ex: $ update BaseModel existing-id)
        """
        error = "** attribute name missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as fi:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = fi.getvalue()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel " + obj_id)
            st = f.getvalue()
            self.assertEqual(error, st)

    def test_update_attribute_name_missing(self):
        """Test when value for the attribue name doesnt exist
        (ex: $ update BaseModel existing-id first_name).
        """
        error = "** value missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as fi:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = fi.getvalue()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel " + obj_id + " first_name")
            st = f.getvalue()
            self.assertEqual(error, st)
