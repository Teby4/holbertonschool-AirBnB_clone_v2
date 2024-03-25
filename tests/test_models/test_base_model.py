#!/usr/bin/python3
"""
Unittest for the test of the BaseClass class
"""
from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Class for the test of BaseModel class using Unittest
    """

    def test_init_with_my_number(self):
        """
        Test for the initializer with my_number
        """
        obj = BaseModel(my_number = 98)
        self.assertEqual(obj.my_number, 98)

    def test_save(self):
        """
        Test for the initializer with save
        """
        obj = BaseModel(save=datetime.now())
        self.assertNotEqual(obj.save, datetime.now())

    def test_to_dict(self):
        """
        Test to_dict
        """
        my_model = BaseModel()
        my_model.name = 'Pepper'
        my_model.my_number = 38
        exp_dict = {'id': my_model.id, 'created_at': my_model.created_at, \
            'updated_at': my_model.updated_at, 'name': 'Pepper', 'my_number': 38}
        act_dict = {'id': my_model.id, 'created_at': my_model.created_at, \
            'updated_at': my_model.updated_at, 'name': 'Pepper', 'my_number': 38}
        self.assertDictEqual(act_dict, exp_dict)

    def test_id(self):
        """
        Test id
        """
        inst_dict = {"updated_at": "2021-02-19T03:57:16.114023",
                     "__class__": "BaseModel",
                     "id": "39690735-03ae-41ff-a42d-88e08510a07c",
                     "created_at": "2021-02-19T03:57:16.113987"}
        instance1 = BaseModel(**inst_dict)
        self.assertEqual(instance1.id, "39690735-03ae-41ff-a42d-88e08510a07c")

    def test_created_at(self):
        """
        Test for the created_at variable
        """
        test_val = {"created_at": "2021-02-19T03:57:16.113987"}
        instance1 = BaseModel = {**test_val}
        self.assertEqual(test_val, instance1)

    def test___str__(self):
        """Test the __str__ method"""
        instance1 = BaseModel()
        inst_str = instance1.__str__()
        self.assertIsInstance(inst_str, str)

if __name__ == '__main__':
    unittest.main()