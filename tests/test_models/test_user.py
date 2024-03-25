#!/usr/bin/python3
"""
Unittest for User class.
"""
import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    def test_user_instance(self):
        user = User()
        self.assertIsInstance(user, User)
    
    def test_user_inherits_base_model(self):
        user = User()
        self.assertIsInstance(user, BaseModel)
    
    def test_user_has_all_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
    
    def test_user_attributes_defaults(self):
        user = User()
        self.assertEqual(user.email, "Pepito@gmail.com")
        self.assertEqual(user.password, "pepito123")
        self.assertEqual(user.first_name, "pepito")
        self.assertEqual(user.last_name, "De la rosa")

if __name__ == '__main__':
    unittest.main()