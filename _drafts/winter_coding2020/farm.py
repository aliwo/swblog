import sys
sys.setrecursionlimit(99999)

class G:
    v = []
    raddish = 0
    sweet_potato = 0
    potato = 0

    @classmethod
    def add_cnt(cls, i, j):
        if cls.v[i][j] == 0:
            cls.raddish += 1
        elif cls.v[i][j] == 1:
            cls.sweet_potato += 1
        elif cls.v[i][j] == 2:
            cls.potato += 1



def dfs(visited, i, j):
    visited._add(f'{i} {j}')

    # 상하좌우
    next_move = []
    if i > 0 and G.v[i-1][j] == G.v[i][j]: # 상
        next_move.append(f'{i-1} {j}')
    if i < len(G.v) - 1 and G.v[i+1][j] == G.v[i][j]: # 하
        next_move.append(f'{i+1} {j}')
    if j > 0 and G.v[i][j-1] == G.v[i][j]: # 좌
        next_move.append(f'{i} {j-1}')
    if j < len(G.v[i]) - 1 and G.v[i][j+1] == G.v[i][j]: # 우
        next_move.append(f'{i} {j+1}')

    for elem in next_move:
        if elem not in visited:
            dfs(visited, int(elem.split(' ')[0]), int(elem.split(' ')[1]))



def solution(v):
    G.v = v

    visited = set()
    for i in range(len(v)):
        for j in range(len(v[i])):
            if f'{i} {j}' not in visited:
                G.add_cnt(i, j)
                dfs(visited, i, j)


    return [G.raddish, G.sweet_potato, G.potato]


print(solution([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]))