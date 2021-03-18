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

    # TO DO:
    # cochran sample size formula
    # find sample size given confidence interval and width (unknown population std dev)
