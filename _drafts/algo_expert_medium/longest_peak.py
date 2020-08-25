# 20200824 triumph


def left_length(array, tip):
    prev = array[tip]
    length = 0
    for i in reversed(range(0, tip)):
        if prev > array[i]:
            length += 1
            prev = array[i]
        else:
            return length
    return length


def right_length(array, tip):
    prev = array[tip]
    length = 0
    for i in range(tip+1, len(array)):
        if prev > array[i]:
            length += 1
            prev = array[i]
        else:
            return length
    return length


def longestPeak(array):
    max = 0
    for i in range(1, len(array)):
        left = left_length(array, i)
        right = right_length(array, i)
        if left and right:
            max = left + right + 1 if left + right + 1 > max else max
    return max


print(longestPeak([1,2,3,3,4,0,10,6,5,-1,-3,2,3]))