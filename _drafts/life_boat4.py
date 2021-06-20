from math import ceil

# 2019-09-14 오후 11시:
# 맨 끝 인덱스 부터 for 문 탐색하는 방식 -> 0번째 인덱스 부터 for 문 탐색하는 방식
# 으로 수정해서 2개의 효율성 테스트를 통과할 수 있게 되었다.

# 0 번쨰 요소가 50 이라는 걸 알았다면,
# 50 을 초과하는 i 들은 싹다 혼자 태워서 보내버리면 된다.


def solution(people, limit):
    # half = limit // 2
    boats = 0
    people.sort()

    i = len(people) - 1
    while len(people):

        # 제일 무거운 사람을 pop 한다.
        space = limit - people[i]
        i -= 1
        people.pop()

        # 가벼운 사람들 중에 보트에 탈 꼭 맞는 사람을 찾는다.
        second_person_index = -1
        for j in range(len(people)):
            if people[j] > space:
                second_person_index = j - 1
                break

        # 맨 끝 사람과 그 뒤 사람을 같이 앉힐 수 있는 경우.
        # 싹 다
        if len(people) and j == len(people) - 1:
            if people[j] <= space:
                second_person_index = j

        if second_person_index != -1:
            people.pop(second_person_index)
            i -= 1

        boats += 1

        # 여기부터는 0 번쨰 인덱스를 사용한 최적화 로직
        if people:
            space = limit - people[0]
            for j in reversed(range(len(people))):
                if people[j] > space:  # 가장 얇은 사람이랑 타도 둘이서 못타는 뚱뚱이들
                    people._pop(j)
                    i -= 1
                    boats += 1
                else:  # 뚱뚱이가 없으면 break
                    break

    return boats

# assert solution([70, 50, 80, 50], 100) == 3
assert solution([70, 50, 80], 100) == 3

