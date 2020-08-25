# triumph
from collections import deque


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def moveElementToEnd(array, toMove):
    to_start = deque()
    for i in reversed(range(0, len(array))):
        if array[i] == toMove:
            if to_start:
                swap(array, to_start.popleft(), i)
                to_start.append(i)
        else:
            to_start.append(i)

    return array



# print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 4], 2))
print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
# print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
