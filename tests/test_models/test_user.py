import unittest
from os import path
from models.base_model import BaseModel
from datetime import datetime


MODEL = path.join(path.join(getcwd(), 'models', 'user.py'))


class TestUser(unittest.TestCase):

    def test_user_instance(self):
        """Test if User instance is created"""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        """Test if User attributes are initialized correctly"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_inheritance(self):
        """Test if User inherits from BaseModel"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_user_to_dict(self):
        """Test the to_dict() method of User"""
        user = User()
        user_dict = user.to_dict()

        self.assertIsInstance(user_dict, dict)
        self.assertIn('__class__', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')

    def test_user_str(self):
        """Test the __str__() method of User"""
        user = User()
        user_str = str(user)

        expected_str = f"[User] ({user.id}) {user.__dict__}"
        self.assertEqual(user_str, expected_str)


if __name__ == '__main__':
    unittest.main()
