#!/usr/bin/python3
"""
This is a class that defines all common attributes/methods
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """initalizing instances """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at.now()

        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)


    def __str__(self):
        """returns a string representation of an object"""
        cls = self.__class__.__name__
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        """
        if instance is available then self update will update it's self
        everytime the object changes
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        this function returns a dictionary
        containing all keys/values of __dict__ of the instance
        """
        obj_to_dic = self.__dict__.copy()
        obj_to_dic['__class__'] = str(type(self)).split('.')[-1].split('\'')[0]
        obj_to_dic['created_at'] = self.created_at.isoformat()
        obj_to_dic['updated_at'] = self.updated_at.isoformat()
        return obj_to_dic
