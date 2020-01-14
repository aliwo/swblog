

def solution(A, K):
    if not A:
        return []
    i = K % len(A)
    return A[len(A)-i:] + A[0:len(A)-i]


assert solution([3, 8, 9, 7, 6], 1) == [6, 3, 8, 9, 7]
assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
assert solution([3, 8, 9, 7, 6], 6) == [6, 3, 8, 9, 7]
assert solution([3, 8, 9, 7, 6], 5) == [3, 8, 9, 7, 6]
