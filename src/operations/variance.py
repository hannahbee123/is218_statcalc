def variance(values):
    values_mean = sum(values) / len(values)
    population_variance = sum([((x - values_mean) ** 2) for x in values]) / len(values)
    return population_variance
