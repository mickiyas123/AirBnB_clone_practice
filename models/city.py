#!/usr/bin/python3
""" city Module """

# Local Application Import
from models.base_model import BaseModel


class City(BaseModel):
    """ City class that inherit from BaseModel """
    name = ""
    state_id = ""
