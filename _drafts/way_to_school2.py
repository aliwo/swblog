
# 테스트 1 2 3 10 은 통과하고, 나머지는 모두 시간초과하는 로직 완성.

class G:
    graph = {} # 상하좌우로만 움직일 수 있는 2 * 2 이상의 바둑판은 인접 리스트로 표현하기에 적합합니다.
    min_distance = 99999999
    cache = []


def find_all_paths(start, end, path=[]):
    '''
    path 는 앞으로의 탐색에 영향을 주지 않습니다.
    start 로 부터 시작해서 end 에 도달하는
    최단 거리 후보들을 리턴합니다.
    '''
    path = path + [start]

    if len(path) > G.min_distance:
        return [] # 현재까지 발견한 최단거리보다 길어지면 바로 포기합니다.
    if start == end:
        G.min_distance = len(path) if G.min_distance > len(path) else G.min_distance
        return [path]
    if G.graph[start] == set():
        return []
    paths = []
    for node in G.graph[start]:
        if node not in path:
            newpaths = find_all_paths(node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def make_graph(height, width):
    '''
    width * height 크기의 그래프를 만듭니다.
    key 는 문자열이며 세로 가로는 띄어쓰기로 구별합니다. 즉. '1 1' 이 첫번째 정점입니다.
    100 * 100 크기라면 마지막 정점은 '100 100' 입니다.
    '''
    G.graph = {f'{i} {j}': set() for i in range(1, height + 1) for j in range(1, width + 1)}

    for key, value in G.graph.items():
        i, j = key.split()
        i = int(i)
        j = int(j)

        for node in [f'{i -1} {j}', f'{i +1} {j}', f'{i} {j -1}', f'{i} {j +1}']: # 상하좌우
            if node in G.graph:
                value.add(node)
                G.graph[node].add(key)


def solution(m, n, puddles):
    answer = 0
    make_graph(n, m)
    for elem in puddles:
        G.graph[f'{elem[1]} {elem[0]}'] = [] # puddles 는 막다른 길로 만듭니다.

    paths = find_all_paths('1 1', f'{n} {m}') # 그래프를 3번 만들면 시간초과입니다. 그래프 만드는게 빡세네요.
    for path in paths:
        if len(path) == G.min_distance:
            answer += 1

    return answer

assert solution(4, 3, [[3, 2]]) == 4


