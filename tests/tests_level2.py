import unittest
from calculator import Calculator

class TestOprations(unittest.TestCase):

    def setUp(self):
        self.myCalc = Calculator(8,2)

    def test_sum(self):
        self.assertEqual(self.myCalc.get_sum(), 4, "The answer is not 4!!")

    def test_difference(self):
        self.assertEqual(self.myCalc.get_difference(), 4, "The answer is not 4!!")

    def test_product(self):
        self.assertEqual(self.myCalc.get_product(), 4, "The answer is not 4!!")

    def test_quotient(self):
        self.assertEqual(self.myCalc.get_quotient(), 4, "The answer is not 4!!")

if __name__== "__main__":

    unittest.main()