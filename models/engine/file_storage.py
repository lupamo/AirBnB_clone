#!/usr/bin/python3
"""
Module for the File storage class resposible for serialization
and deserialization
"""
import json
import os
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """ The class for storing and retrieving date."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Responsible for retreating all the objects
        stored, returns the dict obj"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>
        .id, it adds a new object to class attribute
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        (path: __file_path/json format for storing
        """
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if
        the JSON file (__file_path) exists ; otherwise, do nothing.
        """
        if os.path.isfile(self.__file_path):
            try:
                with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
            except FileNotFoundError:
                pass
        return FileStorage.__objects
