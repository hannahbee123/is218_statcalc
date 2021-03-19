from src.random_generator import RandomGenerator
from src.calculator import Calculator


class PopulationSampling:
    def __init__(self):
        pass

    @staticmethod
    def simple_rand(self, lst):
        # this method selects 10 random values from a list using 5 as a seed
        random_generator = RandomGenerator()
        simple_random_sample = random_generator.rand_choices_seed(self, lst, 10, 5)
        return simple_random_sample

    @staticmethod
    def margin_error(self, lst):
        # this method finds the margin of error using a z value of 1.96
        # z value of 1.96 corresponds to a 95% confidence interval
        calculator = Calculator()
        std_dev = calculator.standard_dev(lst)
        n = len(lst)
        return 1.96 * (std_dev / calculator.square_root(n))

    @staticmethod
    def confidence_interval(self, lst):
        # this method prints the confidence interval of a list using a confidence interval of 95%
        # it displays the mean +/- the margin of error (i.e. the confidence interval)
        calculator = Calculator()
        std_dev = calculator.standard_dev(lst)
        n = len(lst)
        mean = calculator.mean(lst)
        margin_err = 1.96 * (std_dev / calculator.square_root(n))
        print('The confidence interval is' + mean + '+/-' + margin_err)

    @staticmethod
    def cochran_formula(self, lst, p):
        """
        This method returns the ideal sample size of a list using a confidence z-score of 1.96.
        Probability must be greater than 0 and less than 1. If not then the
        probability will be assumed to be 50 percent (i.e. p = 0.5)
        if the population is less than a 10,000 then the modified Cochran's formula for smaller populations
        will be instead
        """
        if p >= 1 or p <= 0:
            p = 0.5
        calculator = Calculator()
        std_dev = calculator.standard_dev(lst)
        n = len(lst)
        z = 1.96
        margin_err = z * (std_dev / calculator.square_root(n))
        n0 = round(((z ** 2)*p*(1-p))/(margin_err ** 2))
        if n < 10000:  # checks if the population is small
            return round(n0/(1+(n0-1/n)))
        else:
            return n0

    @staticmethod
    def confidence_width(self, width, p):
        """
        Finds sample size given confidence interval and width (unknown population std dev).
        Due to the lack of a standard dev, the confidence interval will be 95%
        """
        if p >= 1 or p <= 0:
            p = 0.5
        e = width/2
        z = 1.96
        return round(((z/e) ** 2) * (p * (1-p)))
