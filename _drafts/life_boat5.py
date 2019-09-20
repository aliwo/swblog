# 2019-09-15 리스트를 0번 부터 회전하고,
# 리스트 초반부에는 삭제 연산을 하지 않는 새로운 로직을 설계합니다.

# i 가 하나 남아있다고 해도 기저 사례 없이 해결 됩니다.

def solution(people, limit):
    boats = 0
    people.sort()
    i = 0  # 0번 부터

    while i <= len(people) - 1:

        # 혼자 타아만 하는 사람을 색출한다.
        space = limit - people[i]

        while len(people):
            j = len(people) - 1
            if i == j:
                return boats + 1

            weight = people.pop(j)
            boats += 1 # 일단 마지막 뚱뚱이 하나 태움.
            if weight <= space: # i 랑 탈 수 있다면 함께 태워 보낸다.
                break

        i += 1

    return boats

# 2명씩 탈 수도 있고, 1명이 탈 수도 있고
assert solution([70, 50, 80, 50], 100) == 3 # 짝
assert solution([70, 50, 80, 50, 50], 100) == 4 # 홀

# 다 따로 탐.
assert solution([70, 50, 80], 100) == 3 # 홀
assert solution([70, 80], 100) == 2 # 짝

# 다 둘 씩 탐.
assert solution([50, 50, 50], 100) == 2 # 홀
assert solution([50, 50, 50, 50], 100) == 2 # 짝
assert solution([5, 5, 5, 5], 100) == 2 # 짝

# 다 뚱뚱이들
assert solution([100, 100], 100) == 2
assert solution([100, 100, 100], 100) == 3

# 1개 짜리 리스트
assert solution([100], 100) == 1
assert solution([50], 100) == 1



