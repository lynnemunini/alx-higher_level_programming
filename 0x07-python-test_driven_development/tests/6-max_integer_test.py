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
        my_list = max_integer([])
        self.assertIsNone(my_list)
