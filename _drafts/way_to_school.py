import sys

sys.setrecursionlimit(20000)

cache = {} # 세상에... move 가 리턴을 하는 함수가 아니라서 cache 를 못해!


class G:  # Global
    field = []
    shortest_distance = 100 * 100  # 그냥 큰 수로 초기화
    paths = 0
    m = 0
    n = 0


def move(n, m, distance, visited=[]):
    '''
    TODO: 한 번 방문한 정점은 다시 방문하지 못하게 해야 함.
    '''
    if distance > G.shortest_distance:
        return

    if G.m == m + 1 and G.n == n + 1:
        if distance < G.shortest_distance:
            G.shortest_distance = distance
            return 1
        elif distance == G.shortest_distance:
            pass # ?
        return  # 최단 거리가 아님.

    if n < 0 or n >= G.n:
        return

    if m < 0 or m >= G.m:
        return

    node = f'{n}{m}'
    if node in visited:
        return

    if G.field[n][m] == 0:
        return

    visited = visited + [node]
    move(n - 1, m, distance + 1, visited=visited)
    move(n + 1, m, distance + 1, visited=visited)
    move(n, m - 1, distance + 1, visited=visited)
    move(n, m + 1, distance + 1, visited=visited)  # 상하좌우


def solution(m, n, puddles):
    G.m, G.n = m, n

    G.field = [[1 for _ in range(m)] for _ in range(n)]

    for elem in puddles:
        G.field[elem[1] - 1][elem[0] - 1] = 0

    move(0, 0, 0)

    return G.paths
