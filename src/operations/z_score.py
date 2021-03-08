def find_z(values, a):
    values_mean = sum(values) / len(values)
    standard_dev = (sum([((x - values_mean) ** 2) for x in values]) / len(values)) ** 0.5
    return (a-values_mean) / standard_dev
