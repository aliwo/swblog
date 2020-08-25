# 2개의 리스트에서 각각 하나의 integer 를 뽑아서 가장 작은 수를 만들어라
# 가장 작은 수를 만드는 조합 [integer_a, integer_b] 를 리턴할 것
# 리스트 안의 각 요소는 unique 하다.
# 정답은 항상 하나만 있다고 가정한다.

def sub(a, b):
    if a > b:
        return a - b
    return b - a

def smallestDifference(arrayOne, arrayTwo):
    '''
    정렬을 쓰는 순간 n log n 이 된다.
    양 쪽 리스트를 정렬할 때 얻을 수 있는 이득?

    정렬 안하고 접근하면?
    n1 이 array1 의 길이, n2가 array2의 길이라고 할 때
    최악의 경우 n1 * n2 만큼 계산한다.

    크고 작냐 여부가 아니라 0 과의 거리로 정렬한다면?
    '''
    arrayOne.sort()
    arrayTwo.sort()
    result = 999999
    x = y = 0
    answer_x = answer_y = 0
    while x < len(arrayOne) and y < len(arrayTwo):
        cur = abs(sub(arrayOne[x], arrayTwo[y]))
        if cur < result:
            result = cur
            answer_x, answer_y = x, y
        if arrayOne[x] > arrayTwo[y]:
            y += 1
        elif arrayOne[x] < arrayTwo[y]:
            x += 1
        else:
            return [arrayOne[x], arrayTwo[y]]
    return [arrayOne[answer_x], arrayTwo[answer_y]]

print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))