def alter_alpha(to):
    num = ord(to)
    return num - 65 if num < 79 else 90 - num + 1


def traverse(done, i):
    # TODO ; left_cnt 보다 right_cnt 가 크면 right 탐색을 중단 하는 최적화가 가능할까? 답에 영향이 없을까?

    # 기저 사례
    if False not in done:
        return 0

    left_cnt = right_cnt = 0
    left_i = right_i = i

    for _ in range(len(done)):
        if done[left_i] == False:
            break
        left_i = left_i - 1 if left_i > 0 else len(done) - 1
        left_cnt += 1
    done[left_i] = True
    left_cnt += traverse(done, left_i)
    done[left_i] = False

    for _ in range(len(done)):
        if done[right_i] == False:
            break
        right_i = right_i + 1 if right_i + 1 < len(done) else 0
        right_cnt += 1
    done[right_i] = True
    right_cnt += traverse(done, right_i)
    done[right_i] = False

    return min(left_cnt, right_cnt)

def solution(name):
    '''
    done 을 쓰지 않고 해결할 방법은 없을까?
    '''
    cnt = 0
    done = [False] * len(name)

    for i in range(len(name)):
        if name[i] == 'A':
            done[i] = True
        else:
            cnt += alter_alpha(name[i])

    return cnt + traverse(done, 0)


# assert alter_alpha('B') == 1
# assert alter_alpha('N') == 13
# assert alter_alpha('Z') == 1
# assert alter_alpha('Y') == 2
#
# assert alter_cursor([True, False, False], 0) == 2

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

# 길이가 13 인 name 집중 테스트
assert solution('AAZAAZAAZAAZA') == 15
assert solution('EOIZRPJUTDHQY') == 101 # ?
assert solution('IUFYPWDNURSDH') == 97
assert solution('RNRHPGTWSPVEN') == 119
assert solution('EEFCBLTGKZFLV') == 84
assert solution('CZDGCCUYPJATF') == 68
assert solution('AAABAAAB') == 7
assert solution('AABAAAAAAAAAABAA') == 9
assert solution('ABABAAAAAAABA') == 10
assert solution('AABAAAAAAAAAAB') == 6





