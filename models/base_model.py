#!/usr/bin/python3
"""This module is the class BaseModel"""


import uuid
import sys
from datetime import datetime
import models


class BaseModel:
    """This is the base model for our project"""

    def __init__(self, *args, **kwargs):
        """This is the constructor for our instances"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.fromisoformat(self.updated_at)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Prints information about the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all
           key-values of __dict__ of the instance"""
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
