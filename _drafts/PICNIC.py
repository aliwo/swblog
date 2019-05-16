def findCombination(left_behind):

    if len(left_behind) == 0: # 기저 사례 1: 모든 친구를 짝 지은 경우
        results[cur_case] += 1
        return

    # left_behind 중 0 번째 멤버를 짝 지어줄 방법을 찾는다.
    for elem in friends_dicts[cur_case][left_behind[0]]:
        if elem in left_behind:
            new_left_behind = left_behind[1:]
            new_left_behind.remove(elem)
            findCombination(new_left_behind)


cases = int(input()) # case 의 수
results = [0] * cases # 결과값을 저장하는 전역변수
friends_dicts = [] # 친구 쌍을 저장하는 dict 의 리스트
for _ in range(cases):
    friends_dicts.append({}) # 빈 dict 생성
students = [0] * cases # 각 케이스별 학생의 수

for cur_case in range(cases):
    students[cur_case], _  = [int(x) for x in input().split()]

    for i in range(students[cur_case]):
        friends_dicts[cur_case][i] = [] # 모든 dict 가 한꺼번에 움직인다. 마치 같은 객체인것 처럼.

    friends = input().split()
    for i, x in enumerate(friends):
        if i % 2 == 0:
            a, b = int(friends[i]), int(friends[i+1])
            if a > b:
                friends_dicts[cur_case][b].append(a)
            else:
                friends_dicts[cur_case][a].append(b)


for cur_case in range(cases):
    findCombination(list(range(students[cur_case])))
    print(results[cur_case])
