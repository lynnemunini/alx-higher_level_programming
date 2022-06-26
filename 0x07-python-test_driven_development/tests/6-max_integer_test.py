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

    def test_negative_values(self):
        """
        test the function given negative integers as input
        """
        max_value = max_integer([-1, 0, -5])
        expected = 0
        self.assertEqual(max_value, expected)

    def test_same_values(self):
        """
        test the function given similar values
        """
        max_value = max_integer([1, 1])
        expected = 1
        self.assertEqual(max_value, expected)

    def test_string_values(self):
        """
        test the function given string values
        """
        self.assertRaises(TypeError, max_integer, [1, "girl", "yes"])

    def test_float_values(self):
        """
        test the function given floating point values
        """
        max_value = max_integer([1.7, 2.2])
        expected = 2.2
        self.assertEqual(max_value, expected)

    def test_list(self):
        """
        test the function given a list as input
        """
        self.assertRaises(TypeError, max_integer, [1, [2, 3, 6]])
