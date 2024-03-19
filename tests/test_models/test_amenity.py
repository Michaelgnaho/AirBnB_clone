#!/usr/bin/env python3
"""Unittest module for the Amenity Class."""

from models.amenity import Amenity
from models.base_model import BaseModel
import unittest
import datetime
import os

class TestAmenity(unittest.TestCase):
    """Amenity model class test case"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.amenity = Amenity()
        cls.amenity.name = "Wifi"

    @classmethod
    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(Amenity.__doc__)

    a = Amenity()
    def test_has_attributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))

    def test_attributes_are_string(self):
        self.assertIs(type(self.amenity.name), str)

    def test_class_exists(self):
        '''Tests whether class exists or not'''
        x = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.a)), x)

    def test_user_inheritance(self):
        '''Tests if Amenity is a subclass of BaseModel'''
        self.assertIsInstance(self.a, Amenity)

    def test_types(self):
        '''tests if the type of the attribute is the correct one'''
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)

    def test_save(self):
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.amenity))


if __name__ == "__main__":
    unittest.main()