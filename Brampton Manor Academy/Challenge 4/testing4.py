import unittest
from Challenge4 import *

class TestSum(unittest.TestCase):

    def test_windchill(self):
        self.assertEqual(calculate(3.5,18), -16.47884113003356)

if __name__ == '__main__':
    unittest.main()
