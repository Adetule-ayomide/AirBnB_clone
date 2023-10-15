import unittest
from models.city import City
from datetime import datetime
import uuid

class TestCity(unittest.TestCase):

    def setUp(self):
        """
        Set up a City instance for testing.
        """
        self.city = City()

    def tearDown(self):
        """
        Clean up after each test.
        """
        del self.city

    def test_city_instance(self):
        """
        Test if the city is an instance of the City class.
        """
        self.assertIsInstance(self.city, City)

    def test_city_inherits_from_base_model(self):
        """
        Test if City inherits from BaseModel.
        """
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_attributes(self):
        """
        Test the attributes of the City class.
        """
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_city_initial_attributes(self):
        """
        Test the initial attributes of a City instance.
        """
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_city_id_attribute(self):
        """
        Test if the City instance has an 'id' attribute.
        """
        self.assertTrue(hasattr(self.city, 'id'))

    def test_city_created_at_attribute(self):
        """
        Test if the City instance has a 'created_at' attribute.
        """
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertIsInstance(self.city.created_at, datetime)

    def test_city_updated_at_attribute(self):
        """
        Test if the City instance has an 'updated_at' attribute.
        """
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_city_str_method(self):
        """
        Test the __str__ method of the City class.
        """
        expected_str = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_city_to_dict_method(self):
        """
        Test the to_dict method of the City class.
        """
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
