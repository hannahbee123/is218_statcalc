# population sampling tests
import unittest

from src.random_generator import RandomGenerator
from src.population_sampling import PopulationSampling


class PopulationSamplingTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.random_generator = RandomGenerator()
        self.pop_sampling = PopulationSampling()

    def test_instantiate_pop_sampling(self):
        self.assertIsInstance(self.pop_sampling, PopulationSampling)

    def test_instantiate_rand_gen(self):
        self.assertIsInstance(self.random_generator, RandomGenerator)

    def test_simple_rand(self):
        test_list = self.random_generator.rand_list(self, 0, 10, 50, 3)
        result = self.pop_sampling.simple_rand(self, test_list, 10, 5)
        self.assertEqual(self.pop_sampling.simple_rand(self, test_list, 10, 5), result)
        test_list.clear()

    def test_margin_error(self):
        test_list = [4, 9, 3, 6, 8, 2, 1, 8, 5, 9]
        self.assertEqual(round(self.pop_sampling.margin_error(self, test_list), 6), 1.736564)
        test_list.clear()

    def test_confidence_interval(self):
        test_list = [4, 9, 3, 6, 8, 2, 1, 8, 5, 9]
        self.assertEqual(self.pop_sampling.confidence_interval(self, test_list), [7.236564, 3.763436])
        test_list.clear()

