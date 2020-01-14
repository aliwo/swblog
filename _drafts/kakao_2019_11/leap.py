

def solution(stones, k):
    '''
    k = 3 고정이라고 생각해 보자.

    리스트를 길이 3씩 쪼개본다.

    2 4 5 = 가장 큰 수 5 위치는 2
    4 5 3 = 가장 큰 수 5 위치는 2
    5 3 2 = 가장 큰 수 5 위치는 2
    3 2 1 = 가장 큰 수 3 -> 쪼갠 조각의 max 중 가장 작으므로 3이 정답
    2 1 4 = 가장 큰 수 4
    1 4 2 = 가장 큰 수 4
    4 2 5 = 가장 큰 수 5
    2 5 1 = 가장 큰 수 5

    if 를 (n-2) * 3 만큼 실행.
    따라서 O(n) 에 해결 가능..

    로직은 다 맞으나 시간초과 ^^

    답은 minimum_max 를 항상 포함하며, 나머지는 모두 minimum_max 보다 작은 수 이다.
    답은 항상 1을 포함할까?

    minimum_max 의 위치와 값을 같이 저장한다고 하자.

    '''
    minimum_max = max(stones[0:k])
    i = 1

    while i + k <= len(stones):
        temp = max(stones[i:i+k])
        if minimum_max > temp:
            minimum_max = temp
        i += 1

    return minimum_max


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)) # 3 이 정답

