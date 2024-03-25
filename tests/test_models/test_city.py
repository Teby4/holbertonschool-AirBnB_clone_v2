#!/bin/usr/python3
"""
Unittest for City class.
"""
import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    def test_city_instance(self):
        city = City()
        self.assertIsInstance(city, City)
    
    def test_city_inherits_base_model(self):
        city = City()
        self.assertIsInstance(city, BaseModel)
    
    def test_city_has_state_id_and_name_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
    
    def test_city_attributes_defaults(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == '__main__':
    unittest.main()