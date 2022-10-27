import unittest
from Challenge8 import *

class TestSum(unittest.TestCase):

    def test_romanToDig1(self):
        self.assertEqual(romanToDig("XLIV"), 44)
        
    def test_romanToDig2(self):
        self.assertEqual(romanToDig("CCLXV"), 265)

if __name__ == '__main__':
    unittest.main()
