from src.operations.addition import Addition
from src.operations.division import Division
from src.operations.multiplication import Multiplication
from src.operations.subtraction import Subtraction
from src.operations.square import Square
from src.operations.square_root import SquareRoot
from src.operations.mean import Mean
from src.operations.median import Median
from src.operations.std_dev import StandardDeviation
from src.operations.mode import Mode
from src.operations.variance import Variance
from src.operations.z_score import ZScore


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = Addition.add(self, a, b)
        return self.result

    def subtract(self, a, b):
        self.result = Subtraction.subtract(self, a, b)
        return self.result

    def multiply(self, a, b):
        self.result = Multiplication.multiply(self, a, b)
        return self.result

    def divide(self, a, b):
        self.result = Division.divide(self, a, b)
        return self.result

    def square(self, a):
        self.result = Square.square(self, a)
        return self.result

    def square_root(self, a):
        self.result = SquareRoot.square_root(self, a)
        return self.result

    def mean(self, values):
        self.result = Mean.mean(self, values)
        return self.result

    def median(self, values):
        self.result = Median.median(self, values)
        return self.result

    def mode(self, values):
        self.result = Mode.mode(self, values)
        return self.result

    def standard_dev(self, values):
        self.result = StandardDeviation.standard_deviation(self, values)
        return self.result

    def variance(self, values):
        self.result = Variance.variance(self, values)
        return self.result

    def z_score(self, values, a):
        self.result = ZScore.z_score(self, values, a)
        return self.result
