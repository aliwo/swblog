

def findCombination(left_behind, picked):
    '''
    picked 는 set 입니다.
    '''

    # 기저 사례 1: 모든 친구를 짝 지은 경우
    if len(left_behind) == 0:
        if picked not in results[cur_case]:
            results[cur_case].append(picked)
        return

    # left_behind 중 0 번째 멤버를 짝 지어줄 방법을 찾는다.
    for elem in friends_list[cur_case]:
        new_left_behind = left_behind[:]
        new_picked = set(picked)
        if elem[0] in new_left_behind and elem[1] in new_left_behind:
            new_left_behind.remove(elem[0])
            new_left_behind.remove(elem[1])
            new_picked.add(elem)
            findCombination(new_left_behind, new_picked)


cases = int(input())
results = [[]] * cases
friends_list = [[]] * cases
students = [0] * cases

for cur_case in range(cases):
    students[cur_case], _  = input().split()
    input_list = [int(x) for x in input().split()]

    for i, x in enumerate(input_list):
        if i % 2 == 0:
            friends_list[cur_case].append((input_list[i], input_list[i+1]))

for cur_case in range(cases):
    findCombination(list(range(int(students[cur_case]))), set())
    print(len(results[cur_case]))
