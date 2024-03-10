#!/usr/bin/python3
""" FileStorage module """

import json
from models.review import Review
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
import os


clss = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
    "State": State
}


class FileStorage:
    '''File storage class'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects'''
        return type(self).__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        if obj.id in type(self).__objects:
            return
        else:
            k = f"{obj.__class__.__name__}.{obj.id}"
            type(self).__objects[k] = obj

    def save(self):
        '''serializes __objects to the JSON file'''
        x = []
        for obj in type(self).__objects.values():
            x.append(obj.to_dict())
        with open(type(self).__file_path, "w", encoding='utf-8') as f:
            json.dump(x, f)

    def reload(self):
        '''deserializes the JSON file to __objects'''
        if os.path.exists(type(self).__file_path) is True:
            return
            try:
                with open(type(self).__file_path, "r") as f:
                    n_obj = json.load(f)
                    for k, val in n_obj.items():
                        obj = self.clss_dict[val['__class__']](**val)
                        type(self).__objects[k] = obj
            except Exception:
                pass
