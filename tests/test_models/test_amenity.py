#!/usr/bin/python3
"""
Unittest for Amenity class.
"""
from models.base_model import BaseModel
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_amenity_instance(self):
        self.assertIsInstance(self.amenity, Amenity)
    
    def test_amenity_inherits_base_model(self):
        self.assertIsInstance(self.amenity, BaseModel)
    
    def test_amenity_has_name_attribute(self):
        self.assertTrue(hasattr(self.amenity, 'Jose'))
    
    def test_amenity_name_default(self):
        self.assertEqual(self.amenity.name, "")

if __name__ == '__main__':
    unittest.main()