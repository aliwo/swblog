import sys
sys.setrecursionlimit(99999999)

class G:
    strs = []
    result = []
    t = ''
    min_len = 99999999


def match(a, b):
    if len(b) > len(a):
        return False
    for a_char, b_char in zip(a, b):
        if a_char != b_char:
            return False
    return True


def combinations(start, comb=[]):
    '''
    strs 의 요소를 가지고 t[start:] 를 만드는 모든 경우의 수를 리턴합니다.
    각 원소는 무한정 사용할 수 있습니다.
    '''
    if G.min_len < len(comb):
        return

    if start >= len(G.t):
        if ''.join(comb) == G.t:
            if G.min_len > len(comb):
                G.min_len = len(comb)
        return

    for word in G.strs:
        if match(G.t[start: start + len(word)], word):
            comb.append(word)
            combinations(start + len(word), comb)
            comb.pop()
    return comb


def solution(strs, t):
    G.strs = strs
    G.t = t
    combinations(0)
    return G.min_len if G.min_len != 99999999 else -1

# print(solution(['ba', 'na', 'n', 'a'], 'banana'))
print(solution(["ba", "an", "nan", "ban", "n"], "banana"))

