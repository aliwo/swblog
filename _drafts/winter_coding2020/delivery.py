def solution(n, delivery):
    result = ['?' for _ in range(n + 1)]  # 0 번 index 는 버린다.

    for elem in delivery:
        if elem[2] == 1:
            result[elem[0]] = 'O'
            result[elem[1]] = 'O'

    for elem in delivery:
        if elem[2] == 0:
            if result[elem[0]] == 'O':
                result[elem[1]] = 'X'
            elif result[elem[1]] == 'O':
                result[elem[0]] = 'X'

    answer = ''.join(result)
    return answer[1:]


print(solution(6, [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]))
print(solution(7, [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]	))