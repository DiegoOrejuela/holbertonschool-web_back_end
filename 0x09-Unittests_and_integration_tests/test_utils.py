#!/usr/bin/env python3.7
""" Suite test utils.py
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized, param


class TestAccessNestedMap(unittest.TestCase):
    """ Test Access Nested Map
    """

    @parameterized.expand([
        param(1, nested_map={"a": 1}, path=("a",)),
        param({"b": 2}, nested_map={"a": {"b": 2}}, path=("a",)),
        param(2, nested_map={"a": {"b": 2}}, path=("a", "b"))
    ])
    def test_access_nested_map(self, expected, nested_map, path):
        """ Test utils.access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        param(KeyError, nested_map={}, path=("a",)),
        param(KeyError, nested_map={"a": 1}, path=("a", "b"))
    ])
    def test_access_nested_map_exception(self, expected, nested_map, path):
        """ Test utils.access_nested_map with exception"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)
