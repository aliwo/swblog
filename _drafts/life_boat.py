# 시간 초과다 흑흑... 정렬을 안 쓰고 해결하는 방법을 찾아야 하나? 정렬을 안 쓰면 find_fit 이 성립이 안된다.

# 둘 씩 탈 수 있는 모든 사람을 짝 지었다면 나머지는 남은 사람 수 만큼의 보트가 필요함.
# 둘 씩 짝 지을 수 있는 사람을 모두 짝 지었다는 걸 알 수 있으려면 어떻게 해야 할까?
# people[0] + people[1] 이 limit 을 초과하는 경우...
# if len(people) > 2 and people[0] + people[1] > limit:
#     return answer + len(people)
# 추가해도 시간초과 나더라...

# 남은 모든 사람이 둘 씩 탈 수 있는 경우

# 아래 if 문 추가해도 시간초과임
# if len(people) > 2 and people[0] + people[1] > limit:
#     return answer + len(people)
# if len(people) > 2 and len(people) % 2 == 0 and people[-1] + people[-2] < limit:
#     return answer + len(people) // 2


def find_fit(people, extra):

    for i in range(0, len(people)):
        if people[i] > extra:
            return i - 1
    else:
        return len(people) - 1 # 모든 사람이 둘 씩 탈 수 있는 경우 n^ 의 시간복잡도가 나온다.


def solution(people, limit):
    answer = 0

    # 퀵 소트 시간 복잡도 nlogn
    people = sorted(people)

    while people:

        extra = limit - people.pop()
        fit = find_fit(people, extra)

        if fit != -1:
            people.pop(fit)
        answer += 1

    return answer

# print(solution([70, 50, 80, 50], 100))
print(solution([3, 7, 3, 7, 10, 10, 10, 10], 10))


# [3, 7, 3, 7, 10, 10, 10, 10] -> 3 3 7 7 10 10 10 10 이 된다.


# 틀린 답
# def solution(people, limit):
#     answer = 1
#     boat_weight = 0
#     boat_people = 0
#
#     for elem in sorted(people):
#         in_boat_weight = boat_weight + elem
#         in_boat_people = boat_people + 1
#
#         if in_boat_weight <= limit and in_boat_people <= 2:
#             boat_weight = in_boat_weight
#             boat_people = in_boat_people
#         else:
#             answer += 1
#             boat_weight = elem
#             boat_people = 1
#
#     return answer

