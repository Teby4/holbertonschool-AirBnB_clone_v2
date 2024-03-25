#!/bin/usr/python3
"""
Unittest for Place class.
"""

import unittest
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_place_instance(self):
        self.assertIsInstance(self.place, Place)
    
    def test_place_inherits_base_model(self):
        self.assertIsInstance(self.place, BaseModel)
    
    def test_place_has_all_attributes(self):
        attributes = [
            'city_id', 'user_id', 'name', 'description', 
            'number_rooms', 'number_bathrooms', 'max_guest',
            'price_by_night', 'latitude', 'longitude', 'amenity_ids'
        ]
        for attr in attributes:
            self.assertTrue(hasattr(self.place, attr))
    
    def test_place_attributes_defaults(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

if __name__ == '__main__':
    unittest.main()