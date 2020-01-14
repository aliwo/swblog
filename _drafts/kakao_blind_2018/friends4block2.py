# del list 방식. 블럭 사이에 빈 공간이 있는 경우를 고려하지 못해서 오답.


class G:
    pending = {}
    bombed = 0
    board = []


def bomb():
    for key, (i, j) in G.pending.items():
        del G.board[key][i:j+1]
        G.bombed += j+1 - i
    G.pending = {}


def traverse(i, j):
    found = False

    if i >= len(G.board) - 1 or j >= len(G.board[i]) - 1 \
            or j >= len(G.board[i+1]) - 1 or j < 0:
        return found

    if G.board[i][j] == G.board[i][j+1] == G.board[i+1][j] == G.board[i+1][j+1]:
        for x, y in [(i+1, j-1), (i+1, j+1), (i+1, j), (i, j+1)]:
            traverse(x, y)
        if i in G.pending:
            G.pending[i] = (min(G.pending[i][0], j), max(G.pending[i+1][1], j+1))
        else:
            G.pending[i] = (j, j + 1)
        if i+1 in G.pending:
            G.pending[i+1] = (min(G.pending[i+1][0], j), max(G.pending[i+1][1], j+1))
        else:
            G.pending[i+1] = (j, j + 1)
        found = True

    return found


def solution(m, n, board):
    G.board = [[board[i][j] for i in reversed(range(m))] for j in range(n)]
    found = True
    while found:
        found = False
        for i in range(len(G.board)):
            for j in range(len(G.board[i])):
                if traverse(i, j):
                    found = True
                    bomb()
                    break
            if found:
                break

    return G.bombed




