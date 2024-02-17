import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """step up"""
        self.storage = FileStorage()

    def tearDown(self):
        """tear down"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_file_path_exists(self):
        """check if file path exists"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_objects_exists(self):
        """check if object exists"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_all_method(self):
        """test all method"""
        obj = BaseModel()
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertIn(type(obj).__name__ + '.' + obj.id, all_objs)

    def test_new_method(self):
        """test new method"""
        obj = BaseModel()
        self.storage.new(obj)
        key = type(obj).__name__ + '.' + obj.id
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_save_method(self):
        """test save model"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, "r") as file:
            saved_objs = json.load(file)
            key = type(obj).__name__ + '.' + obj.id
            self.assertIn(key, saved_objs)

    def test_reload_method(self):
        """test reload method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = type(obj).__name__ + '.' + obj.id
        self.assertIn(key, new_storage._FileStorage__objects)

if __name__ == '__main__':
    unittest.main()