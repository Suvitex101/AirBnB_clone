#!/usr/bin/python3
"""class Place that inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """A Place.

    Attributes:
        city_id (str): id of city.
        user_id (str): id of user.
        name (str): name of place.
        description (str): description of place.
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms.
        max_guest (int): max number of guest.
        price_by_night (int): night price.
        latitude (float): latitude
        longitude (float): longitude
        amenity_ids (str): list of string
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
