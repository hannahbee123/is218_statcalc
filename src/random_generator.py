# random generator class
'''
functions:
1. Generate a random number without a seed between a range of two numbers -- both integer and decimal
2. Generate a random number with a seed between a range of two numbers -- both integer and decimal
3. Generate a list of N random numbers with a seed and between a range of numbers -- both integer and decimal
4. Select a random number from a list
5. Set a seed and randomly select the same value from a list
6. Select N number of items from a list without a seed
7. Select N number of items from a list with a seed
'''
import random


def rand(a, b):
    return random.randrange(a, b)


def rand_seed(a, b, seed):
    random.seed(seed)
    return random.randrange(a, b)


def rand_list(a, b, n, seed):
    random.seed(seed)
    random_list = []
    for value in range(n):
        random_list.append(random.randrange(a, b))
    return random_list


def rand_choice(lst):
    return random.choice(lst)


def rand_choice_seed(lst, seed):
    random.seed(seed)
    return random.choice(lst)


def rand_choices(lst, n):
    return random.choices(lst, k=n)


def rand_choices_seed(lst, n, seed):
    random.seed(seed)
    return random.choices(lst, k=n)
