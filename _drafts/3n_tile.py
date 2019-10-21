import sys
sys.setrecursionlimit(99999)

cache = {}
cache2 = {}


def calc_rest(n):
    '''
    겹치는 타일을 놓고 남은 공간을 채우는 경우의 수를 리턴합니다.
    '''
    print(f'rest 계산 {n}')
    if n <= 4:
        return 1
    if n in cache2:
        return cache2[n]

    cache2[n] = solution(n - 4) + calc_rest(n - 2)

    return cache2[n]


def solution(n):
    print(f'solution 계산 {n}')
    if n == 2:
        return 3
    if n in cache:
        return cache[n]

    answer = solution(n - 2) * 3
    answer += calc_rest(n) * 2
    cache[n] = answer

    return cache[n]


# print(solution(6))
print(solution(8))
