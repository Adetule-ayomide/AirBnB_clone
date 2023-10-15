import unittest
from unittest.mock import patch
from io import StringIO
from models import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        """Set up test environment."""
        self.cmd = HBNBCommand()
        self.hbnb_output = StringIO()

    def tearDown(self):
        """Clean up after each test."""
        self.hbnb_output.close()

    def test_create_no_args(self):
        """Test create method with no arguments"""
        with patch('sys.stdout', self.hbnb_output):
            self.cmd.onecmd("create")
        self.assertIn("** class name missing **", self.hbnb_output.getvalue())

    def test_show_no_class_name(self):
        """Test show method with no class name"""
        with patch('sys.stdout', self.hbnb_output):
            self.cmd.onecmd("show")
        self.assertIn("** class name missing **", self.hbnb_output.getvalue())

    def test_show_no_instance_id(self):
        """Test show method with no instance id"""
        with patch('sys.stdout', self.hbnb_output):
            self.cmd.onecmd("show BaseModel")
        self.assertIn("** instance id missing **", self.hbnb_output.getvalue())

    def test_destroy_no_class_name(self):
        """Test destroy method with no class name"""
        with patch('sys.stdout', self.hbnb_output):
            self.cmd.onecmd("destroy")
        self.assertIn("** class name missing **", self.hbnb_output.getvalue())

    def test_destroy_no_instance_id(self):
        """Test destroy method with no instance id"""
        with patch('sys.stdout', self.hbnb_output):
            self.cmd.onecmd("destroy BaseModel")
        self.assertIn("** instance id missing **", self.hbnb_output.getvalue())

    def test_update_no_class_name(self):
        """Test update method with no class name"""
        with patch('sys.stdout', self.hbnb_output):
            self.cmd.onecmd("update")
        self.assertIn("** class name missing **", self.hbnb_output.getvalue())

    def test_update_no_instance_id(self):
        """Test update method with no instance id"""
        with patch('sys.stdout', self.hbnb_output):
            self.cmd.onecmd("update BaseModel")
        self.assertIn("** instance id missing **", self.hbnb_output.getvalue())

if __name__ == '__main__':
    unittest.main()
