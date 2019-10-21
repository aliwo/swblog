import sys
sys.setrecursionlimit(99999999)


class G:
    money = []

cache = {}


def traverse(start, end):
    '''
    항상 오른쪽 (시계 방향)으로만 이동한다고 하자.
    '''
    if start >= end:
        return 0

    key = f'{start} {end}'

    if key in cache:
        return cache[key]

    if start + 2 >= end:
        cache[key] = max(G.money[start:end])
        return cache[key]

    cache[key] = max(G.money[start] + traverse(start + 2, end),
                  G.money[start + 1] + traverse(start + 3, end))

    return cache[key]


def solution(money):
    G.money = money
    return max(traverse(1, len(money)), money[0] + traverse(2, len(money)-1))


print(solution([1, 2, 3, 1]))
print(solution([1, 90, 3, 1, 90, 2]))
# print(solution([9, 3, 9, 3, 1]))
# print(solution())

# G.money = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# traverse(1, len(G.money))
