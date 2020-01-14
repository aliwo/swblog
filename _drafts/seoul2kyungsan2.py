
'''
내 솔루션 보다 살짝 빠르다.
리스트 캐시일때 ->
효율성  테스트
테스트 1 〉	통과 (2691.85ms, 173MB)
테스트 2 〉	통과 (2761.50ms, 177MB)
테스트 3 〉	통과 (3074.92ms, 184MB)
테스트 4 〉	통과 (2596.09ms, 171MB)
테스트 5 〉	통과 (2829.17ms, 181MB)
'''


'''
dict 캐시일 때 ->
테스트 1 〉	통과 (4510.30ms, 343MB)
테스트 2 〉	통과 (5434.84ms, 511MB)
테스트 3 〉	통과 (5609.90ms, 511MB)
테스트 4 〉	통과 (4517.05ms, 338MB)
테스트 5 〉	통과 (5464.98ms, 511MB)

dict 캐시가 어마어마하게 느리네 왜? 해시 연산 때문에? 문자열이 키라서?
1. 숫자 비교보다 문자열 비교가 훨씬 느리다.
2. 따라서 문자열을 key 로 하는 dict look up이 숫자를 key 로 하는 list look up 보다 느리다.

'''


def solution(K, travel):
    N = len(travel) + 1
    # (도시의 수 + 1) * 제한시간 크기의 이중 배열을 -1로 초기화
    # dict 를 안 쓰니까 번거롭게 초기화 하는 것 뿐... xt 의 cache 일 뿐이네.

    # 최적화도 안하는데 뭐 이렇게 빨라?
    cache = {}
    def pathSum(x, t): # t 는 여태까지의 총 소요시간 x 는 도시
        if t > K:
            return -1000000000
        if x == N:
            return 0
        key = f'{x}.{t}'
        if key in cache:
            return cache[key]
        cache[key] = max(travel[x - 1][1] + pathSum(x + 1, t + travel[x - 1][0]), travel[x - 1][3] + pathSum(x + 1, t + travel[x - 1][2]))
        return cache[key]
    sum = pathSum(1, 0)
    return sum


# assert solution(1650, [[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]]) == 660
assert solution(3000, [[1000, 2000, 300, 700], [1100, 1900, 400, 900], [900, 1800, 400, 700], [1200, 2300, 500, 1200]]) == 5900
