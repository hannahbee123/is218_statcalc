import random


def rand(a, b):   # generate random number without a seed between range of two numbers
    return random.randrange(a, b)


def rand_seed(a, b, seed):   # generate random number with seed between range of two numbers
    random.seed(seed)
    return random.randrange(a, b)


def rand_list(a, b, n, seed):   # generate list of n random numbers with seed and between range of numbers
    random.seed(seed)
    random_list = []
    for value in range(n):
        random_list.append(random.randrange(a, b))
    return random_list


def rand_choice(lst):   # select random number from list
    return random.choice(lst)


def rand_choice_seed(lst, seed):   # set a seed and randomly select the same value from a list
    random.seed(seed)
    return random.choice(lst)


def rand_choices(lst, n):   # select N number of items from a list without a seed
    return random.choices(lst, k=n)


def rand_choices_seed(lst, n, seed):   # select N number of items from a list with a seed
    random.seed(seed)
    return random.choices(lst, k=n)
