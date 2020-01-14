# 조건
import copy

m = 6  # 높이
n = 6  # 넓이
board = ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']

# 내가 짠 코드

# 1. 요소 뽑기
b = board
for i in range(m):
    b[i] = list(b[i])
while True:
    b2 = copy.deepcopy(b)
    # 2. 터트릴 요소 찾기
    x = []  # x좌표 : 가로
    y = []  # y좌표 : 세로(높이)
    for i in range(m - 1):
        for j in range(n - 1):
            # print(i, j)
            if b[i][j] == b[i + 1][j] and b[i][j] == b[i][j + 1] and b[i][j] == b[i + 1][j + 1]:
                x.append(j)
                y.append(i)

    # 3. 터트릴 요소 잘보이게 바꾸기
    for i, j in zip(y, x):
        b[i][j], b[i + 1][j], b[i][j + 1], b[i + 1][j + 1] = '#', '#', '#', '#'

    # print(b)
    # 4. '#'없애버리고 쭉쭉쭉쭉 내리기
    while True:
        a = True
        for i in range(m - 1):  # 위에서 내려가는 거니 비교가능
            for j in range(n):
                if b[i + 1][j] == '#' and b[i][j] != '#':
                    tmp = b[i + 1][j]
                    b[i + 1][j] = b[i][j]
                    b[i][j] = tmp
                    a = False
        if a:
            break
        # while문 잘못씀
    # print(b)
    if b == b2:
        break

print(b)

