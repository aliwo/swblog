def alter_alpha(to):
    '''
    A 를 to 로 바꾸기 위해서 몇 번 조작을 해야하는지를 리턴합니다.
    A 는 ord 65 이며
    Z 는 ord 90 입니다.
    알파벳은 총 26개 이므로, 사실 down 은 13 번째 까지만 회전하면 될 것 같네요
    '''
    down = 0
    up = 1 # 이미 한 칸 위로 올라간, Z 에서 시작합니다.
    for i in range(65, 79):
        if ord(to) == i:
            break
        down += 1

    for i in reversed(range(78, 91)):
        if ord(to) == i:
            break
        up += 1

    return min(down, up)


def alter_cursor(done, i):
    '''
    만약 left 와 right 가 같은 경우일 지라도,
    남아 잇는 False 에 따라서 최적해가 다르다.

    '''
    left = right = i
    left_cnt = right_cnt = 1
    if False not in done:
        return [-1, 0]

    while True:
        left = left - 1 if left > 0 else len(done) - 1
        if done[left] == False:
            break
        left_cnt += 1

    while True:
        right = right + 1 if right < len(done) - 1 else 0
        if done[right] == False:
            break
        right_cnt += 1

    if left_cnt == right_cnt: # alter_cursor 를 재귀호출 해야 함!
        temp_done = done[:]
        temp_done[left] = True
        left_i, left_cnt = alter_cursor(temp_done, left)

        temp_done[left] = False

        temp_done[right] = True
        right_i, right_cnt = alter_cursor(temp_done, right)

        if left_cnt > right_cnt: # 이것도 같을 확률이 있는거 아닌가?
            pass




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
assert solution('AAAAAAAAAAAAAAAAAAA') == 0
assert solution('BB') == 3
assert solution('ABCAZYX') == 15
assert solution('AN') == 14 # 13 + 1
assert solution('ANM') == 27 # 1 + 13 + 1 + 12
assert solution('AAABAAAAAAB') == 7 # 1 + 1 + 4 + 1
# 이동 -> A 1 B 2 C 3 A 4 Z 5 Y 6 X 이동은 6 번
# 1 2 1 2 3 -> 9번



