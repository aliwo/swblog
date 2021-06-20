# 재귀를 아예 안 쓰고 구현해보기
# 최종

'''
정확성  테스트
테스트 1 〉	통과 (0.07ms, 10.9MB)
테스트 2 〉	통과 (0.09ms, 10.7MB)
테스트 3 〉	통과 (0.05ms, 10.9MB)
테스트 4 〉	통과 (1.76ms, 10.9MB)
테스트 5 〉	통과 (31.45ms, 10.8MB)
테스트 6 〉	통과 (3.14ms, 10.8MB)
테스트 7 〉	통과 (0.97ms, 10.8MB)
테스트 8 〉	통과 (1.75ms, 10.8MB)
테스트 9 〉	통과 (0.08ms, 10.8MB)
테스트 10 〉	통과 (0.60ms, 10.9MB)
테스트 11 〉	통과 (1.76ms, 10.9MB)
'''


class G:
    pending = set()
    bombed = 0
    board = []


def bomb():
    for i, j in reversed(sorted(G.pending)):
        G.board[i]._pop(j)
        G.bombed += 1
    G.pending = set()


def traverse(i, j):
    if j >= len(G.board[i + 1]) - 1:
        return

    if G.board[i][j] == G.board[i][j + 1] == G.board[i + 1][j] == G.board[i + 1][j + 1]:
        for x, y in [(i + 1, j + 1), (i + 1, j), (i, j + 1), (i, j)]:
            G.pending.add((x, y))


def solution(m, n, board):
    G.board = [[board[i][j] for i in reversed(range(m))] for j in range(n)]

    while True:
        for i in range(len(G.board) - 1):
            for j in range(len(G.board[i]) - 1):
                traverse(i, j)
        if not G.pending:
            break
        bomb()

    return G.bombed

assert solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]) == 15
