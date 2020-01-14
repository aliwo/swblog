
adj = {
    1: {2, 3, 4, 5},
    2: {1, 3, 4, 6},
    3: {1, 2, 5, 6},
    4: {1, 2, 5, 6},
    5: {1, 3, 4, 6},
    6: {2, 3, 4, 5}
}


def move(pip, num):
    '''
    주어진 pip 을 num 으로 맞추는데 필요한 move 의 수를 리턴합니다.
    '''
    if pip == num:
        return 0
    if num in adj[pip]:
        return 1
    return 2


def solution(A):
    '''
    주사위 갯수는 1 ~ 100개
    시간은 상관 없다. -> 가벼운 마음으로 완전 탐색 가능!
    사실 전부 1로 통일, 전부 2로 통일... 전부 3으로 통일도 가능함 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

    move 는 lookup 연산만 한다. (dict 안의 set 을 lookup 하므로, 상수시간이다.)
    많이 봐줘서... 곱하기 같은 간단한 연산이라고 치고...

    주사위가 최대 100개, 주사위 눈은 1~6개로 6개.
    따라서 600번의 move 연산을 한다.
    상용 CPU 가 더하기 같은 간단한 연산은 1초에 약 2억번의 연산을 한다고 가정...
    6개의 temp 값을 정렬하는 건 "지배하는 연산"이 아니므로 무시하고...
    따라서

    solution() 은 1초 미만으로 실행 가능!

    '''
    result = []

    for i in range(1, 7):
        temp = 0
        for pip in A:
            temp += move(pip, i)
        result.append(temp)

    return sorted(result)[0]

# print(solution([1, 2, 3]))
# print(solution([1, 1, 6]))
# print(solution([1, 6, 2, 3]))

