
kimchi_soup = {
    1: [2],
    2: [3],
    3: [4],
    4: [5],
    5: [],
    6: [7, 8, 9],
    7: [1],
    8: [2],
    9: [4],
    10: [3],
}

visited = []
topology = []
anchor = 0

def dfs(here):
    visited.append(here)
    for i in kimchi_soup[here]:
        if i not in visited:
            dfs(i)

def dfs_all():
    global anchor
    for key, value in kimchi_soup.items():
        if key not in visited:
            dfs(key)
            # topology.append(visited[anchor:])
            # anchor = len(visited) # anchor 의 존재로 인해 위상정렬 때 중복을 피한다.

dfs_all()

print('위상정렬!')
print([elem for i in reversed(range(len(topology))) for elem in topology[i]])
# 올바른 위상정렬 순서는
# 10 -> 6 7 8 9 -> 1 2 3 4 5
