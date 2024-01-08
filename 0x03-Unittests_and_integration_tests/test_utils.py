#!/usr/bin/env python3
'''module for testing utils.py'''


import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
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

class TestMemoize(unittest.TestCase):
    """Test case for the `memoize` decorator."""

    class TestClass:
        """Test class for memoized methods."""
        
        def a_method(self):
            """A method returning the constant value 42."""
            return 42

        @memoize
        def a_property(self):
            """A memoized property using the `memoize` decorator."""
            return self.a_method()

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_a_method):
        """Test the behavior of the memoized property."""
        test_instance = self.TestClass()

        # Call a_property twice
        result1 = test_instance.a_property
        result2 = test_instance.a_property

        # Assert that a_method is only called once
        mock_a_method.assert_called_once()

        # Assert that the correct result is returned
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)


if  __name__ == '__main__':
    unittest.main()