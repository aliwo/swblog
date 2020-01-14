'''
정확성  테스트
테스트 1 〉	통과 (0.10ms, 10.8MB)
테스트 2 〉	통과 (0.11ms, 10.8MB)
테스트 3 〉	통과 (0.05ms, 10.8MB)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	통과 (49.77ms, 10.7MB)
테스트 6 〉	통과 (20.96ms, 10.8MB)
테스트 7 〉	통과 (8.08ms, 10.7MB)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	통과 (0.09ms, 10.7MB)
테스트 10 〉	통과 (17.52ms, 10.7MB)
테스트 11 〉	실패 (시간 초과)
'''

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
        for x, y in [(i+1, j+1), (i+1, j), (i, j+1)]:
            traverse(x, y)
        for x, y in [(i + 1, j + 1), (i + 1, j), (i, j + 1), (i, j)]:
            G.pending.add((x, y))
        found = True

    return found


def solution(m, n, board):
    G.board = [[board[i][j] for i in reversed(range(m))] for j in range(n)]
    done = 0 # done - 1 라인은 더 이상 순회하지 않아도 된다.
    found = True
    while found:
        found = False
        for i in range(done, len(G.board) - 1):
            for j in reversed(range(done, len(G.board[i]) - 1)):
                if traverse(i, j):
                    found = True
            if not found:
                done = i + 1
        bomb()

    return G.bombed


assert solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]) == 15
