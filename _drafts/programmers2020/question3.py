
def solution(a):
    if len(a) <= 3:
        return len(a)

    right_min_meno = {len(a)-1: a[len(a)-1]}
    answer = 2
    left_min= a[0]
    right_min = min(a[2:len(a)])

    for i in reversed(range(1, len(a)-1)):
        right_min_meno[i] = min(a[i+1], a[i])

    for i in range(1, len(a)-1):

        # "가장 작은 수" 가 자신일 때
        if left_min > a[i] or right_min > a[i]:
            answer += 1

        if a[i] < left_min:
            left_min = a[i]

        # 오른쪽 min 값 재 할당
        if a[i+1] == right_min and a[i+2:len(a)]:
            right_min = right_min_meno[i+2]

    return answer




# print(smallest_and_second_smallest([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
# print(solution([9, -1, -5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))