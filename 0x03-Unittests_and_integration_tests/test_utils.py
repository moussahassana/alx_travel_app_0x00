#!/usr/bin/env python3

import unittest
from typing import Any, Dict, Tuple
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Dict[str, Any],
        path: Tuple[str, ...],
        expected: Any
    ) -> None:
        """Test access_nested_map with various inputs."""
        self.assertEqual(access_nested_map(nested_map, path), expected)


# test_utils.py

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json

class TestGetJson(unittest.TestCase):
    """
    Unit test class for the get_json function in utils.py.
    This class ensures that HTTP requests are mocked and that
    the function returns the correct payload from a fake HTTP response.
    """

    @parameterized.expand([
        # Each tuple contains:
        # - A descriptive test case name
        # - A test URL to pass to get_json
        # - The expected JSON payload to return
        ("example", "http://example.com", {"payload": True}),
        ("holberton", "http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, name, test_url, test_payload, mock_get):
        """
        Test that get_json returns the expected JSON payload without making real HTTP requests.

        Args:
            name (str): A name for the test case (used for readability in test reports)
            test_url (str): The URL passed to get_json
            test_payload (dict): The mocked JSON data to be returned by the .json() method
            mock_get (Mock): The patched version of requests.get
        """

        # Create a mock response with a .json() method returning test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function under test
        result = get_json(test_url)

        # Verify that requests.get was called once with the correct URL
        mock_get.assert_called_once_with(test_url)

        # Verify that the result matches the mocked payload
        self.assertEqual(result, test_payload)

if __name__ == "__main__":
    unittest.main()

