
graph = {}


def dfs(node, visited=[]):
    visited.append(node)
    for n in graph[node]:
        if n not in visited:
            dfs(n, visited=visited)


def dfs_all():
    visited = []
    dfs_call_cnt = 0
    for key, value in graph.items():
        if key not in visited:
            dfs(key, visited=visited)
            dfs_call_cnt += 1
    return dfs_call_cnt


def solution(n, costs):
    costs.sort(key=lambda x:x[2]) # 건설 비용을 기준으로 정렬합니다.
    total_cost = 0

    # 그래프 형성
    for i in range(n):
        graph[i] = []

    # 다리 건설
    for elem in costs:
        before_construct = dfs_all()

        graph[elem[0]].append(elem[1])
        after_construct = dfs_all()

        if after_construct == before_construct: # after 가 before 보다 큰 경우는 없다.
            graph[elem[0]].pop()
            continue

        total_cost += elem[2]

        if after_construct == 1:
            # 모든 섬이 연결되었다면
            return total_cost

    # raise Exception # 여기 닿을 때가 있네?

assert solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]) == 4


