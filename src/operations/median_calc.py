def find_median(values):
    sorted_values = values.sort()  # sorts values numerically
    length = len(values)
    if (length % 2) == 0:  # checks if amount of values is even
        return ((sorted_values[length/2])+(sorted_values[(length/2)-1])) / 2
    else:
        return sorted_values[(length/2) - 1.5]
