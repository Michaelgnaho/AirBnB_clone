#!/usr/bin/env python3
"""The test model for (review) class"""

import unittest
import os
from datetime import datetime
from time import sleep
from models import storage
from models.review import Review
from models.base_model import BaseModel
import uuid


class TestReview(unittest.TestCase):
    """Review model class test case"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.review = Review()
        cls.review.user_id = str(uuid.uuid4())
        cls.review.place_id = str(uuid.uuid4())
        cls.review.text = "So great and peaceful"

    @classmethod
    def tearDownClass(cls):
        """Cleans class up"""
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.review.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(Review.__doc__)


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_is_stored(self):
        self.assertIn(Review(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_id_is_pub(self):
        r = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(r))
        self.assertNotIn("place_id", r.__dict__)

    def test_user_id_is_pub_cls(self):
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_text_is_public_cls(self):
        r = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(r))
        self.assertNotIn("text", r.__dict__)

    def test_two_reviews_unique_ids(self):
        r1 = Review()
        r2 = Review()
        r3 = Review()
        r4 = Review()
        self.assertNotEqual(r1.id, r2.id)
        self.assertNotEqual(r1.id, r3.id)
        self.assertNotEqual(r2.id, r4.id)
        self.assertNotEqual(r3.id, r4.id)

    def test_two_rev_created_at(self):
        r1 = Review()
        sleep(0.1)
        r2 = Review()
        self.assertLess(r1.created_at, r2.created_at)

    def test_two_reviews_different_updated_at(self):
        rv1 = Review()
        sleep(0.1)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        r = Review()
        r.id = "123456"
        r.created_at = r.updated_at = dt
        r_str = r.__str__()
        self.assertIn("[Review] (123456)", r_str)
        self.assertIn("'id': '123456'", r_str)
        self.assertIn("'created_at': " + dt_repr, r_str)
        self.assertIn("'updated_at': " + dt_repr, r_str)

    def test_args_unused(self):
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        rv = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rv.id, "345")
        self.assertEqual(rv.created_at, dt)
        self.assertEqual(rv.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

class TestReview(unittest.TestCase):
    """Review model class test case"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.review = Review()
        cls.review.user_id = str(uuid.uuid4())
        cls.review.place_id = str(uuid.uuid4())
        cls.review.text = "St. Petesburg"

    @classmethod
    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.review.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(Review.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)

    def test_attributes_are_string(self):
        self.assertIs(type(self.review.user_id), str)
        self.assertIs(type(self.review.place_id), str)
        self.assertIs(type(self.review.text), str)

    def test_save(self):
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.review))

if __name__ == "__main__":
    unittest.main()