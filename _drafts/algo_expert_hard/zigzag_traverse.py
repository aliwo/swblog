def zigzagTraverse(array):
    '''
    순회가 종료된 시점에
    1. 아래로 내려갔다 우상향 (만약 막다른 골목이면 오른쪽으로 갔다가 우상향)
    2. 오른쪽으로 갔다가 좌하향 (만약 막다른 골목이면 아래로 내려갔다가 좌하향)

    막다른 골목이면 stuck == True
    '''

    if not array:
        return []
    if len(array) == 1:
        return array[0]


    result = [array[0][0]]
    result_len = len(array) * len(array[0])

    i = 0
    j = 0
    while len(result) < result_len:
        # 자리 잡고
        if i+1 < len(array):
            i += 1
        elif j <= len(array[i]):
            j += 1

        # 우상향
        while i >= 0 and j < len(array[i]):
            result.append(array[i][j])
            if i > 0 and j + 1 < len(array[i]):
                i -= 1
                j += 1
            else:
                break

        if len(result) == result_len:
            break

        # 자리 잡고
        if j+1 < len(array[i]):
            j += 1
        elif i+1 < len(array):
            i += 1

        # 좌하향
        while i >= 0 and j < len(array[i]):
            result.append(array[i][j])
            if j > 0 and i + 1 < len(array):
                i += 1
                j -= 1
            else:
                break

    return result

# print(zigzagTraverse([[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]))
# print(zigzagTraverse([[1]]))
# print(zigzagTraverse([[1], [2]]))
print(zigzagTraverse([[1, 3], [2, 4], [5, 7], [6, 8], [9, 10]]))







