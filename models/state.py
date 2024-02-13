#!/usr/bin/python3
"""class State that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """A State.

    Attributes:
        name (str): name of state.
    """
    name = ""
