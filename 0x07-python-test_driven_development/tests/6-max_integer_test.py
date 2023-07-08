#!/usr/bin/python3
""" Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty(self):
        # Test when given list is empty
        # This is equivalent self.assertTrue(a is b)
        self.assertIs(max_integer([]), None)
        self.assertIs(max_integer(), None)

    def test_equality(self):
        #Make sure type errors are raised when necessary
        self.assertEqual(max_integer([110,20,-34,55]), 110)
        self.assertEqual(max_integer([1,20,-34,55]), 55)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-5, -9, -2, -98]), -2)
        self.assertEqual(max_integer([34, 23, 98, 21]), 98)

if __name__ == "__main__":
    unittest.main(verbosity=2)
