#!/usr/bin/env python3
'''module for testing utils.py'''


import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock
from typing import Dict, Tuple, Union

class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ["a"], KeyError, "'a'"),
        ({"a": 1}, ["a", "b"], KeyError, "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception, expected_message):
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):
    '''class for testing get_json function'''
    
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """Tests `get_json`'s output."""
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as request_get:
            self.assertEqual(get_json(test_url), test_payload)
            request_get.assert_called_once_with(test_url)


if  __name__ == '__main__':
    unittest.main()