#!/usr/bin/python3
"""This defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """The represent a User.

    Attributes:
        email (str): Email of the user.
        password (str): Password of the user.
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
