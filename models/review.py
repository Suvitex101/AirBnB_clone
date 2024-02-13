#!/usr/bin/python3
"""class Review that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A Review.

    Attributes:
        place_id (str): id of place.
        user_id (str): id of user.
        text (str): review.
    """
    place_id = ""
    user_id = ""
    text = ""
