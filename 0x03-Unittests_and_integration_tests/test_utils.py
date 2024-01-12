#!/usr/bin/env python3
"""Module for testing the utils class methods
"""
import unittest
from typing import (
    Any,
    Mapping,
    Sequence,
    Dict,
    Callable,
)
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """ Class to implement test cases for accessNestedMap
    method
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected_output: Any):
        """ Test that the method returns what is it supposed to
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence,
                                         expected_output: Any):
        """ Test the KeyError exception
        """
        with self.assertRaises(expected_output) as context:
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """ Test cases for get_json method
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict):
        """ Test the get_json method
        """
        mock = Mock()
        mock.json.return_value = test_payload
        with patch('requests.get', return_value=mock):
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
