
# 그냥 정렬을 쓰면 이렇게 쉽게 풀린다.
# def threeNumberSort(array, order):
#     table = {elem: i for i, elem in enumerate(order)}
#     return sorted(array, key=lambda x: table.get(x))


def find_first(array, start_index, number):
    for i in range(start_index, len(array)):
        if array[i] == number:
            return i
    return -1


def find_last(array, end_index, number):
    for i in reversed(range(0, end_index)):
        if array[i] == number:
            return i
    return -1


# assert find_first([1,1,1], 0, 1) == 0
# assert find_first([1,0,1], 0, 1) == 0
# assert find_first([1,0,1], 1, 1) == 2
# assert find_first([0,1,-1], 0, 1) == 1
# assert find_first([-1,-1,1], 0, 1) == 2
#
# assert find_last([1,1,0], 2, 1) == 1
# assert find_last([1,1,1], 2, 1) == 2
# assert find_last([1,1,1], 1, 1) == 1

def threeNumberSort(array, order):
    last_zero = find_last(array, len(array), order[0])

    first_one = find_first(array, 0, order[1])
    last_one = find_last(array, len(array), order[1])

    first_two = find_first(array, 0, order[2])

    if last_zero != -1:
        if first_one != -1:
            while last_zero > first_one:
                array[last_zero], array[first_one] = array[first_one], array[last_zero]
                if last_zero > last_one:
                    last_one = last_zero
                last_zero = find_last(array, last_zero, order[0])
                first_one = find_first(array, first_one, order[1])
        elif first_two != -1:
            while last_zero > first_two:
                array[last_zero], array[first_two] = array[first_two], array[last_zero]
                last_zero = find_last(array, last_zero, order[0])
                first_two = find_first(array, first_two, order[2])

    if first_two != -1:
        if last_one != -1:
            while first_two < last_one:
                array[last_one], array[first_two] = array[first_two], array[last_one]
                last_one = find_last(array, last_one, order[1])
                first_two = find_first(array, first_two, order[2])
        elif last_zero != -1:
            while first_two < last_zero:
                array[last_zero], array[first_two] = array[first_two], array[last_zero]
                last_zero = find_last(array, last_zero, order[1])
                first_two = find_first(array, first_two, order[2])

    return array

print(threeNumberSort([7, 8, 9, 7, 8, 9, 9, 9, 9, 9, 9, 9], [8,7,9]))