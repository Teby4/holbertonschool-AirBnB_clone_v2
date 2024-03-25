#!/bin/usr/python3
"""
Unittest for Review class.
"""
import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    def test_review_instance(self):
        review = Review()
        self.assertIsInstance(review, Review)
    
    def test_review_inherits_base_model(self):
        review = Review()
        self.assertIsInstance(review, BaseModel)
    
    def test_review_has_place_id_user_id_and_text_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
    
    def test_review_attributes_defaults(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

if __name__ == '__main__':
    unittest.main()