#!/usr/bin/python3
"""review module
"""

# Local application imports
from models.base_model import BaseModel


class Review(BaseModel):
    """ a class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""