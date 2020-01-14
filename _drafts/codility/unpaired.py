
def solution(A):
    # write your code in Python 3.6
    cache = {}

    for elem in A:
        if elem in cache:
            del cache[elem]
        else:
            cache[elem] = True

    return list(cache.keys())[0]


print(solution([9, 3, 9, 3, 9, 7, 9]))
