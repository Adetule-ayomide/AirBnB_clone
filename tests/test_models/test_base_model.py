import unittest
"""unittest for BaseModel"""
from os import path
from models.base_model import BaseModel
from datetime import datetime
import uuid

MODEL = path.join(path.join(getcwd(), 'models', 'base_model.py'))

class TestBase(unittest.TestCase):
    """test BaseModel functionality"""

    # ------------- BaseModel
    def test_init(self):
        """Test the constructor (__init__) method"""
        case = BaseModel()
        self.assertIsInstance(case, BaseModel)

    def test_instance_type(self):
        """test the type of BaseModel instance"""
        case1 = BaseModel()
        self.assertIsInstance(case1, BaseModel)

    def test_base_model_printing(self):
        """test the format of printing an instance"""
        case = BaseModel()
        format = f"[{case.__class__.__name__}] ({case.id}) {case.__dict__}"
        self.assertEqual(str(case), format)

    def test_instance_inequality(self):
        """test the inequality of two instances"""
        case1 = BaseModel()
        case2 = BaseModel()
        self.assertNotEqual(case1, case2)

    def test_instanceID_inequality(self):
        """test the inequality of two instances IDs"""
        case1 = BaseModel()
        case2 = BaseModel()
        self.assertNotEqual(case1.id, case2.id)

    def test_inequality_of_created_updated(self):
        """test the inequality of created_at and updated_at attributes
         after using the save(self) method"""
        case = BaseModel()
        self.assertNotEqual(case.created_at, case.updated_at)

    def test_created_time_less_than_current_time(self):
        """test if the created time is always less than the current time"""
        case = BaseModel()
        self.assertTrue(case.created_at < datetime.now())

    def test_inequality_of_updated_at(self):
        """Check the inequality of updated_at and updated_at attributes
        before and after using the save(self) method"""
        case = BaseModel()
        previous_updated_at = case.updated_at
        case.save()
        self.assertNotEqual(previous_updated_at, case.updated_at)

    def test_id_is_uuid4_string(self):
        """Ensure id is a uuid4 string (len == 36)"""
        case = BaseModel()
        self.assertTrue(len(case.id) == 36)
        self.assertEqual(uuid.UUID(case.id).version, 4)

    def test_to_dict_iso_format(self):
        """test if created_at and updated_at are in the “%Y-%m-%dT%H:%M:%S.%f”
        ISO format in the dictionary returned from to_dict method"""
        case = BaseModel()
        model_dict = case.to_dict()
        iso_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(model_dict['created_at'], case.created_at.strftime(iso_format))
        self.assertEqual(model_dict['updated_at'], case.updated_at.strftime(iso_format))

    def test_updated_at_after_save(self):
        """test if the updated_at after using the save
         method is greater than the old updated_at"""
        case = BaseModel()
        old_updated_at = case.updated_at
        case.save()
        self.assertTrue(case.updated_at > old_updated_at)

    def test_to_dict_keys_and_values(self):
        """test if to_dict method returned a dictionary
        that has the correct keys and values"""
        case = BaseModel()
        model_dict = case.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_created_updated_at_instances(self):
        """test if created_at and updated_at are instances of datetime"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_deserialization_and_reloading_from_JSON(self):
        """Test deserialization and reloading from JSON"""
        case = BaseModel()
        model_dict = case.to_dict()
        reloaded_model = BaseModel(**model_dict)
        self.assertEqual(case.id, reloaded_model.id)
        self.assertEqual(case.created_at, reloaded_model.created_at)
        self.assertEqual(case.updated_at, reloaded_model.updated_at)

    def test_UUID_Length(self):
        """test the length of the UUID"""
        case = BaseModel()
        self.assertEqual(len(case.id), 36)

    def test_UUID_type(self):
        """test the type of the UUID"""
        case = BaseModel()
        self.assertIsInstance(case.id, str)

    def test_dates(self):
        """test the inequality of dates"""
        case = BaseModel()
        self.assertNotEqual(case.created_at, case.updated_at)


if __name__ == '__main__':
    unittest.main()
