#!/usr/bin/env python3
'''Module for testing client.py'''

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized, parameterized_class
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''Class for testing GithubOrgClient'''

    @patch('client.get_json', return_value=repos_payload)
    @patch.object(GithubOrgClient, '_public_repos_url', return_value='https://api.github.com/orgs/dummy_org/repos')
    def test_public_repos(self, mock_repos_url, mock_get_json):
        '''Test the public_repos method of GithubOrgClient'''
        org_name = 'dummy_org'

        with patch.object(GithubOrgClient, 'org', return_value=org_payload):
            client = GithubOrgClient(org_name)
            result = client.public_repos()

        # Ensure org is called once
        client.org.assert_called_once()

        # Ensure _public_repos_url is called once
        mock_repos_url.assert_called_once()

        # Ensure get_json is called once with the expected argument
        mock_get_json.assert_called_once_with('https://api.github.com/orgs/dummy_org/repos')

        # Ensure the correct result is returned
        self.assertEqual(result, expected_repos)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        '''Test the has_license method of GithubOrgClient'''
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)

@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), [
    (org_payload, repos_payload, expected_repos, apache2_repos),
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Class for integration testing GithubOrgClient'''

    @classmethod
    def setUpClass(cls, org_payload, repos_payload, expected_repos, apache2_repos):
        '''Set up class for integration testing'''
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [
            MagicMock(json=lambda: org_payload),
            MagicMock(json=lambda: repos_payload),
            MagicMock(json=lambda: apache2_repos),
        ]

    @classmethod
    def tearDownClass(cls):
        '''Tear down class for integration testing'''
        cls.get_patcher.stop()

    def test_public_repos(self):
        '''Test public_repos method in integration'''
        client = GithubOrgClient('dummy_org')
        result = client.public_repos()

        # Ensure the correct result is returned
        self.assertEqual(result, expected_repos)

    def test_public_repos_with_license(self):
        '''Test public_repos method with license argument in integration'''
        client = GithubOrgClient('dummy_org')
        result = client.public_repos(license="apache-2.0")

        # Ensure the correct result is returned
        self.assertEqual(result, apache2_repos)


if __name__ == '__main__':
    unittest.main()
