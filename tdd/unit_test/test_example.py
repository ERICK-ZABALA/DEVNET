#!/usr/bin/python3
#!/usr/bin/python3
"""

Unit Test, on based method assert Equal compare two values
if that is correct is True than the value is False.

"""
import unittest

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(4,4)
    def test_decrement(self):
        self.assertEqual(3,4)

if __name__ == '__main__':
    unittest.main()
    