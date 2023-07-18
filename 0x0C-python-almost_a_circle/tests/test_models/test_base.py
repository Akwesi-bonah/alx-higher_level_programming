#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBase_instantiation
    TestBase_to_json_string
    TestBase_save_to_file
    TestBase_from_json_string
    TestBase_create
    TestBase_load_from_file
    TestBase_save_to_file_csv
    TestBase_load_from_file_csv
    """

import os
import unittest
from models.base import Base

class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)



if __name__ == "__main__":
    unittest.main()
