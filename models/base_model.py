#!/usr/bin/python3
import datetime
import uuid

""" BaseModel module """


class BaseModel:
    '''The base class that defines all
    common attributes/methods for other classes'''

    def __init__(self):
        '''The initialization for BaseModel class'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = self.created_at

    def __str__(self):
        '''Returns a representation of an object of BaseModel class'''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''Update the date due the last modification of an object'''
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values
        of __dict__ of the instance'''
        cls_name = {"__class__": self.__class__.__name__}
        merge = {**cls_name, **self.__dict__}
        return merge
