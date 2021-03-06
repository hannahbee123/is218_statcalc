import unittest

from src.calculator.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_is_zero_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    # def test_add_method_calculator(self):


    # def test_subtract_method_calculator(self):


    # def test_multiply_method_calculator(self):


    # def test_divide_method_calculator(self):


    # def test_square_method_calculator(self):


    # def test_square_root_method_calculator(self):


    # def test_mean_method_calculator(self):


    # def test_median_method_calculator(self):


    # def test_mode_method_calculator(self):


    # def test_std_dev_method_calculator(self):


    # def test_variance_method_calculator(self):


    # def test_z_score_method_calculator(self):



if __name__ == "__main__":
    unittest.main()