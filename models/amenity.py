#!/usr/bin/python3
"""This defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This represent an amenity.

    attrs:
        name: Name of the amenity.
    """

    name = ""
