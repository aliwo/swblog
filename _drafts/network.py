
# 간단한 dfs_all 문제.

graph = {

}

def dfs(here, visited=[]):
    visited.append(here)
    for node in graph[here]:
        if node not in visited:
            dfs(node, visited)


def dfs_all():
    visited = []
    networks = 0
    for node in graph.keys():
        if node not in visited:
            networks += 1
            dfs(node, visited)

    return networks

def solution(n, computers):
    for i, adjs in enumerate(computers):
        graph[i] = []
        for j in range(len(adjs)):
            if i == j:
                continue
            if adjs[j]:
                graph[i].append(j)

    return dfs_all()


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))


