#!/usr/bin/python3
"""FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        new_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(new_name, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = FileStorage.__objects
        obj_dict = {obj: new_dict[obj].to_dict() for obj in new_dict.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        try:
            with open(FileStorage.__file_path,) as f:
                obj_dict = json.load(f)
                for i in obj_dict.values():
                    class_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(class_name)(**i))
        except FileNotFoundError:
            return
