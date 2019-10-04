# 종만북에서 풀었던 문제. 삼각형 모양만 다르다.
# cache[i][j] 보다 f 스트링을 사용한 1중 dict 가 훨씬 빠르다.

cache = {}

class G:
    triangle = []


def move(i, j):
    '''
    현재 위치에서 내려갔을 떄 얻을 수 있는 최댓값을 반환합니다.
    '''
    key = f'{i} {j}'
    if key in cache:
        return cache[key]

    if i > len(G.triangle) - 1:
        return 0

    if j > len(G.triangle[i]) - 1:
        return 0

    cache[key] = max(G.triangle[i][j] + move(i + 1, j), G.triangle[i][j] + move(i + 1, j + 1))

    return cache[key]


def solution(triangle):
    G.triangle = triangle
    return move(0, 0)

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
