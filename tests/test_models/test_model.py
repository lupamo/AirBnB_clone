import unittest

from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModelToDict(unittest.TestCase):
    def test_to_dict(self):
        """Create a BaseModel instance"""
        obj = BaseModel()
        """ Call to_dict() method"""
        obj_dict = obj.to_dict()

        """Verify that the returned dictionary contains all the keys"""
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)

        """Verify the values of the keys"""
        self.assertEqual(obj.id, obj_dict['id'])
        self.assertEqual(obj.created_at.isoformat(), obj_dict['created_at'])
        self.assertEqual(obj.updated_at.isoformat(), obj_dict['updated_at'])
        self.assertEqual('BaseModel', obj_dict['__class__'])

    def test_save(self):
        """create a BaseModel instance"""
        obj = BaseModel()
        created_at = obj.created_at
        updated_at = obj.updated_at

        """call save() method"""
        obj.save()

        """verify that updated_at has been updated"""
        self.assertNotEqual(updated_at, obj.updated_at)
        """Verify that created_at has not changed"""
        self.assertEqual(created_at, obj.created_at)

        """Check if the object is saved to a file"""
        self.assertTrue(os.path.isfile("file.json"))
    def test_id(self):
        """Create multiple BaseModel instances"""
        obj1 = BaseModel()
        obj2 = BaseModel()

        """Check that the id attribute is a string"""
        self.assertIsInstance(obj1.id, str)
        self.assertIsInstance(obj2.id, str)

        """check that the ids are unique"""
        self.assertNotEqual(obj1.id, obj2.id)

    def test_str(self):
        """create a BaseModel instance"""
        obj = BaseModel()

        """check the string representation"""
        expected_str = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_str)


if __name__ == '__main__':
    unittest.main()