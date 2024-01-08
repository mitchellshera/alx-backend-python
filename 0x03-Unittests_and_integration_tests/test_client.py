#!/usr/bin/env python3
'''module for testing client.py'''


import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @patch('client.get_json', return_value={'login': 'dummy_org'})
    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    def test_org(self, org_name):
        with patch('client.get_json', return_value={'login': org_name}):
            client = GithubOrgClient(org_name)
            result = client.org()

        # Ensure get_json is called once with the expected argument
        client.get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name))

        # Ensure the correct result is returned
        self.assertEqual(result, {'login': org_name})


if __name__ == '__main__':
    unittest.main()
