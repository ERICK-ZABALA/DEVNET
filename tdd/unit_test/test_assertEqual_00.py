#!/usr/bin/python3

"""

Unit Test, on based method assert Equal compare two values
if that is correct is True than the value is False.

"""
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        one = 'a'
        two = 'a'
        self.assertEqual(one, two)

"""
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

"""
