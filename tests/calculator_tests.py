import unittest

from calculator import Calculator
from random_generator import RandomGenerator


class CalculatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_is_zero_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(2, 2), 0)
        self.assertEqual(calculator.result, 0)

    def test_multiply_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_divide_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(2, 2), 1)
        self.assertEqual(calculator.result, 1)
        self.assertRaises(ZeroDivisionError, calculator.divide, 1, 0)

    def test_square_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.square(2), 4)
        self.assertEqual(calculator.result, 4)

    def test_square_root_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.square_root(4), 2)
        self.assertEqual(calculator.result, 2)

    # def test_mean_method_calculator(self):

    # def test_median_method_calculator(self):

    # def test_mode_method_calculator(self):

    # def test_std_dev_method_calculator(self):

    # def test_variance_method_calculator(self):

    # def test_z_score_method_calculator(self):


if __name__ == "__main__":
    unittest.main()
