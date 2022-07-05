#!/usr/bin/python3
"""This module contains a class
called Place.
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """This class inherits from BaseModel."""
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [""]
