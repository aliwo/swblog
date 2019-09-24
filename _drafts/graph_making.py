from collections import defaultdict

graph = {
    'a': ['b'],
    'b': ['c'],
    'c': ['a']
} # 위상정렬 불가능한 그래프


# default dict 를 dfs 호출할 땐 주의해야 함. 회전 중에 없던 key 가 생겨버릴 수 있다.
# 현재 key a b c 가 존재하고, c 의 value 가 [d] 라고 하자. dfs 호출 중 default_dict[d] 에 접근하게 되고
# 이 때문에 default_dict 의 length 가 회전 중에 바뀌게 된다. -> 이는 런타임 에러로 이어짐.

def dfs(visited, node):
    visited.append(node)
    for elem in graph[node]:
        if elem not in visited:
            dfs(visited, elem)


def topology_sort():
    '''
    전역변수 graph 와 올바르게 정의된 함수 dfs 에 의존합니다.
    :return:
    '''
    visited = []
    topology = []
    anchor = 0
    for key, value in graph.items():
        if key not in visited:
            dfs(visited, key)
            topology.append(visited[anchor:])
            anchor = len(visited)
    return [elem for i in reversed(range(len(topology))) for elem in topology[i]]


def find_difference(a, b):
    '''
    a 와 b가 똑같은 경우는 주어지지 않는다고 가정합니다.
    '''
    for chr_a, chr_b in zip(a, b):
        if chr_a != chr_b:
            return chr_a, chr_b


def solution(words) -> str:
    for i in range(len(words) - 1):
        a, b = find_difference(words[i], words[i+1])
        graph[a].append(b) # 방향 그래프를 형성합니다.
        graph[b] # b 가 없으면 b 를 생성해 줍니다. (default dict 의 특성 때문)

    return ''.join(topology_sort())

print(topology_sort())
# assert 'ogklh' in solution(['gg', 'kia', 'lotte', 'lg', 'hanhwa'])


