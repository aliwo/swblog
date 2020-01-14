
def solution(A):
    cache = [False for _ in range(len(A)+1+1)]
    cache[0] = True
    for elem in A:
        if elem < 0:
            continue
        cache[elem] = True
    for i in range(len(cache)+1):
        if not cache[i]:
            return i

assert solution([1,3,6,4,1,2]) == 5
assert solution([1,2,3]) == 4
assert solution([-1, -3]) == 1



