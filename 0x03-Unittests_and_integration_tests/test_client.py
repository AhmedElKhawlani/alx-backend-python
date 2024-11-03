#!/usr/bin/env python3

"""
Unit tests with parameterization and patching decorators for GithubOrgClient
"""

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests for GithubOrgClient class methods
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the expected value
        for each organization name
        """
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(
            test_client.ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        """
        Test that GithubOrgClient.public_repos_url returns the correct URL
        based on the mocked org property
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "something"}
            test_client = GithubOrgClient('test')
            result = test_client._public_repos_url
            self.assertEqual(result, "something")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that GithubOrgClient.public_repos returns a list of repository
        names based on the payload
        """
        mock_get_json.return_value = [{"name": "google"}, {"name": "Twitter"}]

        with patch('client.GithubOrgClient._public_repos_url',
                   return_value="mock_url"):
            test_client = GithubOrgClient('test')
            result = test_client.public_repos()
            expected = ["google", "Twitter"]
            self.assertEqual(result, expected)

            mock_get_json.assert_called_once()
            patch('client.GithubOrgClient._public_repos_url'
                  ).assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that GithubOrgClient.has_license checks for the correct
        license key in a repo
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient using pre-configured test data
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up mock for requests.get before integration tests
        """
        config = {"return_value.json.side_effect": [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]}
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repo(self):
        """
        Integration test for public_repo method
        """
        test_client = GithubOrgClient('Google')
        self.assertEqual(test_client.org, self.org_payload)
        self.assertEqual(test_client.repos_payload, self.repos_payload)
        self.assertEqual(test_client.public_repos(), self.expected_repos)
        self.assertEqual(test_client.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """
        Integration test for filtering public repos by license
        """
        test_client = GithubOrgClient("google")
        self.assertEqual(test_client.public_repos(), self.expected_repos)
        self.assertEqual(test_client.public_repos("XLICENSE"), [])
        self.assertEqual(test_client.public_repos("apache-2.0"),
                         self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """
        Stop patcher after integration tests
        """
        cls.get_patcher.stop()
