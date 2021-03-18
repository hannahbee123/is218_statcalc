import unittest

from src.random_generator import RandomGenerator


class RandomGeneratorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.random_generator = RandomGenerator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.random_generator, RandomGenerator)

    def test_random_number_without_seed(self):
        random_generator = RandomGenerator()
        print(random_generator.rand(self, 0, 100))

    def test_random_number_with_seed(self):
        random_generator = RandomGenerator()
        random_number = random_generator.rand_seed(self, 0, 100, 10)
        self.assertEqual(random_generator.rand_seed(self, 0, 100, 10), random_number)

    def test_random_list_with_seed(self):
        random_generator = RandomGenerator()
        random_list = random_generator.rand_list(self, 0, 100, 10, 5)
        self.assertEqual(random_generator.rand_list(self, 0, 100, 10, 5), random_list)

    def test_random_choice_without_seed(self):
        random_generator = RandomGenerator()
        values = [5, 19, 27, 10, 12, 67]
        random_choice = random_generator.rand_choice(self, values)
        print(random_choice)

    def test_random_choice_with_seed(self):
        random_generator = RandomGenerator()
        values = [6, 20, 28, 11, 13, 68]
        random_choice = random_generator.rand_choice_seed(self, values, 5)
        self.assertEqual(random_generator.rand_choice_seed(self, values, 5), random_choice)

    def test_random_choices_without_seed(self):
        random_generator = RandomGenerator()
        values = [7, 21, 29, 12, 14, 69]
        random_choices = random_generator.rand_choices(self, values, 3)
        print(random_choices)

    def test_random_choices_with_seed(self):
        random_generator = RandomGenerator()
        values = [8, 22, 30, 13, 15, 70]
        random_choices = random_generator.rand_choices_seed(self, values, 4, 7)
        self.assertEqual(random_generator.rand_choices_seed(self, values, 4, 7), random_choices)