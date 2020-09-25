
def count(a, i):
    dead_cnt = 0

    # 왼쪽으로 이동
    for j in reversed(range(0, i)):
        if a[i] < a[j]:
            dead_cnt += 1
        if dead_cnt > 2:
            return 0

    for j in range(i+1, len(a)):
        if a[i] < a[j]:
            dead_cnt += 1
        if dead_cnt > 2:
            return 0

    return 1



def solution(a):
    answer = 2
    for i in range(1, len(a)-1):
        answer += count(a, i)
    return answer




# print(smallest_and_second_smallest([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
# print(solution([9, -1, -5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))