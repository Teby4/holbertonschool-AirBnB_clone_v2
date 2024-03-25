#!/usr/bin/python3
"""
Unittest for State class.
"""
import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    def test_state_instance(self):
        state = State()
        self.assertIsInstance(state, State)
    
    def test_state_inherits_base_model(self):
        state = State()
        self.assertIsInstance(state, BaseModel)
    
    def test_state_has_name_attribute(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))
    
    def test_state_name_is_empty_string_by_default(self):
        state = State()
        self.assertEqual(state.name, "")
    
    def test_state_name_can_be_set(self):
        state = State()
        state.name = "Uruguay"
        self.assertEqual(state.name, "Uruguay")

if __name__ == '__main__':
    unittest.main()