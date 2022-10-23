import unittest
from Challenge5 import *

class TestSum(unittest):

    def TestCalculate1(self):
        self.assertNotTrue(calculate(666666, 1999998)) 

    def TestCalculate2(self):
        self.assertTrue(calculate(142857, 428571))

if __name__ == '__main__':
    unittest.main()

