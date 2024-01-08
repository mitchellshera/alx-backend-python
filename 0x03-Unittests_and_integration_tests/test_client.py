#!/usr/bin/env python3
'''Module for testing client.py'''

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    '''Class for testing GithubOrgClient'''

    @patch('client.get_json', return_value={'login': 'dummy_org', 'repos_url': 'https://api.github.com/orgs/dummy_org/repos'})
    def test_public_repos_url(self, mock_get_json):
        '''Test the _public_repos_url method of GithubOrgClient'''
        org_name = 'dummy_org'

        with patch.object(GithubOrgClient, 'org', return_value={'login': org_name}):
            client = GithubOrgClient(org_name)
            result = client._public_repos_url

        # Ensure org is called once
        client.org.assert_called_once()

        # Ensure get_json is called once with the expected argument
        mock_get_json.assert_called_once_with('https://api.github.com/orgs/dummy_org/repos')

        # Ensure the correct result is returned
        self.assertEqual(result, 'https://api.github.com/orgs/dummy_org/repos')

if __name__ == '__main__':
    unittest.main()
