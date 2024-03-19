#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_instantiation
    TestBase_Instance_Print
    TestBaseModel_save
    TestBase_from_json_string
    TestBaseModel_to_dict
"""

import unittest
from models import storage
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import json
import re


class TestBaseModel_Instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_IsInstanceOf(self):
        """Test instance type"""
        x = BaseModel()
        self.assertTrue(issubclass(type(x), BaseModel))
        self.assertIsInstance(x, BaseModel)
        self.assertEqual(str(type(x)), "<class 'models.base_model.BaseModel'>")

    def test_ContainsId(self):
        """Test id attr exists"""
        x = BaseModel()
        self.assertTrue(hasattr(x, "id"))

    def test_IdType(self):
        """Test id type"""
        x = BaseModel()
        self.assertEqual(type(x.id), str)

    def test_CompareTwoInstancesId(self):
        """Compare distinct instances ids"""
        x1 = BaseModel()
        x2 = BaseModel()
        self.assertNotEqual(x1.id, x2.id)

    def test_uuid(self):
        """Test that id is a valid uuid"""
        x1 = BaseModel()
        x2 = BaseModel()
        for inst in [x1, x2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(x1.id, x2.id)

    def test_uniq_id(self):
        """Tests for unique user ids."""
        u = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(u)), len(u))

    def test_two_models_unique_ids(self):
        x1 = BaseModel()
        x2 = BaseModel()
        self.assertNotEqual(x1.id, x2.id)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), storage.all().values())

    def test_ContainsCreated_at(self):
        """Checks if (created_at) exists"""
        x = BaseModel()
        self.assertTrue(hasattr(x, "created_at"))

    def test_Created_atInstance(self):
        """Checks for (created_at) type"""
        x = BaseModel()
        self.assertIsInstance(x.created_at, datetime)

    def test_ContainsUpdated_at(self):
        """Checks if (updated_at) exists"""
        x = BaseModel()
        self.assertTrue(hasattr(x, "updated_at"))

    def test_Updated_atInstance(self):
        """Checks for (updated_at) type"""
        x = BaseModel()
        self.assertIsInstance(x.updated_at, datetime)

    def test_datetime_created(self):
        """Tests if updated_at & created_at are current at creation."""
        date_now = datetime.now()
        x = BaseModel()
        diff = x.updated_at - x.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = x.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        x1 = BaseModel()
        x1.id = "123456"
        x1.created_at = x1.updated_at = dt
        x1str = x1.__str__()
        self.assertIn("[BaseModel] (123456)", x1str)
        self.assertIn("'id': '123456'", x1str)
        self.assertIn("'created_at': " + dt_repr, x1str)
        self.assertIn("'updated_at': " + dt_repr, x1str)

    def test_args_unused(self):
        x1 = BaseModel(None)
        self.assertNotIn(None, x1.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        x1 = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(x1.id, "345")
        self.assertEqual(x1.created_at, dt)
        self.assertEqual(x1.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        x1 = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(x1.id, "345")
        self.assertEqual(x1.created_at, dt)
        self.assertEqual(x1.updated_at, dt)

class TestBaseModel_Instance_Print(unittest.TestCase):
    """Unittest for testing the __str__ method."""

    def test_str_return(self):
        """Unittest for testing the return value of __str__ method."""
        x1 = BaseModel()
        Dika = "[{}] ({}) {}".format("BaseModel", x1.id, str(x1.__dict__))
        self.assertEqual(str(x1), Dika)

    def test_str(self):
        """test that the str method has the correct output"""
        x1 = BaseModel()
        string = "[BaseModel] ({}) {}".format(x1.id, x1.__dict__)
        self.assertEqual(string, str(x1))

    def test_of_str(self):
        """Tests for __str__ method."""
        x1 = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(x1))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), x1.id)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        d2 = x1.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)

class TestBaseModel_Save_Method(unittest.TestCase):
    """Unittest for testing the save method."""

    def test_validates_save(self):
        """Check save models"""
        x = BaseModel()
        updated_at_1 = x.updated_at
        x.save()
        updated_at_2 = x.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_one_save(self):
        x = BaseModel()
        sleep(0.05)
        first_updated_at = x.updated_at
        x.save()
        self.assertLess(first_updated_at, x.updated_at)

    def test_two_saves(self):
        x = BaseModel()
        sleep(0.05)
        first_updated_at = x.updated_at
        x.save()
        second_updated_at = x.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        x.save()
        self.assertLess(second_updated_at, x.updated_at)

    def test_save_with_arg(self):
        x = BaseModel()
        with self.assertRaises(TypeError):
            x.save(None)

class TestBaseModel_to_Dict_Method(unittest.TestCase):
    """Unittest for testing the to_dict method of the BaseModel class."""

    def test_className_present(self):
        """Test className present"""
        x = BaseModel()
        dic = x.to_dict()
        self.assertNotEqual(dic, x.__dict__)

    def test_attribute_ISO_format(self):
        """Test datetime field isoformated"""
        x1 = BaseModel()
        dic = x1.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)

    def test_to_dict_type(self):
        x = BaseModel()
        self.assertTrue(dict, type(x.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        x = BaseModel()
        self.assertIn("id", x.to_dict())
        self.assertIn("created_at", x.to_dict())
        self.assertIn("updated_at", x.to_dict())
        self.assertIn("__class__", x.to_dict())

    def test_to_dict_added_attrs(self):
        x = BaseModel()
        x.name = "Holberton"
        x.my_number = 98
        self.assertIn("name", x.to_dict())
        self.assertIn("my_number", x.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        x = BaseModel()
        x_dict = x.to_dict()
        self.assertEqual(str, type(x_dict["created_at"]))
        self.assertEqual(str, type(x_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        x = BaseModel()
        x.id = "123456"
        x.created_at = x.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(x.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        x = BaseModel()
        self.assertNotEqual(x.to_dict(), x.__dict__)

    def test_to_dict_with_arg(self):
        x = BaseModel()
        with self.assertRaises(TypeError):
            x.to_dict(None)


if __name__ == "__main__":
    unittest.main()