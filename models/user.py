#!/usr/bin/python3
"""User module
"""

# Local application imports
from models.base_model import BaseModel


class User(BaseModel):
    """ a class that inherits from BaseModel"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
