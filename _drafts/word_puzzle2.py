def match(a, b):
    if len(b) > len(a):
        return False
    for a_char, b_char in zip(a, b):
        if a_char != b_char:
            return False
    return True


def combinations(strs, t):
    '''
    strs 의 요소를 가지고 t[start:] 를 만드는 모든 경우의 수를 리턴합니다.
    각 원소는 무한정 사용할 수 있습니다.
    '''

    start = 0
    result = []
    min_len = 9999999999
    i = 0

    comb = []
    while i < len(strs):
        word = strs[i]

        if match(t[start:], word):
            comb.append(word)
            start = start + len(word)

            # comb 가 길어져 더 이상의 탐색이 무의미한 경우
            if len(comb) > min_len:
                start -= len(comb.pop())
                i += 1
                continue

            # 탐색이 끝난 경우.
            if start >= len(t):
                if ''.join(comb) == t:
                    result.append(comb[:])
                    min_len = len(comb) if min_len > len(comb) else min_len
                start -= len(comb.pop())
                i += 1
                continue

            i = 0
            continue
        elif i < len(strs) - 1:
            i += 1
            continue
        elif comb:
            last = comb.pop()
            start -= len(last)
            i = strs.index(last) + 1
        else:
            break


    return min_len if min_len != 9999999999 else -1

def solution(strs, t):
    return combinations(strs, t)

print(solution(['ba', 'na', 'n', 'a'], 'banana'))
print(solution(['ba', 'na', 'n', 'a'], 'bababa'))
print(solution(["ba", "an", "nan", "ban", "n"], "banana"))
print(solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple"))

