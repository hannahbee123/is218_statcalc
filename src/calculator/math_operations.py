from src.calculator.operations import addition
from src.calculator.operations import division
from src.calculator.operations import multiplication
from src.calculator.operations import square
from src.calculator.operations import square_root
from src.calculator.operations import subtraction
from src.calculator.operations import mean_calc
from src.calculator.operations import median_calc
from src.calculator.operations import mode_calc
from src.calculator.operations import std_dev
from src.calculator.operations import variance
from src.calculator.operations import z_score


class MathOperations:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def square_root(self, a):
        self.result = square_root(a)
        return self.result

    def mean_value(self, values):
        self.result = mean_calc(values)
        return self.result

    def median_value(self, values):
        self.result = median_calc(values)
        return self.result

    def mode_value(self, values):
        self.result = mode_calc(values)
        return self.result

    def standard_dev(self, values):
        self.result = std_dev(values)
        return self.result

    def variance_value(self, values):
        self.result = variance(values)
        return self.result

    def z_score_value(self, values):
        self.result = z_score(values)
        return self.result
