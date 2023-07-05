#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class MyTestCase(unittest.TestCase):
    """Define unittest for max_integer"""
    def test_empty(self):
        """Test for empty string"""
        self.assertEqual(max_integer(""), None)

    def test_string(self):
        """Test for strings"""
        strings = "Bonnah"
        self.assertEqual(max_integer(strings), 'o')

    def test_empty_list(self):
        """Test for empty list"""
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_ordered_list(self):
        """Test for ordered list"""
        my_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(my_list), 4)

    def test_unordered_list(self):
        """Test for unordered list"""
        my_list = [1, 3, 4, 2]
        self.assertEqual(max_integer(my_list), 4)

    def test_max_value(self):
        """Test for max value"""
        my_list = [4, 1, 1, 4, 2]
        self.assertEqual(max_integer(my_list), 4)

    def test_single_value(self):
        """Test for list with single value"""
        my_list = [120]
        self.assertEqual(max_integer(my_list), 120)

    def test_list_of_float_values(self):
        """Test for list containing float values"""
        my_list = [1.4, 0.1, 3.4, 10.0]
        self.assertEqual(max_integer(my_list), 10.0)

    def test_list_of_integer_values(self):
        """Test for list containing integer values"""
        my_list = [10, 20, 30, 40, 50]
        self.assertEqual(max_integer(my_list), 50)

    def test_list_of_string_values(self):
        """Test of list containing string values"""
        my_list = ["Tommy", "Johnny", "Peterson", "Bonnah"]
        self.assertEqual(max_integer(my_list), 'Tommy')


if __name__ == '__main__':
    unittest.main()
