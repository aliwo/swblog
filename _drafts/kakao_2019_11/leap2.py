

def max_pos(li):
    max = li[0]
    pos = 0
    for i in range(1, len(li)):
        if li[i] > max:
            max = li[i]
            pos = i

    return max, pos



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
    minimum_max, i = max_pos(stones[0:k])

    while i <= len(stones) - k:
        temp_max, pos = max_pos(stones[i:i+k])
        if minimum_max > temp_max:
            minimum_max = temp_max

        i += pos + 1 # 현재 max 보다 더 작은 max 를 찾는것이 목적이기 때문에 현재 max 이후 부터 이어서 계산하면 됩니다.

    return minimum_max


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)) # 3 이 정답

