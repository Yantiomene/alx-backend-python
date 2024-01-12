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
from utils import access_nested_map


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
