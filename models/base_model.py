#!/usr/bin/python3
"""BaseModel class Defines."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel of HBnB project"""

    def __init__(self, *args, **kwargs):
        """A mew BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for i, a in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(a, time_form)
                else:
                    self.__dict__[i] = a
        else:
            models.storage.new(self)

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        myClass = self.__class__.__name__
        return "[{}] ({}) {}".format(myClass, self.id, self.__dict__)
