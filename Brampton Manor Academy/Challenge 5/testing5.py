import unittest
from Challenge5 import *

class TestSum(unittest.TestCase):

    def TestCalculate2(self):
        self.assertNotEqual(calculate(666666, 1999998), 1999998)

    def TestCalculate2(self):
        self.assertEqual(calulate(142587, 427761), 427761)
        
if __name__ == '__main__':
    unittest.main()

