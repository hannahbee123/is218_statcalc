
class ZScore:
    result = 0

    def __init__(self):
        pass

    @staticmethod
    def z_score(self, values, a):
        values_mean = sum(values) / len(values)
        standard_dev = (sum([((x - values_mean) ** 2) for x in values]) / len(values)) ** 0.5
        self.result = (a - values_mean) / round(standard_dev, 6)
        return round(self.result, 6)
