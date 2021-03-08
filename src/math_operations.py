



class MathOperations:
    result = 0

    def __init__(self):
        pass

    @staticmethod
    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    @staticmethod
    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    @staticmethod
    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    @staticmethod
    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    @staticmethod
    def square(self, a):
        self.result = square(a)
        return self.result

    @staticmethod
    def square_root(self, a):
        self.result = square_root(a)
        return self.result

    @staticmethod
    def mean_value(self, values):
        self.result = mean_calc(values)
        return self.result

    @staticmethod
    def median_value(self, values):
        self.result = median_calc(values)
        return self.result

    @staticmethod
    def mode_value(self, values):
        self.result = mode_calc(values)
        return self.result

    @staticmethod
    def standard_dev(self, values):
        self.result = std_dev(values)
        return self.result

    @staticmethod
    def variance_value(self, values):
        self.result = variance(values)
        return self.result

    @staticmethod
    def z_score_value(self, values):
        self.result = z_score(values)
        return self.result
