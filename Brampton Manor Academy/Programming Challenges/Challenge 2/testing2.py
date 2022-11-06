import unittest
from Challenge2 import *

class TestSum(unittest.TestCase):

    def TestJoules(self):
        self.assertEqual(energy(3.4), 7943282347.242789)

    def TestTnt(self):
        self.assertEqual(tnt(3.4), 1.8984900447521007)
    

if __name__ == '__main__':
    unittest.main()
