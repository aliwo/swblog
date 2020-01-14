
def pick_doll(board, stk, pick):
    for layer in board:
        if layer[pick] != 0:
            stk.append(layer[pick])
            layer[pick] = 0
            return


def solution(board, moves):
    answer = 0
    stk = []

    for pick in moves:
        pick_doll(board, stk, pick-1)
        if len(stk) >= 2:
            if stk[-1] == stk[-2]:
                stk.pop()
                stk.pop()
                answer += 2

    return answer


board1 = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
]

moves = [1,5,3,5,1,2,1,4]
# 4 3 1 1 터짐
# 3 터짐
# 2 0 4
print(solution(board1, moves))

