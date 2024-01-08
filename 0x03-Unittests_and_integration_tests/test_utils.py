#!/usr/bin/env python3
'''module for testing utils.py'''


import unittest
from parameterized import parameterized
from utils import utils

class TestAccessNestedMap(unittest.TestCase):
    '''class for testing utils.py'''
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(utils.access_nested_map(nested_map, path), expected_result)

if __name__ == '__main__':
    unittest.main()
