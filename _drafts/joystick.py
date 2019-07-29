def alter_alpha(to):
    '''
    A 를 to 로 바꾸기 위해서 몇 번 조작을 해야하는지를 리턴합니다.
    A 는 ord 65 이며
    Z 는 ord 90 입니다.
    알파벳은 총 26개 이므로, 사실 down 은 13 번째 까지만 회전하면 될 것 같네요
    '''
    down = 0
    for i in range(65, 91):
        if ord(to) == i:
            break
        down += 1

    up = 1 # 이미 한 칸 위로 올라간, Z 에서 시작합니다.
    for i in reversed(range(65, 91)):
        if ord(to) == i:
            break
        up += 1

    return min(down, up)


def alter_cursor(done, i):
    left = right = i
    cnt = 1
    while False in done:
        left = left - 1 if left > 0 else len(done) - 1
        right = right + 1 if right < len(done) - 1 else 0
        if done[left] == False:
            return left, cnt
        if done[right] == False:
            return right, cnt
        cnt += 1

    return [-1, 0]

def solution(name):
    cnt = 0
    done = [False] * len(name)

    for i in range(len(name)):
        if name[i] == 'A':
            done[i] = True

    i = 0
    while i != -1:
        cnt += alter_alpha(name[i])
        done[i] = True
        i, alter_cnt = alter_cursor(done, i)
        cnt += alter_cnt
    return cnt

assert alter_alpha('B') == 1
assert alter_alpha('Z') == 1
assert alter_alpha('Y') == 2

assert alter_cursor([True, False, False], 0) == (2, 1)
assert alter_cursor([True, False, False, False], 0) == (3, 1)
assert alter_cursor([True, True, False, False, True], 0) == (3, 2)
assert alter_cursor([True, True, False, True, True], 0) == (2, 2)

assert solution('JEROEN') == 56
assert solution('JAN') == 23
assert solution('AAA') == 0
assert solution('ABCAZYX') == 15
assert solution('AN') == 14 # 13 + 1
assert solution('ANM') == 27 # 13 + 13 + 1
# 이동 -> A 1 B 2 C 3 A 4 Z 5 Y 6 X 이동은 6 번
# 1 2 1 2 3 -> 9번



