#!/usr/bin/python3
""" module that serializes instances to a JSON file
    and deserializes JSON file to instances
"""

# Standar Library imports
import json
from os.path import exists


class FileStorage:
    """ class that convert the dictionary representation to a JSON string
        and vice versa

        Private class attribute:
                            file_storage: path to the JSON file
                            objects: dict that stores class instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects:
                        key = <obj class name>.id
                        value = obj
            Args:
                obj: class instance(object)
        """
        class_name = type(obj).__name__
        dict_key = class_name + "." + obj.id
        FileStorage.__objects[dict_key] = obj

    def save(self):
        """ serializes __objects to the JSON file
            since __objects is dict of objects it's coverted to dict of dict
        """
        objects_to_dict = FileStorage.__objects.copy()

        for key in objects_to_dict:
            objects_to_dict[key] = objects_to_dict[key].to_dict()
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(objects_to_dict, json_file, indent=4)

    def reload(self):
        """ deserializes the JSON file to __objects if __file_path exists
            since the the jon file contains "str" it needs to be convrted
            to dict then class instance
        """
        from ..base_model import BaseModel
        from ..user import User
        from ..amenity import Amenity
        from ..city import City
        from ..place import Place
        from ..state import State
        from ..review import Review

        file_exists = exists(FileStorage.__file_path)
        reloaded_dict = {}

        classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
                   "City": City, "Place": Place, "State": State,
                   "Review": Review}

        if file_exists:
            with open(FileStorage.__file_path, "r") as json_file:
                reloaded_dict = json.load(json_file)
            for key, val in reloaded_dict.items():
                FileStorage.__objects[key] = classes[val['__class__']](**val)
