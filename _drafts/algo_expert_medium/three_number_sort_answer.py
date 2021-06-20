

def threeNumberSort(array, order):
    '''
    0 과 0 을 swap 하는 경우가 발생한다. (first value 랑 fist value 를 swap 함)
    이걸 막자니 쓸 데 없이 if 가 늘어나고... 이게 최선이란 말인가?
    '''
    first_idx = 0
    second_idx = 0
    third_idx = len(array) - 1

    while second_idx <= third_idx:
        if array[second_idx] == order[1]:
            second_idx += 1
        elif array[second_idx] == order[0]:
            array[first_idx], array[second_idx] = array[second_idx], array[first_idx]
            first_idx += 1
            second_idx += 1
        elif array[second_idx] == order[2]:
            array[third_idx], array[second_idx] = array[second_idx], array[third_idx]
            third_idx -= 1

    return array

print(threeNumberSort([0,0,0,-1,-1,0,1,1], [0, 1, -1]))
print(threeNumberSort([], [0, 1, -1]))
# print(threeNumberSort([-2, -3, -3, -3, -3, -3, -2, -2, -3], [-2, -3, 0]))







# print(threeNumberSort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))