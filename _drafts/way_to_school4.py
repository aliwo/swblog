import sys
sys.setrecursionlimit(30000)

# 2019-10-02 오전 11시. 어젯밤 떠오른 아이디어를 써서 효율성 테스트 반타작 까지는 왔따!!
# 2019-10-03 오후 2시 드디어 정답.
'''
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.8MB)
테스트 2 〉	통과 (0.09ms, 10.8MB)
테스트 3 〉	실패 (런타임 에러)
테스트 4 〉	실패 (런타임 에러)
테스트 5 〉	실패 (런타임 에러)
테스트 6 〉	실패 (런타임 에러)
테스트 7 〉	실패 (런타임 에러)
테스트 8 〉	통과 (0.60ms, 10.8MB)
테스트 9 〉	실패 (런타임 에러)
테스트 10 〉	실패 (런타임 에러)
효율성  테스트
테스트 1 〉	통과 (17.43ms, 11.7MB)
테스트 2 〉	통과 (7.10ms, 11.2MB)
테스트 3 〉	통과 (8.87ms, 11.3MB)
테스트 4 〉	통과 (14.06ms, 11.6MB)
테스트 5 〉	통과 (10.45ms, 11.4MB)
테스트 6 〉	통과 (17.68ms, 11.8MB)
테스트 7 〉	실패 (런타임 에러)
테스트 8 〉	통과 (13.80ms, 11.7MB)
테스트 9 〉	실패 (런타임 에러)
테스트 10 〉	통과 (13.21ms, 11.6MB)
'''


class G:
    max = 99999999
    max_x = 0
    max_y = 0
    cache = {}
    field = None


def retrieve(y, x):
    if (y >= 0 and x >= 0) and (len(G.field) > y) and (len(G.field[y]) > x):
        return G.field[y][x]
    return G.max


def move(y, x):
    '''
    상하 좌우를 탐색. 모든 min 값을 재귀호출
    '''
    if (G.max_y < y) or y < 0:
        return 0
    if (G.max_x < x) or x < 0:
        return 0

    key = f'{y} {x}'

    # 학교에 도착한 경우
    if y == G.max_y and x == G.max_x:
        return 1
    if key in G.cache:
        return G.cache[key]

    up = retrieve(y - 1, x)
    down = retrieve(y + 1, x)
    left = retrieve(y, x - 1)
    right = retrieve(y, x + 1)
    min_value = min(up, down, left, right)

    if min_value == G.max:
        return 0
    if min_value > G.field[y][x]:
        return 0

    result = 0

    if up == min_value:
        result += move(y - 1, x)
    if down == min_value:
        result += move(y + 1, x)
    if left == min_value:
        result += move(y, x - 1)
    if right == min_value:
        result += move(y, x + 1)

    G.cache[key] = result
    return result


def solution(m, n, puddles):
    G.max_x, G.max_y = m - 1, n - 1
    G.field = [[j for j in reversed(range(i + 1 - m, i + 1))] for i in reversed(range(m - 1, m + n - 1))]

    for puddle in puddles:
        G.field[puddle[1] - 1][puddle[0] - 1] = G.max

    return move(0, 0) % 1000000007

# print(solution(4,	3,	[[2, 2]]))
# print(solution(4,	5,	[[2, 2]]))
# print(solution(100, 100, [[2, 2]]))
print(solution(100, 100, []))
# print(solution(100, 100, [[2, 3], [3, 5], [6, 7]]))
# print(solution(1, 100, []))
# print(solution(100, 1, []))
# print(solution(100, 2, []))
