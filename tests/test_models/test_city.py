#!/usr/bin/python3
"""The test module for the City Class"""

import unittest
from datetime import datetime
import uuid
from models.city import City
import os
from models import storage
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """City model class test case"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.city = City()
        cls.city.state_id = str(uuid.uuid4())
        cls.city.name = "St. Petesburg"

    @classmethod
    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_instance_is_stored(self):
        self.assertIn(City(), storage.all().values())

    def test_id_is_pub(self):
        self.assertEqual(str, type(City().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.city.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(City.__doc__)

    def test_attrs(self):
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_state_id_is_public_class_attribute(self):
        c = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(c))
        self.assertNotIn("state_id", c.__dict__)

    def test_name_is_public_class_attribute(self):
        c = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(c))
        self.assertNotIn("name", c.__dict__)

    def test_attributes_are_string(self):
        self.assertIs(type(self.city.state_id), str)
        self.assertIs(type(self.city.name), str)

    def test_save(self):
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.city))


if __name__ == "__main__":
    unittest.main()