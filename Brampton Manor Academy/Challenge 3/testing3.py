import unittest
from Challenge3 import *

class TestSum(unittest.TestCase):

    def TestCalculation(self):
        self.assertEqual(calculation(15,72), 15)

if __name__ == '__main__':
    unittest.main()

