import unittest
from calculator import Calculator

class TestOprations(unittest.TestCase):

    def test_sum(self):
        calculation = Calculator(2,2)
        self.assertEqual(calculation.get_sum(), 4, "The answer is not 4!!")

    def test_difference(self):
        calculation = Calculator(6,2)
        self.assertEqual(calculation.get_difference(), 4, "The answer is not 4!!")

    def test_product(self):
        calculation = Calculator(2,2)
        self.assertEqual(calculation.get_product(), 4, "The answer is not 4!!")

    def test_quotient(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.get_quotient(), 4, "The answer is not 4!!")

if __name__== "__main__":

    unittest.main()