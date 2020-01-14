# 조건
import copy

m = 6  # 높이
n = 6  # 넓이
board = ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']

# %%
# [정답버전]
b = board
for i in range(m):
    b[i] = list(b[i])
while True:
    board2 = copy.deepcopy(board)
    # 2. 터질좌표 찾기
    sero = []  # 세로 좌표 저장
    garo = []
    for i in range(n - 1):
        for j in range(m - 1):
            if board[i][j] == board[i + 1][j + 1] and board[i][j] == board[i + 1][j] and board[i][j] == board[i][j + 1]:
                sero.append(i)
                garo.append(j)
    # print(sero, garo)  # 터질좌표모음
    # print(board)

    # 3. 터질좌표를 받아 #처리

    for i, j in zip(sero, garo):
        board[i][j], board[i + 1][j], board[i][j + 1], board[i + 1][j + 1] = '#', '#', '#', '#'

    for i in board:
        pass
        # print(i)

    # 4. 내려가는 while문 작업

    while True:
        unchange = True
        for i in range(n - 1, 0, -1):
            for j in range(m):
                # print(i, j)
                if board[i][j] == '#' and board[i - 1][j] != '#':
                    tmp = board[i][j]
                    board[i][j] = board[i - 1][j]
                    board[i - 1][j] = tmp
                    unchange = False
        if unchange:
            break
        # print(board)
        # print(board2)
    if board == board2:
        break

print(board)
