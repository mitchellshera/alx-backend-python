#!/usr/bin/env python3
'''Module for testing client.py'''

import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized, parameterized_class
from requests import HTTPError
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Tests the `GithubOrgClient` class."""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org, resp, mocked_fxn):
        """Tests the `org` method."""
        mocked_fxn.return_value = MagicMock(return_value=resp)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_fxn.assert_called_once_with(
            f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self):
        """Tests the `_public_repos_url` property."""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos"}
            self.assertEqual(GithubOrgClient("google")._public_repos_url,
                             "https://api.github.com/users/google/repos")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Tests the `public_repos` method."""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {"login": "google", "id": 1342004},
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            result = GithubOrgClient("google").public_repos()
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()
        self.assertEqual(result, ["episodes.dart"])

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo, key, expected):
        """Tests the `has_license` method."""
        gh_org_client = GithubOrgClient("google")
        result = gh_org_client.has_license(repo, key)
        self.assertEqual(result, expected)


@parameterized_class([
    {'org_payload': TEST_PAYLOAD[0][0], 'repos_payload': TEST_PAYLOAD[0][1],
     'expected_repos': TEST_PAYLOAD[0][2], 'apache2_repos': TEST_PAYLOAD[0][3]}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Performs integration tests for the `GithubOrgClient` class."""

    @classmethod
    def setUpClass(cls):
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return MagicMock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self):
        """Tests the `public_repos` method."""
        result = GithubOrgClient("google").public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """Tests the `public_repos` method with a license."""
        result = GithubOrgClient("google").public_repos(license="apache-2.0")
        self.assertEqual(result, self.apache2_repos)

    @classmethod
    def tearDownClass(cls):
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
