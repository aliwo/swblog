# triumph 20200821

def is_decreasing(array):
    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            return False
    return True


def is_increasing(array):
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            return False
    return True


def isMonotonic(array):
    if not array:
        return True
    if len(array) == 1:
        return True
    if array[0] >= array[1]:
        if is_decreasing(array):
            return True
    if array[0] <= array[1]:
        if is_increasing(array):
            return True
    return False


print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
# print(isMonotonic([-1, -5, -10, -1100, -900, -1101, -1102, -9001]))
