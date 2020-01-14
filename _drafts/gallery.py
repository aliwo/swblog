
gallery = {
    0 : [1, 4],
    1 : [0, 2, 3],
    2 : [1, 5],
    3 : [1],
    4 : [0],
    5 : [2],
}


def dfs(here, visited=[]):
    visited.append(here)
    



def solution():
    cnt = 0
    for i in range(6):
        if dfs(i) == 'UNWATCHED':
           cnt += 1

    return cnt



