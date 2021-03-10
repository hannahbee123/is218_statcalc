
class Median:
    result = 0

    def __init__(self):
        pass

    @staticmethod
    def median(self, values):
        sorted_values = values.sort()  # sorts values numerically
        length = len(values)
        if (length % 2) == 0:  # checks if amount of values is even
            self.result = ((sorted_values[length / 2]) + (sorted_values[(length / 2) - 1])) / 2
            return self.result
        else:
            self.result = sorted_values[(length / 2) - 1.5]
            return self.result
