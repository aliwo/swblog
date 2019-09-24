
# 아무리 봐도 종만북 위상정렬 로직이 틀린것 같아서 파이썬으로 최대한 비슷하게 구현해 봅니다.
# 응 종만이가 맞아~
seen = []
order = []
adj = [[1], [2], [], [2]]


def dfs(here):
    '''
    세상에 이게 왜 되지
    '''
    seen.append(here)
    for i in range(len(adj)):
        if i in adj[here] and i not in seen:
            dfs(i)
    order.append(here)


def topologicalSort():
    for i in range(len(adj)):
        if i not in seen:
            dfs(i)
    order.reverse()
    print(order)


topologicalSort()

