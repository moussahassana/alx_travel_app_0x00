#!/usr/bin/env python3
"""Unit tests for the utils module.

This module contains tests for utility functions such as `memoize`,
`access_nested_map`, and `get_json`.
"""

import unittest
from typing import Any, Dict, Tuple
from parameterized import parameterized
from unittest.mock import patch, Mock
import utils


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
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)


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
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that get_json returns the expected JSON payload "

        Args:
            test_url (str): The URL passed to get_json
            test_payload (dict): The mocked JSON data to be returned
            by the .json() method
            mock_get (Mock): The patched version of requests.get
        """

        # Create a mock response with a .json() method returning test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function under test
        result = utils.get_json(test_url)

        # Verify that requests.get was called once with the correct URL
        mock_get.assert_called_once_with(test_url)

        # Verify that the result matches the mocked payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test cases for the memoize utility decorator."""

    def test_memoize(self) -> None:
        """Test that a_method is only called once when memoized."""

        class TestClass:
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
            TestClass, 'a_method', return_value=42
        ) as mock_method:
            obj = TestClass()
            result1 = obj.a_property
            result2 = obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
