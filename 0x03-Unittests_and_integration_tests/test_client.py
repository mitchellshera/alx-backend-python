#!/usr/bin/env python3
'''Module for testing client.py'''

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    '''Class for testing GithubOrgClient'''

    @patch('client.get_json', return_value={'login': 'dummy_org'})
    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    def test_org(self, org_name):
        '''Test the org method of GithubOrgClient'''
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
