#!/usr/bin/env python3
"""
Unit tests for the client module.

This module contains the TestGithubOrgClient test case class,
which validates the behavior of the GithubOrgClient class,
including tests for organization retrieval and public repository listing.
"""
from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import PropertyMock, patch


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        expected = {"login": org_name, "id": 1}
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, expected)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns expected list
        of repo names and mocks are called"""
        # Given payload
        payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}},
        ]
        mock_get_json.return_value = payload

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_repos_url:
            mock_repos_url.return_value = "http://mocked.url"

            client = GithubOrgClient("my_org")
            result = client.public_repos()

            # Assertions
            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_get_json.assert_called_once_with("http://mocked.url")
            mock_repos_url.assert_called_once()
            
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),  # Optional: test without license key
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns the correct boolean value."""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
