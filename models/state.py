#!/usr/bin/python3
"""This defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """This represent a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
