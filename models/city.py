#!/usr/bin/python3
"""class City that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """A City.

    Attributes:
        state_id (str): id of state.
        name (str): name of state.
    """
    state_id = ""
    name = ""
