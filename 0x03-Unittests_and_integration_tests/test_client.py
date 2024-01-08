#!/usr/bin/env python3
'''Module for testing client.py'''

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    '''Class for testing GithubOrgClient'''

    @patch('client.get_json', return_value=[{'name': 'repo1'}, {'name': 'repo2'}])
    @patch.object(GithubOrgClient, '_public_repos_url', new_callable=unittest.PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        '''Test the public_repos method of GithubOrgClient'''
        org_name = 'dummy_org'

        # Set the return value for the mocked property
        mock_public_repos_url.return_value = 'https://api.github.com/orgs/dummy_org/repos'

        with patch.object(GithubOrgClient, 'org', return_value={'login': org_name}):
            client = GithubOrgClient(org_name)
            result = client.public_repos()

        # Ensure org is called once
        client.org.assert_called_once()

        # Ensure the mocked property is called once
        mock_public_repos_url.assert_called_once()

        # Ensure get_json is called once with the expected argument
        mock_get_json.assert_called_once_with('https://api.github.com/orgs/dummy_org/repos')

        # Ensure the correct result is returned
        self.assertEqual(result, ['repo1', 'repo2'])


if __name__ == '__main__':
    unittest.main()
