import unittest
from CT1 import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """@brief Creates a class object Calculator()
        """
        self.calculator = Calculator()

    # Each test method starts with the keyword test_
    def test_add(self):
        """@briefChecks the method add()
        """
        self.assertEqual(self.calculator.add(4, 7), 11)

    def test_subtract(self):
        """@briefChecks the method subtract()
        """
        self.assertEqual(self.calculator.subtract(10, 5), 5)

    def test_multiply(self):
        """@brief Checks the method multiply()
        """
        self.assertEqual(self.calculator.multiply(3, 7), 21)

    def test_divide(self):
        """@briefChecks the method divide()
        """
        self.assertEqual(self.calculator.divide(10, 2), 5)


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
