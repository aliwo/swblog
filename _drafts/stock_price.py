def solution(prices):
    cache = []
    answer = [0] * len(prices)

    for i in range(len(prices)):
        j = len(cache) - 1
        while j >= 0:
            if cache[j][0] > prices[i]:
                elem = cache.pop()
                answer[elem[1]] = i - elem[1]
            else:
                break
            j -= 1

        cache.append((prices[i], i))

    # 스택의 남은 요소 정리
    while cache:
        elem = cache.pop()
        answer[elem[1]] = len(prices) - 1 - elem[1]

    return answer


print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]

# 2 의 인덱스는 3

# cache 는  [ (1,0), (2,1), (3,2)]
# cache 는  [ (1,0), (2,1), (3,2)]

