#!/usr/bin/env python3
'''module for testing utils.py'''


import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch


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

@parameterized.expand([
    ("http://example.com", {"payload": True}),
    ("http://holberton.io", {"payload": False}),
])
class TestGetJson(unittest.TestCase):

    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload):
        # Mock the get method of requests and set its return value
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload

            # Call the get_json function with the test_url
            result = get_json(test_url)

            # Assert that the mocked get method was called exactly once with test_url as argument
            mock_get.assert_called_once_with(test_url)

            # Assert that the output of get_json is equal to test_payload
            self.assertEqual(result, test_payload)

if  __name__ == '__main__':
    unittest.main()