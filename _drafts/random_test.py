import random

def random_list(length, range_start, range_end, sorted=True):
    result = []
    for _ in range(length):
        result.append(random.randint(range_start, range_end))

    result.sort()
    return result

