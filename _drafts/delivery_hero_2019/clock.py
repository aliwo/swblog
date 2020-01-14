from itertools import permutations


h_range = {'00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
            '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20', '21', '22', '23'}
m_range = {f'{i}{j}' for i in range(0, 6) for j in range(0, 10)}


def solution(A, B, C, D):
    result = set()
    all_time = {f'{h}{m}' for h in h_range for m in m_range}
    for elem in permutations([A, B, C, D]):
        time = f'{elem[0]}{elem[1]}{elem[2]}{elem[3]}'
        if time in all_time:
            result.add(time)
    return len(result)

# print(solution(1, 8, 3, 2))
# print(solution(2, 3, 3, 2))
# print(solution(7, 7, 7, 7)) # 0
# print(solution(2, 4, 2, 4)) # 2424,  안됨 -> 2442, 4224
print(solution(1, 2, 3, 4)) # 1234, 1243,
                            # 2134, 2143,
                            # 1324, 1342,
                            # 1423, 1432,
                            # 2314, 2341,

