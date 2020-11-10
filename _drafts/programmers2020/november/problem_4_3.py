import sys
sys.setrecursionlimit(99999999)
from collections import defaultdict


class G:
    graph = defaultdict(lambda: set())
    memo = {}


def dfs(parent, node):
    '''
    parent 를 통해서 node 에 접근했을 때,
    이 node 에서 가장 자식이 많은 2개를 골라,
    1 (자신) + 자식 수 를 리턴한다.
    '''
    memo_word = f'{parent} {node}'
    if memo_word not in G.memo:
        children = list(filter(lambda x: x != parent, G.graph[node]))
        if not children:
            # print(f'{node} 는 자식이 없다.')
            G.memo[memo_word] = 1
        else:
            G.memo[memo_word] \
                = sum(sorted([dfs(node, child) for child in children], reverse=True)[:2]) + 1
    return G.memo[memo_word]

def solution(t):
    # 그래프 형성
    for i, j in t:
        G.graph[i].add(j)
        G.graph[j].add(i)

    return max([dfs(key, key) for key in G.graph.keys()])

# print(solution([[5,1], [2,5], [3,5], [3,6], [2,4], [4,0]]))
# print(solution([[2,5],[2,0],[3,2],[4,2],[2,1]]))
# print(solution([[0,1],[0,2]]))
# print(solution([[0,1],[0,2],[0,3]]))
# print(solution([[0,1],[1,2],[2,3],[3,4]]))