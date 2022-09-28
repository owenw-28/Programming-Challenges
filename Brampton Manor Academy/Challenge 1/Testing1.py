import unittest
from Challenge1 import *

class TestSum(unittest.TestCase):

    def test_metres(self):
        self.assertEqual(metres(10), 50.292)
        
    def test_feet(self):
        self.assertEqual(feet(10), 165.0)
        
    def test_miles(self):
        self.asserEqual(miles(10), 0.03125007767159208)
        
    def test_furlongs(self):
        self.assertEqual(furlong(10), 0.25)
    
    def test_time(self):
        self.assertEqual(time(10), 0.6048402129985564)

if __name__ == '__main__':
    unittest.main()

