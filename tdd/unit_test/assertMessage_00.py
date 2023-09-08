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
    
    def testPass(self):
        self.assertTrue(True, 'this is a Pass message')
        return
    def testFail(self):
        self.assertFalse(False, 'this is a failed message')
    def testError(self):
        raise RuntimeError('Test error!')
    def testAssesrtTrue(self):
        self.assertTrue(True)
    def testAssertFalse(self):
        self.assertFalse(True)


"""
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

"""
