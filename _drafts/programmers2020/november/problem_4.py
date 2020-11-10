import sys
sys.setrecursionlimit(99999)
from collections import defaultdict


class G:
    graph = defaultdict(lambda: [])


def dfs(v_once, v_twice, node):
    print(f'node: {node} 방문')
    if node in v_once:
        v_twice.add(node)
    else:
        v_once.add(node)
    for elem in G.graph[node]:
        if elem not in v_twice:
            dfs(v_once, v_twice, elem)


def solution(t):
    max_hamil = 0
    # 그래프 형성
    for i, j in t:
        G.graph[i].append(j)
        G.graph[j].append(i)

    for i in G.graph.keys():
        v_once = set()
        v_twice = set()
        print('---------- root dfs ---------')
        dfs(v_once, v_twice, i)
        max_hamil = max(max_hamil, len(v_once.union(v_twice)))
    return max_hamil



# print(solution([[5,1], [2,5], [3,5], [3,6], [2,4], [4,0]]))
print(solution([[2,5],[2,0],[3,2],[4,2],[2,1]]))