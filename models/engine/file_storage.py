#!/usr/bin/python3
""" FileStorage module """

import json


class FileStorage:
    '''File storage class'''
    __file_path = "file.json"
    __objects = {}
    
    def __init__(self):
        pass
    
    def all(self):
        '''Returns the dictionary __objects'''
        return FileStorage.__objects
    
    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        FileStorage.__objects[f"{__class__.__name__}.{self.id}"] = obj

    def save(self):
        '''serializes __objects to the JSON file'''
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f)
    
    def reload(self):
        '''deserializes the JSON file to __objects'''
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass

    