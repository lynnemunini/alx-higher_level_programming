#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class named TestMaxInteger is defined as a subclass of
    unittest.TestCase
    """
    def test_list_has_items(self):
        """
        test_list_has_items is a method. Calls max_integer with
        an empty list and verifies if None is returned
        """
        max_value = max_integer([])
        self.assertIsNone(max_value)

    def test_returns_max(self):
        """
        test_return_max checks whether the the max integer is 
        returned given valid inputs
        """
        max_value = max_integer([2, 7, 9])
        expected = 9
        self.assertEqual(max_value, expected)
