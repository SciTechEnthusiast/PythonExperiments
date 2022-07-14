import unittest
from script import *

class TestScript(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10,20),30, "Addition of 10 and 20 should be 30")
    def test_sub(self):
        self.assertEqual(sub(50,20),30, "Subtraction of 50 and 20 should be 30")
    def test_multiply(self):
        self.assertEqual(mul(5,6),30, "Multiplication of 5 and 6 should be 30")
    def test_division(self):
        self.assertEqual(div(300,10),30, "Division of 300 and 10 should be 30")

    
if __name__ == '__main__':
    unittest.main()