
# 자꾸 틀린 답을 내니까, 느리더라도 정직하게 답을 내는 방법을 먼저 간단하게 구현해 보려고 한다.
# pop 을 쓰면 index 가 엉켜서 안됨...! 문제는 알았다.

def solution(food_times, k):
    i = 0
    while k > 0:
        k -= 1
        food_times[i] -= 1
        if not food_times:
            return -1
        i = i + 1 if i + 1 < len(food_times) else 0

    return i + 1 if i + 1 <= len(food_times) else 0

# assert solution([10, 7, 6, 5, 5, 3, 2], 24) == 5
assert solution([2, 3, 10, 7, 6, 5, 5], 24) == 7
# assert solution([3, 1, 2], 5) == 1
# assert solution([3, 1, 2], 7) == -1

