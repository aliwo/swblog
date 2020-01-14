from timeit import timeit
from random import randint
K = [randint(1, 10) for _ in range(4)]
N =  [randint(1, 10) for _ in range(5)]


def mock_dict():
    cache1 = {}
    for k in K:
        for n in N:
            key = f'{k},{n}'
            if key in cache1:
                return cache1[key]
            cache1[key] = 1
            return cache1[key]


def mock_list():
    cache2 = [[-1 for j in range(11)] for x in range(11)]
    for k in K:
        for n in N:
            if cache2[k][n] != -1:
                return cache2[k][n]
            cache2[k][n] = 1
            return cache2[k][n]

print(timeit(mock_list)) # 11.6139617
print(timeit(mock_dict)) # 0.7821320000000007




