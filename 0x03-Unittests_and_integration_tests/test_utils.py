#!/usr/bin/env python3

"""
Unit tests for utility functions with parameterized cases
"""

from parameterized import parameterized
import unittest
from unittest.mock import patch

from utils import (
    access_nested_map,
    get_json,
    memoize
)


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for the access_nested_map utility function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map returns the correct value given valid paths
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test access_nested_map raises KeyError for invalid paths
        """
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(err.exception))


class TestGetJson(unittest.TestCase):
    """
    Unit tests for the get_json utility function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test get_json fetches and returns JSON content from a given URL
        """

        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """
    Unit tests for the memoize decorator
    """

    def test_memoize(self):
        """
        Test memoize ensures a cached result on repeated calls to a_property,
        verifying a_method is called only once.
        """

        class TestClass:
            """
            Test class to validate memoize decorator functionality.
            """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
