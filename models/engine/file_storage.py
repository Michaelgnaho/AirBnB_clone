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

class FileStorage:
    '''File storage class'''
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        '''Returns the dictionary __objects'''
        return FileStorage.__objects
    
    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        FileStorage.__objects[f"{__class__.__name__}.{self.id}"] = obj

    def save(self):
        '''serializes __objects to the JSON file'''
        x = FileStorage.__objects
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f)
    
    def reload(self):
        '''deserializes the JSON file to __objects'''
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
