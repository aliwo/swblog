import sys
sys.setrecursionlimit(99999999)
from collections import defaultdict
from itertools import combinations


class G:
    graph = defaultdict(lambda: [])


def dfs(visited, max_node, node):
    # print(f'node: {node} 방문')
    visited._add(node)
    max_node += 1
    max_node_temp = max_node

    visitable_nodes = list(filter(lambda x: x not in visited, G.graph[node]))
    if len(visitable_nodes) == 1:
        max_node = dfs(visited, max_node, visitable_nodes[0])
    else:
        for elem1, elem2 in combinations(visitable_nodes, 2):
            visited_temp = set(visited)
            # print(f'{node} 에서 {elem1}, {elem2} 를 뽑았습니다.')
            max_node = max(dfs(visited_temp, 0, elem1) + dfs(visited_temp, 0, elem2) + max_node_temp, max_node)
            # print(f'max_node: {max_node}')

    return max_node


def solution(t):
    max_hamil = 0
    # 그래프 형성
    for i, j in t:
        G.graph[i].append(j)
        G.graph[j].append(i)

    for i in G.graph.keys():
        # print('----------- root dfs -------------')
        temp = dfs(set(), 0, i)
        # print(f'리턴 {temp}')
        max_hamil = max(temp, max_hamil)

    return max_hamil



# print(solution([[5,1], [2,5], [3,5], [3,6], [2,4], [4,0]]))
print(solution([[2,5],[2,0],[3,2],[4,2],[2,1]]))