#!/usr/bin/python3
from datetime import datetime
import uuid

""" BaseModel module """


class BaseModel:
    '''The base class that defines all
    common attributes/methods for other classes'''

    def __init__(self):
        '''The initialization for BaseModel class'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        '''Returns a representation of an object of BaseModel class'''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''Update the date due to the last modification of an object'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values
        of __dict__ of the instance'''
        new_dic = self.__dict__.copy
        new_dic['__class__'] = self.__class__.__name__
        new_dic['created_at'] = self.created_at.isoformat()
        new_dic['updated_at'] = self.updated_at.isoformat()
        return new_dic
