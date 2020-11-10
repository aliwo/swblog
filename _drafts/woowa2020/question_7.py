
# 와 N = 1 예외처리를 안해서 틀리다니

directions_dict = {
    'up_right': lambda x, y, step: (x+1, y-1, 2 + step),
    'down_left': lambda x, y, step: (x-1, y+1, 2 + step),
}


def is_blocked(x, y, n, direction):
    '''
    현재 지점에서 direction 방향으로 이동할 수 있는지를 반환합니다.
    '''
    if x == 1 and y == 2:
        print(x, y)
    x, y, _ = directions_dict[direction](x, y, 0)
    if (not (0 <= x < n)) or (not (0 <= y < n)):
        return True


def solution(n, horizontal):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    cur_direction = None
    step = 0
    x = 0
    y = 0

    if horizontal:
        step += 1
        x += 1
        cur_direction = 'down_left'
        answer[y][x] = step
    else:
        step += 1
        y += 1
        cur_direction = 'up_right'
        answer[y][x] = step

    while x != n - 1 or y != n - 1:
        if is_blocked(x, y, n, cur_direction):
            if cur_direction == 'up_right':
                if x < n - 1: # 오른쪽으로 이동할 수 있다면
                    x += 1
                    step += 1
                    answer[y][x] = step
                else: # 안되면 아래로 내려간다.
                    y += 1
                    step += 1
                    answer[y][x] = step
                cur_direction = 'down_left'
            else:
                if y < n - 1: # 아래로 내려갈 수 있다면
                    y += 1
                    step += 1
                    answer[y][x] = step
                else: # 안되면 오른쪽으로 이동
                    x += 1
                    step += 1
                    answer[y][x] = step
                cur_direction = 'up_right'
        else:
            # block 되지 않았을 때
            x, y, step = directions_dict[cur_direction](x, y, step)
            answer[y][x] = step

    return answer


# print(solution(4, True)) # [[0,1,8,9],[3,6,11,20],[4,13,18,21],[15,16,23,24]]
# print(solution(5, False)) # [[0,3,4,15,16],[1,6,13,18,31],[8,11,20,29,32],[9,22,27,34,39],[24,25,36,37,40]]
# print(solution(6, False))
print(solution(1, False))