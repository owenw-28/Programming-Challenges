import unittest
from Challenge1 import *

class TestSum(unittest.TestCase):

    def test_metres(self):
        self.assertEqual(metres(10), 50.292)

if __name__ == '__main__':
    unittest.main()

