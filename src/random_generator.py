import random


class RandomGenerator:
    def __init__(self):
        pass

    @staticmethod
    def rand(self, a, b):   # generate random number without a seed between range of two numbers
        return random.randrange(a, b)

    @staticmethod
    def rand_seed(self, a, b, seed):   # generate random number with seed between range of two numbers
        random.seed(seed)
        return random.randrange(a, b)

    @staticmethod
    def rand_list(self, a, b, n, seed):   # generate list of n random numbers with seed and between range of numbers
        random.seed(seed)
        random_list = []
        for value in range(n):
            random_list.append(random.randrange(a, b))
        return random_list

    @staticmethod
    def rand_choice(self, lst):   # select random number from list
        return random.choice(lst)

    @staticmethod
    def rand_choice_seed(self, lst, seed):   # set a seed and randomly select the same value from a list
        random.seed(seed)
        return random.choice(lst)

    @staticmethod
    def rand_choices(self, lst, n):   # select N number of items from a list without a seed
        return random.choices(lst, k=n)

    @staticmethod
    def rand_choices_seed(self, lst, n, seed):   # select N number of items from a list with a seed
        random.seed(seed)
        return random.choices(lst, k=n)
