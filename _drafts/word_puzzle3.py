# 2019-10-21
# 재귀호출을 쓰지 않고 완전히 성공하는 알고리즘을 만들었지만
# 오히려 재귀호출 쓸 때 보다 더 느려져 버렸다.


def match(a, b):
    if len(b) > len(a):
        return False
    for a_char, b_char in zip(a, b):
        if a_char != b_char:
            return False
    return True


def solution(strs, t):
    min_len = 99999999
    combinations = [] # (단어, 인덱스) 튜플을 저장하는 리스트
    start = 0
    i = 0

    # combinations 에 요소를 하나 추가합니다.
    while i < len(strs):
        if match(t, strs[i]):
            combinations.append((strs[i], i))
            start = len(strs[i])
            break
        i += 1
    else:
        return -1
    i = 0

    while combinations or i < len(strs):

        if min_len <= len(combinations) or i >= len(strs):
            temp = combinations.pop()
            i = temp[1]
            start -= len(temp[0])

        elif match(t[start: start + len(strs[i])], strs[i]):
            combinations.append((strs[i], i))
            start += len(strs[i])

            # 탐색이 끝난 경우
            if start >= len(t):
                if ''.join([x[0] for x in combinations]) == t:
                    min_len = len(combinations) if len(combinations) < min_len else min_len
                    temp = combinations.pop()
                    i = temp[1]
                    start -= len(temp[0])
            else:
                i = 0
                continue
        i += 1

    return min_len if min_len != 99999999 else -1

print(solution(['ba', 'na', 'n', 'a'], 'banana'))
print(solution(['ba', 'na', 'n', 'a'], 'bababa'))
print(solution(["ba", "an", "nan", "ban", "n"], "banana"))
print(solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple"))

