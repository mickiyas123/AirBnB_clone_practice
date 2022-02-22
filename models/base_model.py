#!/usr/bin/python3
""" Base Module that defines all common
    attributes/methods for other classes
"""

# Standard Library imports
import uuid
from datetime import datetime

# Local application imports


class BaseModel:
    """ class for creating base model objects """

    def __init__(self, *args, **kwargs):
        """ BaseModel Inits

            args: non keyword argument
            kwargs: keyword argument
        """
        if kwargs:
            for key in kwargs:
                if key not in ['created_at', 'updated_at', '__class__']:
                    setattr(self, key, kwargs[key])
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
                self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """ return string representattion of the object """
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance

        key __class__ must is added to this dictionary
        with the class name of the object

        created_at and updated_at are converted
        to string object in ISO format

        """
        new_dict = self.__dict__.copy()
        class_name = type(self).__name__
        new_dict['__class__'] = class_name
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
