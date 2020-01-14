# 재귀를 아예 안 쓰고 구현해보기
# 최종


class G:
    pending = set()
    bombed = 0
    board = []


def bomb():
    for i, j in reversed(sorted(G.pending)):
        G.board[i].pop(j)
        G.bombed += 1
    G.pending = set()


def traverse(i, j):
    found = False

    if i >= len(G.board) - 1 or j >= len(G.board[i]) - 1 or j >= len(G.board[i+1]) - 1:
        return found

    if G.board[i][j] == G.board[i][j+1] == G.board[i+1][j] == G.board[i+1][j+1]:
        for x, y in [(i + 1, j + 1), (i + 1, j), (i, j + 1), (i, j)]:
            G.pending.add((x, y))
        found = True

    return found


def solution(m, n, board):
    G.board = [[board[i][j] for i in reversed(range(m))] for j in range(n)]
    found = True
    while found:
        found = False
        for i in range(len(G.board) - 1):
            for j in reversed(range(len(G.board[i]) - 1)):
                if traverse(i, j):
                    found = True
        bomb()

    return G.bombed


assert solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]) == 15
