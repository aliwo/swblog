# 2019-10-18 재귀 알고리즘으로는 정확성 테스트는 모두 통과하지만 효율성 테스트는 모두 실패했다.
# 그래서 그 다음날인 오늘, 재귀를 사용하지 않는 상향식 DP 로 바꿔서 풀어보려고 한다.


def solution(money):
    '''
    0 번을 골랐을 때 맨 끝 집도 고를 수 있는 로직이라 정확도가 낮음.
    '''
    cache = [money[0], max(money[0], money[1])]

    for i in range(2, len(money)):
        cache.append(max(cache[i-2] + money[i], cache[i-1]))

    return cache[-1]


# print(solution([2, 2, 3, 1]))
# print(solution([1, 9, 1]))
# print(solution([1, 8, 8]))
# print(solution([8, 1, 8]))
# print(solution([8, 8, 8]))
# print(solution([8, 8, 8, 8]))
# print(solution([8, 8, 8, 8, 8]))
# print(solution([1, 90, 3, 1, 90, 2]))
# print(solution([1, 90, 3, 1, 90, 2]))
# print(solution([0, 90, 3, 1, 90, 2]))
# print(solution([0, 90, 0, 0, 90, 2]))
# print(solution([0, 0, 90, 0, 90, 2]))
# print(solution([0, 0, 0, 0, 90, 90]))
# print(solution([0, 0, 0, 0, 180, 90]))
# print(solution([0, 0, 0, 180, 0, 90]))
# print(solution([180, 0, 0, 180, 0, 90]))
# print(solution([180, 0, 0, 181, 0, 90]))
# print(solution([0, 90, 0, 181, 0, 90]))
# print(solution([0, 90, 0, 181, 0, 90]))
# print(solution([0, 0, 3, 1, 90, 2])) # 정답은 93
# print(solution([9, 3, 9, 3, 1]))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9])) # 정답은 24. 3 5 7 9 선택. 내 함수는 25 cache[-2] < cache[-1]
# print(solution([9, 8, 7, 6, 5, 4, 3, 2, 1])) # 정답은 24. 3 5 7 9 선택. 내 함수는 25 cache[-2] < cache[-1]
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 10, 9])) # 정답 29. cache[-2] < cache[-1]

# def solution(money):
#     cache = [money[0], max(money[0], money[1])]
#     zero_include = money[0] > money[1]
#
#     for i in range(2, len(money)):
#         if cache[i-2] + money[i] > cache[i-1]:
#             cache.append(cache[i-2] + money[i])
#             zero_include = not zero_include
#         else:
#             cache.append(cache[i-1])
#
#     # print(zero_include)
#
#     if zero_include:
#         return cache[-2]
#
#     return cache[-1]
